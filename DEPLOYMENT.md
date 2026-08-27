# EuroID Deployment Instructions (Tron MainNet)

## ⚠️ SECURITY FIRST

- **Never** share your private key
- **Never** commit private key to git
- **Never** copy-paste private key into messages
- Use environment variables only

## Prerequisites

1. ✅ Foundry installed (`forge --version` should work)
2. ✅ 85 TRX in your MetaMask wallet (for gas fees)
3. ✅ Your MetaMask seed phrase or private key safely stored

## Step-by-Step Deployment

### Step 1: Export Private Key from MetaMask

**In MetaMask:**
1. Click your account icon (top right)
2. Account details → Show private key
3. Enter your password
4. **Copy the private key** (starts with `0x`)
5. Paste it **ONLY** into your terminal (not email, not chat)

### Step 2: Open Terminal/PowerShell

Navigate to the euroid project:

```powershell
cd F:\euroid
```

Verify Foundry works:

```powershell
forge --version
```

Should show: `forge 1.8.0 ...` or similar.

### Step 3: Set Environment Variable

**In PowerShell**, set your private key (only for this session):

```powershell
$env:PRIVATE_KEY = "0x<paste_your_private_key_here>"
```

**IMPORTANT**: Replace `<paste_your_private_key_here>` with your actual private key from MetaMask.

Example (with fake key):
```powershell
$env:PRIVATE_KEY = "0xac0974bec39a17e36ba4a6b4d238ff944bacb476c6b8d6c1f8d0c12c0b15cb5d"
```

### Step 4: Verify Environment Variable

Check that the variable is set:

```powershell
echo $env:PRIVATE_KEY
```

Should print your private key. If blank, go back to Step 3.

### Step 5: Deploy to Tron MainNet

Run this command (all one line):

```powershell
forge script script/DeployEuroID.s.sol:DeployEuroID `
  --rpc-url https://rpc.trongrid.io `
  --private-key $env:PRIVATE_KEY `
  --broadcast
```

**This will:**
1. Compile the contract
2. Connect to Tron MainNet
3. Deploy EuroID contract
4. Send 500,000,000 EID to your address
5. Print the contract address

### Step 6: Wait for Confirmation

**Expected output:**
```
...
✅ Deployment successful!

==== EuroID Deployment ====
Token Address:     Txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Owner:             Txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Treasury:          Txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Total Supply:      500000000000000000000000000 EID
Treasury Balance:  500000000000000000000000000 EID
```

**Save the "Token Address"** — you'll need it for MetaMask.

### Step 7: Add to MetaMask

1. Open MetaMask
2. Click "**Import Tokens**" (or go to Assets tab)
3. Paste the contract address from Step 6
4. **Symbol should auto-fill as "EID"**
5. **Decimals should be 18**
6. Click "Add Custom Token"
7. Click "Import Tokens"

**You should now see 500,000,000 EID in your MetaMask! ✅**

### Step 8: Test Transfer (Optional)

Send a small amount to a friend to verify it works:

1. In MetaMask, click "Send"
2. Paste their Tron address (starts with `T`)
3. Enter amount (e.g., 1000 EID)
4. Click "Next" → "Confirm"

Done! The token is live on Tron MainNet. 🚀

---

## Troubleshooting

### Error: "Private key not found"

```
Error: Private key not found or invalid
```

**Fix**: Make sure you set the environment variable in Step 3:

```powershell
$env:PRIVATE_KEY = "0x..."
```

### Error: "Insufficient gas"

```
Error: insufficient gas
```

**Fix**: You need ~1-3 TRX for gas fees. Check your MetaMask balance.

### Error: "Invalid RPC URL"

```
Error: Bad response from RPC
```

**Fix**: Tron RPC might be down. Try:
```powershell
curl https://rpc.trongrid.io
```

If it doesn't respond, wait a few minutes and retry.

### Contract deployed but doesn't appear in MetaMask

**Fix**: 
1. Make sure you imported the contract address correctly (from Step 6 output)
2. Make sure MetaMask is set to **Tron MainNet** (not Ethereum)
3. Try removing the token and re-importing it

### "Address is not a valid Tron address"

**Fix**: Your owner address in the script must be a Tron address (starts with `T`). If it's an Ethereum address, convert it:
- Use https://tronweb.org/address/convert (paste Ethereum address to get Tron address)

---

## After Deployment

### Verify on Tronscan

Go to https://tronscan.org and search for your contract address.

You should see:
- ✅ Token name: EuroID
- ✅ Symbol: EID
- ✅ Total supply: 500,000,000
- ✅ Your address as owner

### Next Steps

1. **Share with others**: You can now send EID to other Tron addresses
2. **List on DEX**: Contact SushiSwap or Uniswap to add EID liquidity
3. **Bridge to Ethereum** (later): Requires additional infrastructure

---

## Private Key Safety Reminder

After deployment:
1. **Clear the environment variable**: Close PowerShell or run `$env:PRIVATE_KEY = ""`
2. **Never re-use this private key** for testing
3. **Keep your seed phrase safe** (backup, not online)

---

Need help? Contact GUARDIAN ID support.
