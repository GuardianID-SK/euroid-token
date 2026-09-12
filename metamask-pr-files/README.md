# EuroID (EID) Token — MetaMask Official Registration

## 📋 PR Instructions

### Step 1: Fork MetaMask Contract Metadata Repo
```
https://github.com/MetaMask/contract-metadata
```

### Step 2: Create Directory Structure
```
images/0x905cc1ca8b81bc22f395ecbe7513f57eabe1ce0c/
├── logo.svg        (EuroID_Logo.svg — rename this)
└── info.json       (Already prepared)
```

### Step 3: Upload Files to Your Fork
```bash
# In your forked repo:
mkdir -p images/0x905cc1ca8b81bc22f395ecbe7513f57eabe1ce0c

# Copy files:
cp EuroID_Logo.svg images/0x905cc1ca8b81bc22f395ecbe7513f57eabe1ce0c/logo.svg
cp info.json images/0x905cc1ca8b81bc22f395ecbe7513f57eabe1ce0c/info.json
```

### Step 4: Commit & Push
```bash
git add images/0x905cc1ca8b81bc22f395ecbe7513f57eabe1ce0c/
git commit -m "Add EuroID (EID) token registration

- Token: EuroID (EID)
- Contract: 0x905cc1ca8b81bc22f395ecbe7513f57eabe1ce0c
- Network: Ethereum MainNet
- Website: https://eid.guardian-id.org"

git push origin main
```

### Step 5: Create Pull Request
- Go to: https://github.com/MetaMask/contract-metadata/pulls
- Create new PR from your fork to main branch
- Use commit message as PR title
- Add description:

```
## EuroID Token Registration

**Token Details:**
- Name: EuroID
- Symbol: EID
- Contract: 0x905cc1ca8b81bc22f395ecbe7513f57eabe1ce0c
- Decimals: 18
- Blockchain: Ethereum MainNet
- Supply: 500,000,000 EID

**Description:**
EuroID (EID) is a European digital identity token enabling decentralized verification, cross-border payments, and frictionless access to European financial services.

**Website:** https://eid.guardian-id.org
**GitHub:** https://github.com/GuardianID-SK/euroid-token

**Verification:**
- Contract verified on Etherscan
- Logo provided in SVG format
- Metadata complete and accurate
```

### Step 6: Wait for Approval
- MetaMask team reviews (1-7 days)
- If approved ✅ → Token appears in MetaMask without warnings
- If changes needed → They'll request modifications

---

## 📁 Files Included

- **info.json** — Token metadata (ready to use)
- **EuroID_Logo.svg** — Token logo (512×512px, SVG format)
- **README_PR.md** — This file

## ⏱️ Timeline

- **Submission:** Immediate
- **Review:** 1-7 days (usually 2-3 days)
- **Approval:** After accepted, token auto-imports in MetaMask

## ✅ After Approval

Once MetaMask approves:
1. Token automatically appears in MetaMask when users add network/contract
2. No manual import warnings
3. Logo displays correctly
4. User experience improved 🎉

---

**Created:** 2026-09-12
**Token:** EuroID (EID)
**Status:** Ready for MetaMask PR submission
