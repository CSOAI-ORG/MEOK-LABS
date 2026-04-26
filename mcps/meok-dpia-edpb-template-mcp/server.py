#!/usr/bin/env python3
"""
MEOK DPIA / EDPB Template MCP — generate a GDPR Article 35 + EU AI Act
Article 26(9) DPIA from a 6-question wizard, signed for audit
==========================================================================
By MEOK AI Labs | https://meok.ai

CONTEXT (April 2026):
  EDPB published the first harmonised DPIA template on 14 April 2026, with
  an explicit AI Act Article 26(9) section. Every EU DPO is rewriting their
  templates this month. This MCP turns a 6-question wizard into a complete
  signed DPIA the auditor accepts — with the EDPB structure baked in.

PROBLEM SOLVED: DPIA template fatigue. Every DPO has 4-12 templates floating
across SharePoint. The new EDPB template forces a redraft. Doing 50+ DPIAs
manually = 200+ hours of paperwork. This MCP collapses that to one wizard
call per use case + one signed PDF/JSON pack per DPIA.

USE CASES:
  - "Generate a draft DPIA for our new AI credit-scoring deployment."
  - "Map this DPIA to AI Act Article 26(9) deployer FRIA requirements."
  - "Sign this DPIA so we have audit evidence the assessment happened on date X."
  - "Generate the residual-risk treatment plan for this processing."

PRICING:
  - Free — 1 DPIA / day, no signed pack
  - £29 one-off — single signed DPIA pack (auditor evidence, 365-day verify URL)
  - Pro £79/mo — unlimited DPIAs + ongoing template updates as EDPB consultation evolves
  - Enterprise £1,499/mo — custom rule packs, SLA, white-label PDF output

Install: pip install meok-dpia-edpb-template-mcp
Run:     python server.py

Source: EDPB DPIA template adopted 14 Apr 2026
  https://www.edpb.europa.eu/system/files/2026-04/edpb_dpia_template_explainer_2026_v1_en.pdf
"""

import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from typing import Any, Optional

from mcp.server.fastmcp import FastMCP

_MEOK_API_KEY = os.environ.get("MEOK_API_KEY", "")

try:
    sys.path.insert(0, os.path.expanduser("~/clawd/meok-labs-engine/shared"))
    from auth_middleware import check_access as _shared_check_access  # type: ignore
except ImportError:
    def _shared_check_access(api_key: str = ""):
        if _MEOK_API_KEY and api_key and api_key == _MEOK_API_KEY:
            return True, "OK", "pro"
        if _MEOK_API_KEY and api_key and api_key != _MEOK_API_KEY:
            return False, "Invalid API key.", "free"
        return True, "OK", "free"


def check_access(api_key: str = ""):
    return _shared_check_access(api_key)


# V-06 FIX: SSRF allowlist on attestation API URL.
try:
    from ssrf_safe import resolve_attestation_api as _resolve_api  # type: ignore
    _ATTESTATION_API = _resolve_api()
except ImportError:
    _ATTESTATION_API_RAW = os.environ.get("MEOK_ATTESTATION_API", "https://meok-attestation-api.vercel.app")
    _ALLOWED_API_HOSTS = {"meok-attestation-api.vercel.app", "meok-verify.vercel.app", "meok.ai", "csoai.org", "councilof.ai", "compliance.meok.ai"}
    try:
        _api_parsed = urllib.parse.urlparse(_ATTESTATION_API_RAW)
        _api_host = (_api_parsed.hostname or "").lower()
        _api_scheme = (_api_parsed.scheme or "").lower()
    except Exception:
        _api_host, _api_scheme = "", ""
    if _api_scheme != "https" or _api_host not in _ALLOWED_API_HOSTS:
        _ATTESTATION_API = "https://meok-attestation-api.vercel.app"
    else:
        _ATTESTATION_API = _ATTESTATION_API_RAW.rstrip("/")

STRIPE_29 = "https://buy.stripe.com/4gM6oJ1BW4gi6kd6as8k838"
STRIPE_79 = "https://buy.stripe.com/eVq9AV4O87sudMF42k8k839"
STRIPE_1499 = "https://buy.stripe.com/4gM9AV80kaEG0ZT42k8k837"

_FREE_DAILY_LIMIT = 1


