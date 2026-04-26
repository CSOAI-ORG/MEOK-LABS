# MEOK Labs — open compliance MCPs

The canonical home for [MEOK AI Labs](https://meok.ai)' open-source MCP packages — cryptographically signed compliance attestations for the EU AI Act, DORA, NIS2, CRA, GDPR + UK AI Bill era.

> **Solo founder ([@nicholastempleman](https://github.com/CSOAI-ORG)). London. £0 → revenue in progress. 234+ packages on PyPI. MIT-licensed.**

---

## What's in this repo

| Package | Tier | What it does | PyPI |
|---|---|---|---|
| **meok-omnibus-tracker-mcp** | free | Live status of every EU AI Act Digital Omnibus provision (post 23 March 2026 vote 569-45-23) | [↗](https://pypi.org/project/meok-omnibus-tracker-mcp/) |
| **meok-watermark-attest-mcp** | pro | Article 50 transparency / watermarking compliance (2 Nov 2026 deadline) | [↗](https://pypi.org/project/meok-watermark-attest-mcp/) |
| **meok-cra-annex-iv-classifier-mcp** | pro | EU CRA product classifier (default / Class I / Class II / Annex IV per Reg 2025/2392) | [↗](https://pypi.org/project/meok-cra-annex-iv-classifier-mcp/) |
| **meok-nis2-de-register-mcp** | one-off £499 | German Mittelstand BSI portal NIS2 registration packet generator | [↗](https://pypi.org/project/meok-nis2-de-register-mcp/) |
| **meok-mcp-injection-scan-mcp** | pro | 30+ canonical scan rules covering the April 2026 Anthropic MCP RCE class | [↗](https://pypi.org/project/meok-mcp-injection-scan-mcp/) |
| **meok-dpia-edpb-template-mcp** | one-off £29 | DPIA generator for the EDPB harmonised template (14 Apr 2026) + AI Act Art 26(9) FRIA | [↗](https://pypi.org/project/meok-dpia-edpb-template-mcp/) |
| **meok-attestation-verify** | free CLI | Zero-dependency verifier for any MEOK signed cert | [↗](https://pypi.org/project/meok-attestation-verify/) |
| **care-membrane-mcp** | pro | Care-aligned content validation + 11 neural detection models | [↗](https://pypi.org/project/care-membrane-mcp/) |
| **healthcare-fhir-mcp** | pro | FHIR R4 audit + EU AI Act Annex III high-risk classifier | [↗](https://pypi.org/project/healthcare-fhir-mcp/) |
| **slack-enterprise-mcp** | pro | Slack Enterprise Grid governance + DLP audit | [↗](https://pypi.org/project/slack-enterprise-mcp/) |

The full 234-package catalogue (auto-generated): https://meok-attestation-api.vercel.app/catalogue

---

## How signing works

Every Pro / Enterprise call to a MEOK MCP can issue a **HMAC-SHA256 signed attestation** with a public verify URL. Auditors and procurement teams validate without needing an account.

```bash
pip install meok-attestation-verify
meok-verify https://meok-attestation-api.vercel.app/verify/<cert_id>
```

Source: [`meok-attestation-api/api/index.py`](https://github.com/CSOAI-ORG/MEOK-LABS/blob/main/api/index.py) (Vercel serverless, Python stdlib only).

Migration to **Ed25519 + Sigstore** is funded by the planned NLnet NGI Zero Commons grant (€30K, decision Sept 2026).

---

## Pricing

| Tier | Price | What you get |
|---|---|---|
| Free | £0 | All MCPs functional, 5–10 calls/day per package |
| Starter | [£29 / mo](https://buy.stripe.com/4gM6oJ1BW4gi6kd6as8k838) | Unlimited calls + signed attestations |
| Pro | [£79 / mo](https://buy.stripe.com/eVq9AV4O87sudMF42k8k839) | Pro features across the fleet, 48h support |
| Enterprise | [£1,499 / mo](https://buy.stripe.com/4gM9AV80kaEG0ZT42k8k837) | Custom rule packs, 4h SLA, white-label PDF |
| Assessment | [£5,000 one-off](https://buy.stripe.com/4gM7sN2G0bIKeQJfL28k833) | 48h bespoke gap analysis |

Sponsor open-source maintenance: [GitHub Sponsors](https://github.com/sponsors/CSOAI-ORG) (when live)

---

## Supply-chain transparency

- ✅ MIT-licensed (every package)
- ✅ CycloneDX 1.6 SBOM committed alongside source (`<pkg>/sbom.cdx.json`)
- ✅ Dependencies pinned with version constraints
- ⏳ Sigstore / cosign keyless OIDC signing — **planned via NLnet grant**
- ⏳ SLSA Level 2 build provenance — **planned**

See [`/SECURITY.md`](./SECURITY.md) for the threat model + the V-01 / V-02 / V-03 / V-06 fix history.

---

## License

All packages are MIT. See `<pkg>/LICENSE`. The signing-API source code is also MIT.

---

## Built by

[**MEOK AI Labs**](https://meok.ai) · [@CSOAI-ORG](https://github.com/CSOAI-ORG) · Solo founder, London, no investors, no exit pressure.

Find us:
- Storefront: [councilof.ai](https://councilof.ai)
- Catalogue: [meok-attestation-api.vercel.app/catalogue](https://meok-attestation-api.vercel.app/catalogue)
- Verifier: [meok-verify.vercel.app](https://meok-verify.vercel.app)
- 25 .ai/.org domains, 6 live Vercel sites, 10 Apify Actors, 234 PyPI packages
