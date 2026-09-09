# EuroID (EID) — Tokenomics

**Total supply: 500,000,000 EID — fixed.** The contract contains no mint
function; supply cannot increase. All figures below are verifiable on-chain at
the [token holders page](https://etherscan.io/token/tokenholderchart/0x905cc1ca8b81bc22f395ecbe7513f57eabe1ce0c).

Last verified: 2026-09-09

---

## Distribution

| # | Holder | Address | Amount (EID) | Share | Lock status |
|---|---|---|---:|---:|---|
| 1 | Project owner / deployer | `0x1b1053887700691Fc6AF89fFc5Cab725BF6a00d9` | 248,119,110 | 49.62% | Not locked |
| 2 | Treasury | `0xeb3F08Aa689068079eA94F4cf17AFd0687F2b672` | 150,000,000 | 30.00% | Not locked |
| 3 | Founder / operations | `0xa9edE5abBDd1eF1B9E1616E473CdEBD12B500ad1` | 100,000,000 | 20.00% | Not locked |
| 4 | Early distribution (9 wallets) | various | ~1,875,000 | 0.38% | Circulating |
| 5 | Uniswap V4 liquidity | Uniswap V4 Pool Manager | ~5,086 | 0.001% | Active |
| | **Total** | | **500,000,000** | **100%** | |

Token contract: `0x905Cc1ca8B81BC22F395ECbE7513f57Eabe1ce0c`

---

## Lock and vesting status

**No smart-contract time-lock or vesting is currently in force.**

Wallets 1–3 are ordinary externally owned accounts (EOAs). They are not
vesting contracts, timelocks, or multisigs. Anyone holding the corresponding
private keys can transfer these balances at any time.

We state this plainly because it is what the chain shows, and because a claim
of "locked" that cannot be verified on-chain is worse than no claim at all.

**Planned:** migration of the treasury allocation to an on-chain vesting
contract, and of the project wallet to a Safe multisig. This section will be
updated with the deployed contract address and the vesting schedule once that
is done — and not before.

---

## Liquidity

| Pool | Venue | EID in pool | Status |
|---|---|---:|---|
| EID / ETH | Uniswap V4 | ~5,086 | Nominal |

**EID is not meaningfully tradable at present.** The current position is
primarily for on-chain verifiability. Any attempt at significant trading would
experience severe price impact.

---

## Supply concentration and risk

Three wallets account for 99.6% of total supply. EuroID should be treated as
an early-stage, closely held token. Holders of these wallets can transfer their
balances at any time; there is no technical restriction.