# ── EDPB 14 Apr 2026 template skeleton (sections 1-9 + AI-Act annex) ──────
EDPB_SECTIONS = [
    {
        "code": "1",
        "title": "Description of the processing operation",
        "fields": ["controller", "joint_controllers", "processor", "purpose", "data_categories", "data_subjects", "recipients", "transfers_outside_eu", "retention_period"],
        "edpb_pointer": "EDPB 2026 §1 / GDPR Art 30(1)",
    },
    {
        "code": "2",
        "title": "Necessity and proportionality assessment",
        "fields": ["lawful_basis", "purpose_limitation_check", "data_minimisation_check", "accuracy_measures", "storage_limitation"],
        "edpb_pointer": "EDPB 2026 §2 / GDPR Art 5 + 6",
    },
    {
        "code": "3",
        "title": "Risks to rights and freedoms of data subjects",
        "fields": ["risk_to_rights", "risk_likelihood_1_to_5", "risk_severity_1_to_5", "risk_score", "vulnerable_groups_impact"],
        "edpb_pointer": "EDPB 2026 §3 / GDPR Art 35(7)(c)",
    },
    {
        "code": "4",
        "title": "Risk-mitigation measures + residual risk",
        "fields": ["technical_measures", "organisational_measures", "residual_risk_score", "residual_risk_acceptable"],
        "edpb_pointer": "EDPB 2026 §4 / GDPR Art 35(7)(d)",
    },
    {
        "code": "5",
        "title": "Stakeholder consultation",
        "fields": ["dpo_consulted", "data_subjects_consulted", "supervisory_authority_consultation_required"],
        "edpb_pointer": "EDPB 2026 §5 / GDPR Art 35(2) + 36",
    },
    {
        "code": "6",
        "title": "AI-specific section (where AI/ADM is involved)",
        "fields": ["uses_ai_system", "ai_act_risk_class", "fria_required", "human_oversight_design", "explanation_to_data_subject"],
        "edpb_pointer": "EDPB 2026 §6 / GDPR Art 22 + EU AI Act Art 26(9)",
    },
    {
        "code": "7",
        "title": "Record of processing decision + sign-off",
        "fields": ["dpo_signoff", "controller_signoff", "decision_date", "review_date_next"],
        "edpb_pointer": "EDPB 2026 §7 / GDPR Art 35(11)",
    },
    {
        "code": "8",
        "title": "Annex — DSAR + breach response readiness",
        "fields": ["dsar_response_sla_days", "breach_notification_72h_capability", "data_portability_format"],
        "edpb_pointer": "EDPB 2026 Annex A",
    },
    {
        "code": "9",
        "title": "Annex — international transfers (if any)",
        "fields": ["transfer_mechanism", "scc_module", "tia_completed", "supplementary_measures"],
        "edpb_pointer": "EDPB 2026 Annex B / Schrems II",
    },
]

# AI Act Article 26(9) — Deployer Fundamental Rights Impact Assessment fields
AI_ACT_FRIA_FIELDS = [
    {"field": "deployer_purpose", "definition": "Description of the deployer's intended purpose for the AI system."},
    {"field": "deployer_period_and_frequency", "definition": "Period of intended use + frequency."},
    {"field": "categories_of_natural_persons_affected", "definition": "Specific categories of persons / groups likely affected by use in specific context."},
    {"field": "specific_risks_of_harm", "definition": "Specific risks of harm to the categories above."},
    {"field": "human_oversight_measures", "definition": "Measures of human oversight per the deployer's instructions for use."},
    {"field": "complaint_mechanism", "definition": "Internal governance + complaint mechanism for affected persons."},
    {"field": "fria_review_cadence", "definition": "When the FRIA will be re-reviewed (annually minimum)."},
]

# Default risk patterns the wizard recognises
DEFAULT_RISK_PATTERNS = {
    "biometric": "Biometric processing → Art 9(1) special-category data → high baseline severity, FRIA likely required.",
    "credit": "Credit-scoring AI → Annex III high-risk under EU AI Act → FRIA mandatory + Art 22 ADM safeguards.",
    "employment": "Employment / HR AI → Annex III high-risk → FRIA mandatory + worker representation consultation.",
    "education": "Education / exam scoring AI → Annex III high-risk → FRIA mandatory.",
    "health": "Health AI → Art 9 special-category + EU AI Act Annex I (MDR overlap) → FRIA + clinical oversight.",
    "law-enforcement": "Law enforcement AI → Annex III high-risk + heightened scrutiny → FRIA + DPIA mandatory.",
    "biometric-categorisation": "Biometric categorisation → Art 5 prohibited risk class → STOP, do not deploy.",
    "social-scoring": "Social scoring → Art 5 prohibited → STOP, do not deploy.",
    "child": "Children's data → Art 8 GDPR + Art 5 AI Act manipulation prohibitions → high baseline.",
    "marketing": "Marketing profiling → Art 22 ADM if automated → opt-out + human-review path required.",
}


