# meok-nis2-de-register-mcp

**BSI-portal-ready NIS2 registration packets for German Mittelstand orgs.**

The NIS2-Umsetzungsgesetz (German NIS2 transposition) took force **6 December 2025**. The BSI registration portal opened **6 January 2026**. ~30,000 in-scope orgs have a **~3-month window** to register — deadline mid-April to early-May 2026. Late registration = up to €2M fines under §38b BSIG, plus personal liability of management body.

By [MEOK AI Labs](https://meok.ai).

## Why this MCP

Most Mittelstand orgs are paying €5K–€20K to consultancies for what is, mechanically, a 30-minute form. This MCP:

1. Validates whether your org is in scope (essential vs important entity, KMU exemption check)
2. Generates the BSI-portal-ready registration packet with all 7 obligation acknowledgements
3. Walks you through Mein Unternehmenskonto submission step-by-step
4. Emits a HMAC-SHA256 signed proof of registration readiness for your audit trail / customer due-diligence requests

## Tools

- `validate_org_profile` — in-scope check + entity type + size class
- `generate_bsi_packet` — full registration JSON (Pro)
- `submit_to_mein_unternehmenskonto` — click-by-click portal walkthrough
- `signed_registration_proof` — Pro: cryptographic proof of completion

## Install

```bash
pip install meok-nis2-de-register-mcp
```

## Tiers

- **Free** — in-scope validation + walkthrough
- **£499 one-off** — full BSI packet generation + signed proof — [buy now](https://buy.stripe.com/4gM7sN2G0bIKeQJfL28k833)
- **Pro £199/mo** — unlimited regenerations + monthly compliance refresh + Slack alerts on BSIG amendments — [subscribe](https://buy.stripe.com/14A4gB3K4eUWgYR56o8k836)

Use code **`MEOKEAT`** at checkout for 25% off the first 3 months.

## Sources

- BSIG (NIS2-Umsetzungsgesetz) — https://www.gesetze-im-internet.de/bsig_2009/
- BSI portal — https://www.bsi.bund.de/DE/Themen/Regulierte-Wirtschaft/NIS-2-Umsetzungsgesetz
- Mein Unternehmenskonto — https://mein-unternehmenskonto.de

## Disclaimer

Automated assistance for regulatory preparation. Does not substitute for qualified German legal counsel or BSI's binding determination. MEOK AI Labs provides no warranty of regulatory correctness.

## Related MEOK MCPs

- [`nis2-compliance-mcp`](https://pypi.org/project/nis2-compliance-mcp/) — full NIS2 audit (all 27 EU Member States)
- [`dora-nis2-crosswalk-mcp`](https://pypi.org/project/dora-nis2-crosswalk-mcp/) — banks in scope for both
- [`ai-incident-reporting-mcp`](https://pypi.org/project/ai-incident-reporting-mcp/) — multi-regime incident clocks

## License

MIT — MEOK AI Labs, 2026.

---

## Distribution channels

- **PyPI**: `pip install meok-nis2-de-register-mcp`
- **Apify Store** (Pay-Per-Event): https://apify.com/knowing_yucca/meok-nis2-de-register
- **GitHub** (source): https://github.com/CSOAI-ORG/MEOK-LABS/tree/main/mcps/meok-nis2-de-register-mcp
- **Sponsor**: https://github.com/sponsors/CSOAI-ORG · [Pro £79/mo →](https://buy.stripe.com/eVq9AV4O87sudMF42k8k839)

