# Care Membrane Safety MCP Server

> **By [MEOK AI Labs](https://meok.ai)** — Sovereign AI tools for everyone.

AI safety evaluation toolkit for LLM applications. Score text for care-centered alignment, detect threats and jailbreak attempts, analyze relationship health, predict burnout risk, and certify AI responses against the 16-probe Care Membrane framework.

[![MCPize](https://img.shields.io/badge/MCPize-Listed-blue)](https://mcpize.com/mcp/care-membrane)
[![MIT License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![MEOK AI Labs](https://img.shields.io/badge/MEOK_AI_Labs-255+_servers-purple)](https://meok.ai)

## Tools

| Tool | Description |
|------|-------------|
| `validate_care` | Score text against care-centered alignment principles (0-100) |
| `detect_threats` | Detect jailbreak attempts, prompt injection, and PII extraction |
| `analyze_care_patterns` | Detect burnout risk and relationship health imbalances |
| `predict_relationship_evolution` | Predict relationship evolution over the next 30 days |
| `evaluate_care_membrane` | Evaluate responses against the 16-probe Care Membrane framework |
| `get_care_probes` | List all 16 Care Membrane probes with categories |

## Quick Start

```bash
pip install mcp
git clone https://github.com/MEOK-AI-Labs/care-membrane-mcp.git
cd care-membrane-mcp
python server.py
```

## Zero-Friction Tools

### `quick_check`
Paste any AI response, get instant care score + threat detection. **No API key needed.**

```
quick_check(text="I understand your concern and I'm here to help")
```

### `what_is_care_membrane`
Explains the 16-probe Care Membrane framework. **No parameters needed.**

```
what_is_care_membrane()
```

## Claude Desktop Config

```json
{
  "mcpServers": {
    "care-membrane": {
      "command": "python",
      "args": ["server.py"],
      "cwd": "/path/to/care-membrane-mcp"
    }
  }
}
```

## Pricing

| Plan | Price | Requests |
|------|-------|----------|
| Free | $0/mo | 50 requests/day |
| Pro | $9/mo | Unlimited + priority |
| Enterprise | Contact us | Custom + SLA + on-prem |

[Get on MCPize](https://mcpize.com/mcp/care-membrane) | [Stripe](https://buy.stripe.com/aFadRb5Sc7sucIBaqI8k803)

## Part of MEOK AI Labs

This is one of 255+ MCP servers by MEOK AI Labs. Browse all at [meok.ai](https://meok.ai) or [GitHub](https://github.com/MEOK-AI-Labs).

---

## 🏢 Enterprise & Pro Licensing

| Plan | Price | Link |
|------|-------|------|
| **Care Membrane Safety MCP** | £9/mo | [Subscribe](https://buy.stripe.com/aFadRb5Sc7sucIBaqI8k803) |
| **Compliance Trinity** | £79/mo | [Subscribe](https://buy.stripe.com/eVq5kF2G0aEG3812Yg8k82i) |
| **Full Suite** (9 MCPs) | £999/mo | [Subscribe](https://buy.stripe.com/6oU14p0xS4giaAtbuM8k82q) |

> Built on care ethics by [CSOAI](https://csoai.org) — the Council for Safety of AI.

---
**MEOK AI Labs** | [meok.ai](https://meok.ai) | [csoai.org](https://csoai.org) | nicholas@meok.ai

## Related MEOK MCPs (ecosystem)

- [`eu-ai-act-compliance-mcp`](https://pypi.org/project/eu-ai-act-compliance-mcp/) — EU AI Act
- [`dora-compliance-mcp`](https://pypi.org/project/dora-compliance-mcp/) — EU DORA
- [`nis2-compliance-mcp`](https://pypi.org/project/nis2-compliance-mcp/) — EU NIS2
- [`cra-compliance-mcp`](https://pypi.org/project/cra-compliance-mcp/) — EU CRA
- [`csrd-compliance-mcp`](https://pypi.org/project/csrd-compliance-mcp/) — EU CSRD
- [`gdpr-compliance-mcp`](https://pypi.org/project/gdpr-compliance-mcp/) — GDPR
- [`hipaa-compliance-mcp`](https://pypi.org/project/hipaa-compliance-mcp/) — HIPAA
- [`soc2-compliance-mcp`](https://pypi.org/project/soc2-compliance-mcp/) — SOC 2
- [`iso-42001-compliance-mcp`](https://pypi.org/project/iso-42001-compliance-mcp/) — ISO/IEC 42001 AIMS
- [`nist-rmf-ai-mcp`](https://pypi.org/project/nist-rmf-ai-mcp/) — NIST AI RMF
- [`uk-ai-bill-compliance-mcp`](https://pypi.org/project/uk-ai-bill-compliance-mcp/) — UK AI Regulation
- [`ai-bom-mcp`](https://pypi.org/project/ai-bom-mcp/) — AI Bill of Materials (CycloneDX ML-BOM + SPDX 3.0)
- [`dora-nis2-crosswalk-mcp`](https://pypi.org/project/dora-nis2-crosswalk-mcp/) — DORA × NIS2 dual compliance
- [`ai-incident-reporting-mcp`](https://pypi.org/project/ai-incident-reporting-mcp/) — one incident, all regulatory clocks
- [`care-membrane-mcp`](https://pypi.org/project/care-membrane-mcp/) — pre-inference ethics gate
- [`gods-eye-geospatial-mcp`](https://pypi.org/project/gods-eye-geospatial-mcp/) — civilian open-source geospatial
- [`meok-attestation-verify`](https://pypi.org/project/meok-attestation-verify/) — zero-dep verifier for MEOK signed certs

## Signed attestations (Pro tier)

Every Pro-tier audit emits a **HMAC-SHA256 signed attestation** with a public verify URL — auditors + boards + procurement teams validate it without MEOK backend access.

Get one: [Pro £199/mo](https://buy.stripe.com/14A4gB3K4eUWgYR56o8k836) · [Enterprise £1,499/mo](https://buy.stripe.com/4gM9AV80kaEG0ZT42k8k837) · [48h assessment £5,000](https://buy.stripe.com/4gM7sN2G0bIKeQJfL28k833)

Verify: `pip install meok-attestation-verify`

---

## Distribution channels

- **PyPI**: `pip install care-membrane-mcp`
- **GitHub** (source): https://github.com/CSOAI-ORG/MEOK-LABS/tree/main/mcps/care-membrane-mcp
- **Sponsor**: https://github.com/sponsors/CSOAI-ORG · [Pro £79/mo →](https://buy.stripe.com/eVq9AV4O87sudMF42k8k839)
- **Verifier**: `pip install meok-attestation-verify` then `meok-verify <cert_url>`