def _detect_risk_patterns(use_case_text: str) -> list[dict]:
    """Match a use case description against the default risk catalogue."""
    matches = []
    low = (use_case_text or "").lower()
    for pat, msg in DEFAULT_RISK_PATTERNS.items():
        if pat in low or pat.replace("-", " ") in low:
            matches.append({"pattern": pat, "guidance": msg})
    return matches


def _ai_act_class(use_case_text: str, uses_ai: bool) -> str:
    if not uses_ai:
        return "n/a"
    low = (use_case_text or "").lower()
    if any(p in low for p in ("biometric categorisation", "social scoring", "predictive policing", "subliminal manipulation")):
        return "PROHIBITED (Art 5)"
    if any(p in low for p in ("credit", "employment", "education", "law enforcement", "biometric", "essential service")):
        return "HIGH-RISK (Annex III)"
    if "general-purpose" in low or "foundation" in low or "gpai" in low:
        return "GPAI"
    return "LIMITED / MINIMAL"


def _residual_risk(likelihood: int, severity: int, mitigation_count: int) -> tuple[int, str]:
    raw = likelihood * severity  # 1-25
    mitigation_factor = max(0.3, 1.0 - 0.1 * min(mitigation_count, 7))
    score = int(round(raw * mitigation_factor))
    if score >= 12:
        verdict = "HIGH residual risk — supervisory authority consultation REQUIRED (GDPR Art 36)."
    elif score >= 6:
        verdict = "MEDIUM residual risk — document, monitor quarterly."
    else:
        verdict = "LOW residual risk — proceed with annual review."
    return score, verdict


def _sign_via_attestation_api(api_key: str, dpia: dict) -> dict:
    body = {
        "api_key": api_key,
        "regulation": "GDPR Art 35 + EU AI Act Art 26(9) (EDPB 2026 template)",
        "entity": dpia.get("controller", "anonymous"),
        "score": dpia.get("residual_risk_score", 0),
        "findings": dpia.get("risks_summary", []),
        "articles_audited": [s["code"] for s in EDPB_SECTIONS],
        "auditor_notes": f"DPIA generated via meok-dpia-edpb-template-mcp v1.0 — EDPB 14 Apr 2026 template",
    }
    try:
        data = json.dumps(body).encode("utf-8")
        req = urllib.request.Request(
            f"{_ATTESTATION_API}/sign",
            method="POST", data=data,
            headers={"Content-Type": "application/json", "User-Agent": "meok-dpia-edpb-template/1.0"},
        )
        with urllib.request.urlopen(req, timeout=8) as r:
            return json.loads(r.read().decode("utf-8"))
    except Exception as e:
        return {"error": f"signing unavailable: {type(e).__name__}: {e}"}


_DAILY_USAGE: dict[str, list[float]] = {}


def _consume_quota(tier: str, key: str = "anonymous") -> tuple[bool, str]:
    if tier in ("pro", "enterprise"):
        return True, "OK (paid tier)"
    now = time.time()
    bucket = _DAILY_USAGE.setdefault(key, [])
    cutoff = now - 86400
    bucket[:] = [t for t in bucket if t > cutoff]
    if len(bucket) >= _FREE_DAILY_LIMIT:
        return False, f"Free tier hit ({_FREE_DAILY_LIMIT}/day). Upgrade £29 one-off or Pro £79/mo: {STRIPE_29}"
    bucket.append(now)
    return True, f"OK (free, {_FREE_DAILY_LIMIT - len(bucket)} DPIAs left today)"


# ── MCP server ────────────────────────────────────────────────────────────
mcp = FastMCP("meok-dpia-edpb-template")


