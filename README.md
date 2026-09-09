# EuroID (EID) — Independent Digital Identity Token

**Built in Europe by GUARDIAN ID, a registered Slovak non-profit organisation.**

> **Not affiliated with the European Union.** EuroID is not an official EU
> identity credential and is not connected to the EU Digital Identity Wallet
> (EUDI), the eIDAS framework, or any national eID scheme. See
> [Disclosures](#disclosures) below.

---

## Contract

| | |
|---|---|
| **Contract address** | `0x905Cc1ca8B81BC22F395ECbE7513f57Eabe1ce0c` |
| **Network** | Ethereum Mainnet (chain ID 1) |
| **Name / Symbol** | EuroID / EID |
| **Decimals** | 18 |
| **Total supply** | 500,000,000 EID (fixed) |
| **Standard** | ERC-20 (OpenZeppelin) |

**Verify it yourself:**
[Etherscan token](https://etherscan.io/token/0x905cc1ca8b81bc22f395ecbe7513f57eabe1ce0c) ·
[Verified source code](https://etherscan.io/address/0x905cc1ca8b81bc22f395ecbe7513f57eabe1ce0c#code)

The address above is the **only** official EuroID contract. Any other token
using the name "EuroID" or the symbol "EID" is unrelated to GUARDIAN ID.

---

## Contract properties

The contract is deliberately minimal. What it **does not** have matters more
than what it does:

| Property | Status |
|---|---|
| Mint function after deployment | ❌ None — supply is immutable |
| Burn function | ❌ None |
| Transfer tax / fee on trade | ❌ None |
| Blacklist / freeze / seize | ❌ None |
| Pause function | ❌ None |
| Rebasing | ❌ None |
| Proxy / upgradeable | ❌ None — contract is immutable |
| Ownership | `Ownable2Step` (two-step transfer) |

The `owner` role has **no privileges over token balances or transfers**. There
is no `onlyOwner` function in the contract. Ownership exists only for
administrative identification.

---

## Issuer

**GUARDIAN ID**, non-profit organisation
Company ID (IČO): **55002005**
Registered: 8 December 2022
Pri kalvárii 614/31, 917 01 Trnava, Slovak Republic

Website: [guardian-id.org](https://guardian-id.org) ·
Token page: [eid.guardian-id.org](https://eid.guardian-id.org) ·
Contact: info@guardian-id.org

---

## Supply distribution

See [TOKENOMICS.md](TOKENOMICS.md) for the full breakdown with wallet
addresses. Summary as currently held on-chain:

| Holder | Amount | Share |
|---|---:|---:|
| Project owner / deployer | 248,119,110 | 49.62% |
| Treasury | 150,000,000 | 30.00% |
| Founder / operations | 100,000,000 | 20.00% |
| Early distribution (9 wallets) | ~1,875,000 | 0.38% |
| Uniswap V4 liquidity | ~5,086 | 0.001% |

**Supply is currently highly concentrated and is not time-locked.** We consider
this a limitation, not a feature; see [Known limitations](#known-limitations).

---

## Known limitations

We publish these openly rather than let anyone discover them on their own.

1. **Supply concentration.** Three wallets hold 99.6% of supply. Until this is
   addressed, EID should be treated as an early-stage, closely held token.
2. **No time-lock or vesting is in place.** Project, treasury and operations
   wallets are ordinary externally owned accounts. No smart-contract lock
   currently restricts them.
3. **Liquidity is minimal.** The Uniswap V4 position is nominal. EID is **not
   meaningfully tradable** at present and we do not encourage anyone to buy it
   on the open market until this changes.
4. **No third-party security audit.** An internal review has been performed
   (see `SECURITY_AUDIT_REPORT.md`). It is not an independent audit and should
   not be read as one.
5. **No market price.** EID has no established market value.

---

## Disclosures

- EuroID is **not a stablecoin**. It is not pegged to the euro or any other
  currency. Its value is neither backed nor guaranteed.
- EuroID is **not electronic money** and not an e-money token under the MiCA
  regulation. It is not issued by a regulated financial institution.
- EuroID is **not an official EU identity credential**. GUARDIAN ID is not
  affiliated with, endorsed by, accredited by, or acting on behalf of any
  institution of the European Union. EuroID is not part of the EU Digital
  Identity Wallet (EUDI), is not eIDAS-conformant, and holds no regulatory
  certification of any kind.
- Nothing in this repository is investment advice, an offer, or a solicitation
  to buy any asset.

---

## Licence

See [LICENSE](LICENSE).
