# Blockaid — Verified Project submission

Portal: https://report.blockaid.io/verifiedProject

Field labels may differ slightly; match each answer to the closest field.

---

## Basic details

**Project name**
GUARDIAN ID

**Asset / token name**
EuroID (EID)

**Website**
https://guardian-id.org

**Token information page**
https://eid.guardian-id.org

**Contract address**
0x905Cc1ca8B81BC22F395ECbE7513f57Eabe1ce0c

**Blockchain**
Ethereum Mainnet (chain ID 1)

**Token standard**
ERC-20

**Contract verified**
Yes — Etherscan verified, exact bytecode match; Sourcify match.
https://etherscan.io/address/0x905cc1ca8b81bc22f395ecbe7513f57eabe1ce0c#code

**Source repository**
https://github.com/GuardianID-SK/euroid-token

**Contact email**
info@guardian-id.org

**Social channels**
<!-- FILL IN: Telegram and X/Twitter URLs — they are referenced in the repo,
     put the actual links here and on the website -->

---

## Legal entity

**Organisation**
GUARDIAN ID — non-profit organisation (nezisková organizácia)

**Company ID (IČO)**
55002005

**Registered**
8 December 2022

**Registered address**
Pri kalvárii 614/31, 917 01 Trnava, Slovak Republic

**Jurisdiction**
Slovak Republic (EU member state)

---

## Project description (paste as-is)

EuroID (EID) is an ERC-20 utility token issued by GUARDIAN ID, a non-profit
organisation registered in the Slovak Republic (company ID 55002005, registered
8 December 2022, Trnava). The token supports the organisation's digital identity
initiative.

The contract is a minimal OpenZeppelin ERC-20 with a fixed supply of
500,000,000 EID. It contains no mint function, no burn, no transfer fees, no
pause, no blacklist or freeze capability, and no proxy or upgrade path. The
owner role holds no privileges over balances or transfers — there is no
onlyOwner function in the contract. Source code is verified on Etherscan with
an exact bytecode match.

EuroID is not a stablecoin, is not pegged to the euro, and is not electronic
money or an e-money token under MiCA. It is not an official EU identity
credential and is not affiliated with, endorsed by, or connected to the EU
Digital Identity Wallet (EUDI), the eIDAS framework, or any national eID
scheme. These disclosures are published prominently on guardian-id.org,
eid.guardian-id.org and in the GitHub repository.

---

## Why the current flags are a false positive (paste as-is)

We believe the "impersonator" classification results from the token's name
containing "Euro" and the symbol "EID" resembling the abbreviation "eID". We
have addressed this directly rather than relying on the name alone:

1. Every project surface — website, token page, and repository — carries an
   explicit statement that EuroID is not an EU identity credential, is not part
   of the EU Digital Identity Wallet or eIDAS, and that GUARDIAN ID has no
   affiliation with any EU institution.
2. We make no claim of regulatory approval, certification, conformity
   assessment, or compliance of any kind.
3. We make no claim of a euro peg, backing, or stablecoin status.
4. The issuer is a named, registered legal entity with a public company ID,
   registered address and contact email, disclosed on all project surfaces.
5. The contract address is published in plain text on both guardian-id.org and
   eid.guardian-id.org, establishing a verifiable link between the domain and
   the contract in both directions.
6. The contract has no mint, fee, pause, blacklist or upgrade capability, which
   we believe rules out the honeypot, high-fee and rug-pull patterns the
   classifier screens for.

We additionally disclose openly, in our public tokenomics document, that supply
is currently concentrated, that no time-lock is yet in force, and that
liquidity is nominal — and we explicitly discourage open-market purchase at
this stage. We would rather be assessed on accurate information than on
favourable information.

---

## Before you submit — check each of these

The reviewer will click your links. Every item below must be true at that
moment, or the submission works against you.

- [x] FTP password rotated; credentials removed from any committed script
- [x] Repo description no longer says "European Digital Identity Token"
- [x] README and TOKENOMICS replaced with the corrected versions
- [x] No "how to buy" instructions anywhere while liquidity is nominal
- [ ] "Locked 1-2 years" removed everywhere, or a real vesting contract deployed
- [x] Allocation table sums to 100% and matches Etherscan holders page
- [ ] guardian-id.org links to eid.guardian-id.org and shows the contract address
- [ ] eid.guardian-id.org shows IČO 55002005 and the registered address
- [x] "Security audit" relabelled as internal review, everywhere
- [x] Contract source and tests actually pushed to the public repo
- [ ] Telegram / X links live and pointing to real, populated channels
- [ ] Etherscan token info submitted (logo, website, email, socials)

---

## After submitting

Expect days to weeks, and no guaranteed outcome. Do not submit again while one
is pending — duplicates slow reviews down.

If flags remain after a few weeks, follow up at
https://report.blockaid.io/mistake and reference this verification submission.

Submit separately to the other feeds — Blockaid is not the only one:
- Etherscan token info: https://info.etherscan.com/how-to-update-token-info/
- GoPlus Security, Token Sniffer
- CoinGecko / CoinMarketCap listing applications