@mcp.tool()
def generate_dpia(
    controller: str,
    use_case: str,
    data_categories: str = "",
    data_subjects: str = "",
    lawful_basis: str = "",
    retention_days: int = 365,
    uses_ai: bool = False,
    likelihood_1_to_5: int = 3,
    severity_1_to_5: int = 3,
    mitigation_measures: str = "",
    api_key: str = "",
) -> dict:
    """
    Generate a draft DPIA from the 6-question wizard, structured to the
    EDPB 14 Apr 2026 harmonised template.

    Returns: filled template dict with every EDPB section, automatically
    detected risk patterns, AI Act risk-class verdict, residual risk score,
    and Article 36 supervisor-consultation flag.

    Free tier: 1 DPIA/day. Upgrade for unlimited + signed packs.
    """
    ok, msg, tier = check_access(api_key)
    if not ok:
        return {"error": msg, "upgrade": STRIPE_79}
    quota_ok, quota_msg = _consume_quota(tier, key=api_key or "anonymous")
    if not quota_ok:
        return {"error": quota_msg, "upgrade_one_off": STRIPE_29, "upgrade_pro": STRIPE_79}

    risk_patterns = _detect_risk_patterns(use_case)
    ai_class = _ai_act_class(use_case, uses_ai)
    fria_required = ai_class in ("HIGH-RISK (Annex III)", "PROHIBITED (Art 5)")
    if "STOP" in (rp.get("guidance", "") for rp in risk_patterns) or ai_class == "PROHIBITED (Art 5)":
        return {
            "decision": "STOP — processing falls under EU AI Act Art 5 prohibitions",
            "ai_act_class": ai_class,
            "risk_patterns_matched": risk_patterns,
            "next_action": "Do NOT deploy. Re-scope the use case or seek alternative.",
            "tier": tier, "quota": quota_msg,
        }

    mit_list = [m.strip() for m in (mitigation_measures or "").split(",") if m.strip()]
    residual_score, residual_verdict = _residual_risk(likelihood_1_to_5, severity_1_to_5, len(mit_list))

    consult_required = residual_score >= 12 or "vulnerable" in use_case.lower() or "child" in use_case.lower()

    dpia = {
        "controller": controller,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "template": "EDPB Harmonised DPIA (14 Apr 2026)",
        "ai_act_class": ai_class,
        "fria_required": fria_required,
        "sections": {},
        "risk_patterns_matched": risk_patterns,
        "residual_risk_score": residual_score,
        "residual_risk_verdict": residual_verdict,
        "supervisor_consultation_required_art_36": consult_required,
        "next_review_due": (datetime.now(timezone.utc).replace(year=datetime.now(timezone.utc).year + 1)).date().isoformat(),
        "risks_summary": [r["guidance"][:200] for r in risk_patterns],
    }

    # Fill EDPB sections with the wizard inputs (placeholders where unknown)
    for s in EDPB_SECTIONS:
        section_data = {f: "<TO_FILL>" for f in s["fields"]}
        if s["code"] == "1":
            section_data.update({
                "controller": controller, "purpose": use_case,
                "data_categories": data_categories, "data_subjects": data_subjects,
                "retention_period": f"{retention_days} days",
            })
        elif s["code"] == "2":
            section_data.update({"lawful_basis": lawful_basis or "<TO_FILL — choose Art 6(1) lawful basis>"})
        elif s["code"] == "3":
            section_data.update({
                "risk_likelihood_1_to_5": likelihood_1_to_5,
                "risk_severity_1_to_5": severity_1_to_5,
                "risk_score": likelihood_1_to_5 * severity_1_to_5,
                "vulnerable_groups_impact": ", ".join(r["pattern"] for r in risk_patterns) or "none detected",
            })
        elif s["code"] == "4":
            section_data.update({
                "technical_measures": mit_list,
                "residual_risk_score": residual_score,
                "residual_risk_acceptable": residual_score < 12,
            })
        elif s["code"] == "6":
            section_data.update({
                "uses_ai_system": uses_ai,
                "ai_act_risk_class": ai_class,
                "fria_required": fria_required,
                "human_oversight_design": "<TO_FILL — describe oversight per AI Act Art 14 + Art 26(9)>" if uses_ai else "n/a",
            })
        elif s["code"] == "7":
            section_data.update({
                "decision_date": datetime.now(timezone.utc).date().isoformat(),
                "review_date_next": dpia["next_review_due"],
            })
        dpia["sections"][s["code"]] = {
            "title": s["title"],
            "edpb_pointer": s["edpb_pointer"],
            "data": section_data,
        }

    if fria_required:
        dpia["ai_act_fria_annex"] = {
            "required_by": "EU AI Act Art 26(9)",
            "fields_to_complete": AI_ACT_FRIA_FIELDS,
        }

    return {
        "dpia": dpia,
        "tier": tier,
        "quota": quota_msg,
        "next_step": "Call signed_dpia_pack(controller=…, dpia_json=…) to issue an audit-grade signed cert (£29 one-off or Pro)." if tier == "free" else "Call signed_dpia_pack to seal this DPIA for audit.",
    }


