# meok-dpia-edpb-template-mcp

**Generate a GDPR Art 35 + EU AI Act Art 26(9) DPIA from a 6-question wizard, in the EDPB harmonised template (adopted 14 April 2026).**

```
pip install meok-dpia-edpb-template-mcp
```

## Why this exists

EDPB published the **first harmonised DPIA template on 14 April 2026**, with an explicit AI Act Article 26(9) FRIA section. Every EU DPO is rewriting their templates this month. Doing 50+ DPIAs manually = 200+ hours of paperwork. This MCP collapses that to a wizard call per use case + a signed PDF/JSON pack per DPIA.

## What it does

- Fills all 9 EDPB sections from a 6-input wizard
- Auto-detects 10 default risk patterns (biometric, credit, employment, health, law-enforcement, social-scoring, child, marketing, …)
- Classifies the use case under the EU AI Act risk tiers (Prohibited / High-Risk / GPAI / Limited)
- Flags Article 26(9) FRIA when required (deployers of high-risk AI in services of general interest)
- Computes residual risk + verdict against GDPR Art 35(7)(d)
- Raises Art 36 supervisory-authority consultation flag automatically when residual ≥ 12
- Issues a signed pack (Pro tier) with 365-day public verify URL

## Tools exposed

| Tool | Purpose |
|---|---|
| `generate_dpia(controller, use_case, ...)` | Full draft DPIA in the EDPB structure |
| `map_to_ai_act_article_26_9(use_case)` | FRIA-only fast path |
| `signed_dpia_pack(controller, dpia_json)` | Procurement-grade signed cert (Pro) |
| `list_template_sections()` | Inspect the full EDPB structure before subscribing |
| `pricing()` | Subscribe links + tier comparison |

## Pricing

| Tier | Price | What you get |
|---|---|---|
| Free | £0 | 1 DPIA / day, no signed pack |
| One-off | [£29](https://buy.stripe.com/4gM6oJ1BW4gi6kd6as8k838) | Single signed DPIA pack (auditor evidence) |
| Pro | [£79/mo](https://buy.stripe.com/eVq9AV4O87sudMF42k8k839) | Unlimited DPIAs + template updates as EDPB consultation evolves |
| Enterprise | [£1,499/mo](https://buy.stripe.com/4gM9AV80kaEG0ZT42k8k837) | + custom rule packs + 4h SLA + white-label PDF |

Every signed cert lives at `https://meok-attestation-api.vercel.app/verify/<cert_id>`.

## What you do NOT get

This MCP fills the template. It does not replace a DPO. The `<TO_FILL>` placeholders mark fields where the legal judgement belongs to your DPO, not the wizard.

## Source

EDPB DPIA template explainer adopted 14 April 2026 — [edpb.europa.eu](https://www.edpb.europa.eu/system/files/2026-04/edpb_dpia_template_explainer_2026_v1_en.pdf)

## Built by MEOK AI Labs

Solo founder. London. 234 MCP packages on PyPI. Live signing infrastructure at `meok-attestation-api.vercel.app`. Catalogue: `https://meok-attestation-api.vercel.app/catalogue`.

---

## Distribution channels

- **PyPI**: `pip install meok-dpia-edpb-template-mcp`
- **Apify Store** (Pay-Per-Event): https://apify.com/knowing_yucca/meok-dpia-edpb
- **GitHub** (source): https://github.com/CSOAI-ORG/MEOK-LABS/tree/main/mcps/meok-dpia-edpb-template-mcp
- **Sponsor**: https://github.com/sponsors/CSOAI-ORG · [Pro £79/mo →](https://buy.stripe.com/eVq9AV4O87sudMF42k8k839)

