<div align="center">

# MEOK Labs

### Open compliance MCPs for the EU AI Act / DORA / NIS2 / CRA era

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PyPI Packages](https://img.shields.io/badge/PyPI-234%20packages-orange.svg)](https://pypi.org/user/MEOK_AI_Labs/)
[![EU AI Act](https://img.shields.io/badge/EU%20AI%20Act-Reg%202024%2F1689-blue.svg)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689)
[![DORA](https://img.shields.io/badge/DORA-Reg%202022%2F2554-blue.svg)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554)
[![NIS2](https://img.shields.io/badge/NIS2-Dir%202022%2F2555-blue.svg)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022L2555)
[![CRA](https://img.shields.io/badge/CRA-Reg%202024%2F2847-blue.svg)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R2847)
[![CycloneDX SBOM](https://img.shields.io/badge/SBOM-CycloneDX%201.6-green.svg)](./mcps)
[![SLSA](https://img.shields.io/badge/SLSA-L2%20planned-yellow.svg)](./SECURITY.md)
[![MCP](https://img.shields.io/badge/MCP-server-purple.svg)](https://modelcontextprotocol.io)

[**Catalogue**](https://meok-attestation-api.vercel.app/catalogue) · [**Verify a cert**](https://meok-attestation-api.vercel.app/verify) · [**Apify Actors**](https://apify.com/knowing_yucca) · [**Storefront (councilof.ai)**](https://councilof.ai) · [**Pricing (£29/mo →)**](https://buy.stripe.com/4gM6oJ1BW4gi6kd6as8k838)

> **Solo founder** ([@nicholastempleman](https://github.com/CSOAI-ORG)). London. £0 → revenue in progress.
> **234+ packages on PyPI**. **10 Apify Actors live**. **6 live Vercel sites**. **MIT licensed**.

</div>

---

## What's in this repo

Each subdir under `mcps/` is a self-contained Python MCP server with `pyproject.toml`, `server.py`, `LICENSE`, `README.md`, and a CycloneDX 1.6 `sbom.cdx.json`.

### Flagship 10

| Package | Tier | What it does | PyPI |
|---|---|---|---|
| **meok-omnibus-tracker-mcp** | free | Live status of every EU AI Act Digital Omnibus provision (post 569-45-23 vote, 23 Mar 2026) | [![pypi](https://img.shields.io/pypi/v/meok-omnibus-tracker-mcp)](https://pypi.org/project/meok-omnibus-tracker-mcp/) |
| **meok-watermark-attest-mcp** | pro | Article 50 transparency / watermarking compliance (2 Nov 2026 deadline) | [![pypi](https://img.shields.io/pypi/v/meok-watermark-attest-mcp)](https://pypi.org/project/meok-watermark-attest-mcp/) |
| **meok-cra-annex-iv-classifier-mcp** | pro | EU CRA product classifier (default / Class I / Class II / Annex IV per Reg 2025/2392) | [![pypi](https://img.shields.io/pypi/v/meok-cra-annex-iv-classifier-mcp)](https://pypi.org/project/meok-cra-annex-iv-classifier-mcp/) |
| **meok-nis2-de-register-mcp** | one-off £499 | German Mittelstand BSI portal NIS2 registration packet generator | [![pypi](https://img.shields.io/pypi/v/meok-nis2-de-register-mcp)](https://pypi.org/project/meok-nis2-de-register-mcp/) |
| **meok-mcp-injection-scan-mcp** | pro | 30+ canonical scan rules for the April 2026 Anthropic MCP RCE class | [![pypi](https://img.shields.io/pypi/v/meok-mcp-injection-scan-mcp)](https://pypi.org/project/meok-mcp-injection-scan-mcp/) |
| **meok-dpia-edpb-template-mcp** | one-off £29 | DPIA generator for the EDPB harmonised template (14 Apr 2026) + AI Act Art 26(9) FRIA | [![pypi](https://img.shields.io/pypi/v/meok-dpia-edpb-template-mcp)](https://pypi.org/project/meok-dpia-edpb-template-mcp/) |
| **meok-attestation-verify** | free CLI | Zero-dependency verifier for any MEOK signed cert | [![pypi](https://img.shields.io/pypi/v/meok-attestation-verify)](https://pypi.org/project/meok-attestation-verify/) |
| **care-membrane-mcp** | pro | Care-aligned content validation + 11 neural detection models | [![pypi](https://img.shields.io/pypi/v/care-membrane-mcp)](https://pypi.org/project/care-membrane-mcp/) |
| **healthcare-fhir-mcp** | pro | FHIR R4 audit + EU AI Act Annex III high-risk classifier | [![pypi](https://img.shields.io/pypi/v/healthcare-fhir-mcp)](https://pypi.org/project/healthcare-fhir-mcp/) |
| **slack-enterprise-mcp** | pro | Slack Enterprise Grid governance + DLP audit | [![pypi](https://img.shields.io/pypi/v/slack-enterprise-mcp)](https://pypi.org/project/slack-enterprise-mcp/) |

The full **234-package catalogue**: [meok-attestation-api.vercel.app/catalogue](https://meok-attestation-api.vercel.app/catalogue)

---

## Quick start (60 seconds)

```bash
# Pick the MCP for your regulation
pip install meok-omnibus-tracker-mcp     # EU AI Act Omnibus
pip install meok-watermark-attest-mcp    # EU AI Act Article 50 watermarking
pip install meok-dpia-edpb-template-mcp  # EDPB DPIA harmonised template
pip install meok-mcp-injection-scan-mcp  # Apr 2026 MCP CVE class scanner

# Or run via Apify (no install — Pay-Per-Event):
# https://apify.com/knowing_yucca

# Or via MCPize / Smithery / Claude Marketplace (when listings land)
```

Wire to Claude Code / Cursor / Cline / Windsurf via standard MCP config:

```jsonc
{
  "mcpServers": {
    "meok-omnibus": { "command": "python", "args": ["-m", "server"], "env": {} }
  }
}
```

---

## How signing works

Every Pro / Enterprise call to a MEOK MCP can issue a **HMAC-SHA256 signed attestation** with a public verify URL. Auditors and procurement teams validate without an account:

```bash
pip install meok-attestation-verify
meok-verify https://meok-attestation-api.vercel.app/verify/<cert_id>
```

Signing API source: [meok-attestation-api](https://meok-attestation-api.vercel.app/) (Vercel serverless, Python stdlib only).

Migration to **Ed25519 + Sigstore** is funded by the planned NLnet NGI Zero Commons grant (decision ~Sept 2026).

---

## Pricing

| Tier | Price | What you get |
|---|---|---|
| Free | £0 | All MCPs functional, 5–10 calls/day per package |
| Starter | [£29/mo →](https://buy.stripe.com/4gM6oJ1BW4gi6kd6as8k838) | Unlimited calls + signed attestations |
| Pro | [£79/mo →](https://buy.stripe.com/eVq9AV4O87sudMF42k8k839) | Pro features fleet-wide, 48h support |
| Enterprise | [£1,499/mo →](https://buy.stripe.com/4gM9AV80kaEG0ZT42k8k837) | Custom rule packs, 4h SLA, white-label PDF |
| Assessment | [£5,000 one-off →](https://buy.stripe.com/4gM7sN2G0bIKeQJfL28k833) | 48h bespoke gap analysis |

Sponsor open-source maintenance: [GitHub Sponsors](https://github.com/sponsors/CSOAI-ORG)

---

## Supply-chain transparency

- ✅ MIT-licensed (every package)
- ✅ CycloneDX 1.6 SBOM committed alongside source (`<pkg>/sbom.cdx.json`)
- ✅ SHA-256 source hashes in every SBOM
- ✅ Dependencies pinned with version constraints
- ⏳ Sigstore / cosign keyless OIDC signing — **planned via NLnet grant**
- ⏳ SLSA Level 2 build provenance — **planned**

See [`/SECURITY.md`](./SECURITY.md) for the threat model + the V-01 / V-02 / V-03 / V-06 fix history.

---

## Distribution channels

- 🐍 **PyPI** — 234 packages: [pypi.org/user/MEOK_AI_Labs](https://pypi.org/user/MEOK_AI_Labs/)
- ⚡ **Apify Store** — 10 actors with Pay-Per-Event billing: [apify.com/knowing_yucca](https://apify.com/knowing_yucca) (rename to meok-ai-labs landing soon)
- 🛒 **MCPize** — 85% revenue share marketplace: pending listing
- 🔧 **Smithery** — pending listing
- 📋 **mcp.so** — bulk submission #2171: pending review
- 🔗 **awesome-mcp-servers** — PR pending review

---

## Built by

[**MEOK AI Labs**](https://meok.ai) — solo founder Nicholas Templeman, London. No investors, no exit pressure.

[![GitHub followers](https://img.shields.io/github/followers/CSOAI-ORG?style=social)](https://github.com/CSOAI-ORG)
[![GitHub stars](https://img.shields.io/github/stars/CSOAI-ORG/MEOK-LABS?style=social)](https://github.com/CSOAI-ORG/MEOK-LABS)
