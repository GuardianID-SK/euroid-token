#!/usr/bin/env python3
"""
SushiSwap Pool Creation Agent for EuroID
Automatically creates EID/ETH liquidity pool
"""

import os
import json
from web3 import Web3
import time

# Configuration
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
if not PRIVATE_KEY:
    print("❌ Error: PRIVATE_KEY environment variable not set")
    sys.exit(1)
RPC_URL = "https://eth.llamarpc.com"
SUSHISWAP_ROUTER = "0xd9e1cE17f2641f24aE57b168855b3e3d4969e498"  # SushiSwap V2 Router

# Token addresses
EID_TOKEN = "0x905Cc1ca8B81BC22F395ECbE7513f57Eabe1ce0c"
WETH_TOKEN = "0xC02aaA39b223FE8D0A0e8e4F27ead9083c756Cc2"

# Amounts
ETH_AMOUNT = Web3.to_wei(0.05, "ether")  # 0.05 ETH
EID_AMOUNT = Web3.to_wei(125000, "ether")  # 125k EID (approximately 125k * 1 EUR = 1 EUR per token ratio)

# SushiSwap Router ABI (addLiquidity function)
ROUTER_ABI = json.loads('''[
    {
        "inputs": [
            {"name": "tokenA", "type": "address"},
            {"name": "tokenB", "type": "address"},
            {"name": "amountADesired", "type": "uint256"},
            {"name": "amountBDesired", "type": "uint256"},
            {"name": "amountAMin", "type": "uint256"},
            {"name": "amountBMin", "type": "uint256"},
            {"name": "to", "type": "address"},
            {"name": "deadline", "type": "uint256"}
        ],
        "name": "addLiquidity",
        "outputs": [
            {"name": "amountA", "type": "uint256"},
            {"name": "amountB", "type": "uint256"},
            {"name": "liquidity", "type": "uint256"}
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]''')

# ERC20 ABI for approve function
ERC20_ABI = json.loads('''[
    {
        "inputs": [{"name": "spender", "type": "address"}, {"name": "amount", "type": "uint256"}],
        "name": "approve",
        "outputs": [{"name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]''')

def create_sushiswap_pool():
    """Create liquidity pool on SushiSwap for EID/ETH"""

    print("[*] SushiSwap Pool Creation Agent")
    print("=" * 60)

    # Connect to Web3
    print("[*] Connecting to Ethereum MainNet...")
    w3 = Web3(Web3.HTTPProvider(RPC_URL))

    if not w3.is_connected():
        print("[ERROR] Failed to connect to Ethereum RPC")
        return False

    print("[OK] Connected to Ethereum MainNet")

    # Get account
    account = w3.eth.account.from_key(PRIVATE_KEY)
    print(f"[*] Account: {account.address}")

    # Get balances
    print("\n[*] Checking balances...")
    eth_balance = w3.eth.get_balance(account.address)
    print(f"    ETH Balance: {w3.from_wei(eth_balance, 'ether'):.4f} ETH")

    # Check EID balance
    eid_contract = w3.eth.contract(address=Web3.to_checksum_address(EID_TOKEN), abi=ERC20_ABI)
    try:
        eid_balance = eid_contract.functions.balanceOf(account.address).call()
        print(f"    EID Balance: {w3.from_wei(eid_balance, 'ether'):.2f} EID")
    except:
        print("    EID Balance: Unable to fetch")

    # Check if balances are sufficient
    if eth_balance < ETH_AMOUNT:
        print(f"[ERROR] Insufficient ETH! Need {w3.from_wei(ETH_AMOUNT, 'ether')} but have {w3.from_wei(eth_balance, 'ether')}")
        return False

    print(f"[OK] Sufficient balances!")

    # Step 1: Approve EID token for SushiSwap Router
    print("\n[*] Step 1: Approving EID token for SushiSwap Router...")

    eid_approve_tx = eid_contract.functions.approve(
        Web3.to_checksum_address(SUSHISWAP_ROUTER),
        EID_AMOUNT
    ).build_transaction({
        'from': account.address,
        'nonce': w3.eth.get_transaction_count(account.address),
        'gas': 100000,
        'gasPrice': w3.eth.gas_price,
    })

    print(f"    Gas estimate: {eid_approve_tx['gas']}")
    print(f"    Gas price: {w3.from_wei(eid_approve_tx['gasPrice'], 'gwei')} Gwei")

    signed_approve = w3.eth.account.sign_transaction(eid_approve_tx, PRIVATE_KEY)
    approve_tx_hash = w3.eth.send_raw_transaction(signed_approve.rawTransaction)

    print(f"[OK] Approval TX sent: {approve_tx_hash.hex()}")
    print("    Waiting for confirmation...")

    try:
        receipt = w3.eth.wait_for_transaction_receipt(approve_tx_hash, timeout=120)
        if receipt['status'] == 1:
            print("[OK] EID approval confirmed!")
        else:
            print("[ERROR] Approval transaction failed!")
            return False
    except:
        print("[WARN] Approval confirmation timeout, continuing...")

    # Step 2: Add Liquidity
    print("\n[*] Step 2: Adding liquidity to SushiSwap...")

    router_contract = w3.eth.contract(
        address=Web3.to_checksum_address(SUSHISWAP_ROUTER),
        abi=ROUTER_ABI
    )

    deadline = int(time.time()) + 3600  # 1 hour from now

    liquidity_tx = router_contract.functions.addLiquidity(
        Web3.to_checksum_address(EID_TOKEN),
        Web3.to_checksum_address(WETH_TOKEN),
        EID_AMOUNT,
        ETH_AMOUNT,
        int(EID_AMOUNT * 0.95),  # 5% slippage
        int(ETH_AMOUNT * 0.95),  # 5% slippage
        account.address,
        deadline
    ).build_transaction({
        'from': account.address,
        'nonce': w3.eth.get_transaction_count(account.address),
        'gas': 300000,
        'gasPrice': w3.eth.gas_price,
    })

    print(f"    Liquidity TX:")
    print(f"      EID Amount: {w3.from_wei(EID_AMOUNT, 'ether'):.2f}")
    print(f"      ETH Amount: {w3.from_wei(ETH_AMOUNT, 'ether'):.4f}")
    print(f"      Gas: {liquidity_tx['gas']}")

    signed_liquidity = w3.eth.account.sign_transaction(liquidity_tx, PRIVATE_KEY)
    liquidity_tx_hash = w3.eth.send_raw_transaction(signed_liquidity.rawTransaction)

    print(f"\n[OK] Liquidity TX sent: {liquidity_tx_hash.hex()}")
    print("    Waiting for confirmation...")

    try:
        receipt = w3.eth.wait_for_transaction_receipt(liquidity_tx_hash, timeout=120)

        if receipt['status'] == 1:
            print("\n" + "=" * 60)
            print("[SUCCESS] SushiSwap Pool Created!")
            print("=" * 60)
            print(f"TX Hash: {liquidity_tx_hash.hex()}")
            print(f"Gas Used: {receipt['gasUsed']}")
            print(f"\nPool Link:")
            print(f"  https://www.sushi.com/swap?chainId=1&tokenIn={WETH_TOKEN}&tokenOut={EID_TOKEN}")
            return True
        else:
            print("[ERROR] Liquidity transaction failed!")
            return False

    except Exception as e:
        print(f"[ERROR] {e}")
        return False

if __name__ == "__main__":
    print("\n")
    success = create_sushiswap_pool()
    print("\n")
