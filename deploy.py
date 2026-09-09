#!/usr/bin/env python3
"""
EuroID Deployment Script for Tron MainNet
Uses web3.py to deploy contract
"""

import json
import sys
import os
from pathlib import Path

# Fix Windows encoding
if sys.platform == "win32":
    os.environ["PYTHONIOENCODING"] = "utf-8"
    sys.stdout.reconfigure(encoding='utf-8')

from web3 import Web3

# Configuration
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
ETH_RPC = os.getenv("ETH_RPC", "https://rpc.ankr.com/eth")
GUARDIAN_OWNER = os.getenv("GUARDIAN_OWNER", "0x1b1053887700691Fc6AF89fFc5Cab725BF6a00d9")
GUARDIAN_TREASURY = os.getenv("GUARDIAN_TREASURY", "0x1b1053887700691Fc6AF89fFc5Cab725BF6a00d9")

if not PRIVATE_KEY:
    print("❌ Error: PRIVATE_KEY environment variable not set")
    sys.exit(1)

def main():
    print("=" * 60)
    print("EuroID Deployment on Ethereum MainNet")
    print("=" * 60)

    # Connect to Ethereum
    print(f"\n[*] Connecting to Ethereum RPC: {ETH_RPC}")
    w3 = Web3(Web3.HTTPProvider(ETH_RPC))

    if not w3.is_connected():
        print("❌ Failed to connect to Tron RPC")
        return False

    print("✅ Connected to Tron")

    # Load compiled contract
    print("\n[*] Loading compiled contract...")
    artifact_path = Path("out/EuroID.sol/EuroID.json")

    if not artifact_path.exists():
        print(f"❌ Artifact not found: {artifact_path}")
        return False

    with open(artifact_path) as f:
        artifact = json.load(f)

    abi = artifact.get("abi", [])
    bytecode = artifact.get("bytecode", {}).get("object", "")

    if not bytecode:
        print("❌ No bytecode found in artifact")
        return False

    print(f"✅ Contract loaded (bytecode length: {len(bytecode)})")

    # Get account
    print(f"\n[*] Setting up account with private key")
    acct = w3.eth.account.from_key(PRIVATE_KEY)
    print(f"✅ Account: {acct.address}")
    print(f"   Owner: {GUARDIAN_OWNER}")
    print(f"   Treasury: {GUARDIAN_TREASURY}")

    # Get nonce and gas price
    print("\n[*] Getting network parameters...")
    try:
        nonce = w3.eth.get_transaction_count(acct.address)
        gas_price = w3.eth.gas_price
        print(f"✅ Nonce: {nonce}")
        print(f"✅ Gas Price: {w3.from_wei(gas_price, 'gwei')} Gwei")
    except Exception as e:
        print(f"❌ Error getting network params: {e}")
        return False

    # Create contract factory
    print("\n[*] Creating contract factory...")
    Contract = w3.eth.contract(abi=abi, bytecode=bytecode)

    # Prepare constructor args
    constructor_args = [GUARDIAN_OWNER, GUARDIAN_TREASURY]
    print(f"   Constructor args: {constructor_args}")

    # Build transaction
    print("\n[*] Building deployment transaction...")
    try:
        tx = Contract.constructor(*constructor_args).build_transaction({
            'from': acct.address,
            'nonce': nonce,
            'gas': 3000000,
            'gasPrice': gas_price,
            'chainId': 1  # Tron MainNet chain ID
        })
        print("✅ Transaction built")
    except Exception as e:
        print(f"❌ Error building transaction: {e}")
        return False

    # Sign transaction
    print("\n[*] Signing transaction...")
    try:
        signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        print("✅ Transaction signed")
    except Exception as e:
        print(f"❌ Error signing: {e}")
        return False

    # Send transaction
    print("\n[*] Sending transaction to Tron MainNet...")
    try:
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(f"✅ Transaction sent!")
        print(f"   TX Hash: {tx_hash.hex()}")
    except Exception as e:
        print(f"❌ Error sending transaction: {e}")
        return False

    # Wait for receipt
    print("\n[*] Waiting for transaction confirmation (this may take 30-60 seconds)...")
    try:
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)

        if receipt.status == 1:
            print("✅ Transaction confirmed!")
            print(f"\n" + "=" * 60)
            print("DEPLOYMENT SUCCESSFUL!")
            print("=" * 60)
            print(f"Contract Address: {receipt.contractAddress}")
            print(f"Transaction Hash: {receipt.transactionHash.hex()}")
            print(f"Gas Used: {receipt.gasUsed}")
            print(f"\n[Next Steps]")
            print(f"1. Add to MetaMask:")
            print(f"   - Address: {receipt.contractAddress}")
            print(f"   - Symbol: EID")
            print(f"   - Decimals: 18")
            print(f"\n2. Verify on Tronscan:")
            print(f"   https://tronscan.org/#/contract/{receipt.contractAddress}")
            print("=" * 60)
            return True
        else:
            print("❌ Transaction failed!")
            print(receipt)
            return False

    except Exception as e:
        print(f"❌ Error waiting for receipt: {e}")
        print(f"   TX Hash: {tx_hash.hex()}")
        print(f"   Check status manually on Tronscan")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
