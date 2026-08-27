# EuroID — Solidity/Foundry Token

**EuroID** is a fixed-supply ERC-20 token deployed on **Tron MainNet** for GUARDIAN ID.

## Token Properties

```
Name:              EuroID
Symbol:            EID
Standard:          ERC-20 (TRC-20 on Tron)
Decimals:          18
Total Supply:      500,000,000 EID (immutable)
Owner:             GUARDIAN ID (multisig, eventually)
Treasury:          GUARDIAN ID organizational treasury
```

## Architecture

### Core Contract: EuroID.sol

- **Standard ERC-20** with OpenZeppelin `ERC20.sol`
- **Transparent Ownership** via OpenZeppelin `Ownable2Step`
- **Fixed Supply** — exactly 500,000,000 EID created at deployment
- **No Minting** after deployment — total supply never changes
- **No Transfer Taxes** — all transfers are standard ERC-20
- **No Rebasing, Blacklisting, or Hidden Restrictions**

### Constructor Parameters

```solidity
address guardianOwner    // Owner of the smart contract (for governance)
address treasury         // Receives all 500M EID at deployment
```

### Key Features

1. **Immutable Supply**
   - Total supply locked at deployment time
   - No public or internal mint function
   - No burn function (supply cannot be reduced)
   - No rebase or reflection mechanics

2. **Owner Powers** (Limited)
   - Cannot mint or burn tokens
   - Cannot seize tokens from users
   - Cannot modify balances arbitrarily
   - Can only be transferred via safe two-step process
   - **Purpose**: organizational attribution and future narrowly-scoped admin functions

3. **Standard ERC-20 Features**
   - `transfer(to, amount)` — send tokens
   - `approve(spender, amount)` — allow spending
   - `transferFrom(from, to, amount)` — spend approved tokens
   - `balanceOf(account)` — check balance
   - `allowance(owner, spender)` — check approval

## Build and Test

### Compile

```bash
forge build
```

### Run Tests

```bash
forge test -vv
```

**Test Results** (as of deployment):
- 17 unit tests: ✅ ALL PASSED
- Coverage: name, symbol, decimals, supply, owner, treasury, transfers, approvals, no minting, no seizure, supply immutability, ownership transfer

## Deployment

### Tron MainNet Deployment

⚠️ **CRITICAL SECURITY WARNING**

Never commit private keys to version control. Use environment variables or secure key management.

#### Step 1: Export Private Key from MetaMask

1. Open MetaMask
2. Click your account → Settings → Security & Privacy
3. Export Private Key (confirm your password)
4. Store securely (never share, never commit to git)

#### Step 2: Prepare Environment

```bash
export GUARDIAN_OWNER=0x1b1053887700691Fc6AF89fFc5Cab725BF6a00d9
export GUARDIAN_TREASURY=0x1b1053887700691Fc6AF89fFc5Cab725BF6a00d9
export PRIVATE_KEY=0x<your_private_key_here>
```

#### Step 3: Deploy to Tron MainNet

```bash
forge script script/DeployEuroID.s.sol:DeployEuroID \
  --rpc-url https://rpc.trongrid.io \
  --private-key $PRIVATE_KEY \
  --broadcast
```

#### Step 4: Add to MetaMask

1. Open MetaMask
2. Click "Import Tokens"
3. Enter the contract address from Step 3 output
4. Decimals: 18
5. Confirm

## Security

- ✅ No mint after deployment
- ✅ No token seizure capability
- ✅ No transfer taxes or hidden mechanics
- ✅ Ownership via safe two-step transfer
- ✅ OpenZeppelin audited libraries
- ✅ No upgradeable proxy

## Owner Limitations

Owner **CANNOT**:
- Create new EID tokens
- Destroy tokens
- Seize user balances
- Freeze addresses
- Impose taxes
- Change total supply

## License

MIT