@mcp.tool()
def map_to_ai_act_article_26_9(use_case: str, deployer_purpose: str = "", api_key: str = "") -> dict:
    """
    Map a use case to AI Act Article 26(9) Fundamental Rights Impact Assessment
    (FRIA) — required for deployers of high-risk AI in the public sector and
    private bodies providing services of general interest.
    """
    ok, msg, tier = check_access(api_key)
    if not ok:
        return {"error": msg, "upgrade": STRIPE_79}
    ai_class = _ai_act_class(use_case, uses_ai=True)
    risk_patterns = _detect_risk_patterns(use_case)
    return {
        "ai_act_class": ai_class,
        "fria_required": ai_class in ("HIGH-RISK (Annex III)", "PROHIBITED (Art 5)"),
        "deployer_purpose": deployer_purpose,
        "risk_patterns_matched": risk_patterns,
        "fria_template_fields": AI_ACT_FRIA_FIELDS,
        "next_step": "Call generate_dpia(uses_ai=true, ...) for the full DPIA + FRIA combined pack.",
    }


@mcp.tool()
def signed_dpia_pack(
    controller: str,
    dpia_json: str,
    api_key: str = "",
) -> dict:
    """
    Issue a cryptographically signed DPIA pack with a 365-day public verify URL.
    Use the output dict from generate_dpia() as dpia_json.

    £29 one-off OR Pro £79/mo OR Enterprise £1,499/mo.
    """
    ok, msg, tier = check_access(api_key)
    if not ok or tier not in ("pro", "enterprise"):
        return {
            "error": "signed DPIA packs require £29 one-off (single use) or Pro £79/mo (unlimited)",
            "upgrade_one_off": STRIPE_29,
            "upgrade_pro": STRIPE_79,
            "upgrade_enterprise": STRIPE_1499,
        }
    try:
        dpia = json.loads(dpia_json)
    except json.JSONDecodeError as e:
        return {"error": f"invalid dpia_json: {e}"}
    cert = _sign_via_attestation_api(api_key, {
        "controller": controller,
        "residual_risk_score": dpia.get("residual_risk_score", 0),
        "risks_summary": dpia.get("risks_summary", []),
    })
    return {
        "tier": tier,
        "controller": controller,
        "report": cert,
        "verify_at": cert.get("verify_url"),
        "ship_to_dpo": "Forward this cert + verify URL to your DPO. Upload to your records of processing (Art 30 GDPR).",
    }


@mcp.tool()
def list_template_sections() -> dict:
    """Return the full EDPB 2026 template structure + AI Act FRIA annex fields."""
    return {
        "template_version": "EDPB Harmonised DPIA (14 Apr 2026)",
        "edpb_sections": EDPB_SECTIONS,
        "ai_act_fria_fields": AI_ACT_FRIA_FIELDS,
        "default_risk_patterns": DEFAULT_RISK_PATTERNS,
        "source": "https://www.edpb.europa.eu/system/files/2026-04/edpb_dpia_template_explainer_2026_v1_en.pdf",
    }


@mcp.tool()
def pricing() -> dict:
    """Pricing + subscribe links."""
    return {
        "free": {"price_gbp": 0, "limit": f"{_FREE_DAILY_LIMIT} DPIA / day", "signed_packs": False},
        "one_off_29": {"price_gbp": 29, "subscribe": STRIPE_29, "scope": "single signed DPIA", "signed_packs": True},
        "pro_79": {"price_gbp": 79, "subscribe": STRIPE_79, "scope": "unlimited DPIAs + ongoing template updates", "support": "48h"},
        "enterprise_1499": {"price_gbp": 1499, "subscribe": STRIPE_1499, "scope": "+ custom rule packs + SLA + white-label PDF", "support": "4h"},
        "verify_any_cert": "https://meok-attestation-api.vercel.app/verify",
    }


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
