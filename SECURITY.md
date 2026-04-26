# Security Policy

## Reporting

Email **nicholas@csoai.org** with `[SECURITY]` in the subject. We respond within 48h. PGP key on request.

## Disclosure history

| ID | Severity | Status | Affected | Fix |
|---|---|---|---|---|
| V-01 | CRITICAL | FIXED 2026-04-26 | meok-attestation-api | `MEOK_ATTESTATION_KEY` + pepper now REQUIRED at module load (was: silent dev-placeholder fallback that anyone with source-read could forge against) |
| V-02 | CRITICAL | FIXED 2026-04-26 | meok-attestation-api `/webhook` | Hard reject on missing Stripe webhook secret (was: fail-open). Plus replay-window check (±5min). |
| V-03 | HIGH | FIXED 2026-04-26 | meok-attestation-api `/provision` | Customer self-serve now requires real Stripe `session_id` verified live. Master-key bypass for support recovery. |
| V-06 | HIGH | FIXED 2026-04-26 | 6 top MCPs | SSRF allowlist on `MEOK_ATTESTATION_API` env var. Blocks pivot via env-var injection. |
| V-07 | HIGH | FIXED 2026-04-26 | meok-attestation-api `/sign` | Tier resolved server-side from key, never from request body. Previously a Pro key could sign a cert claiming `tier=enterprise`. |

V-04 (anonymous-bucket rate limit) and V-05 (race conditions) are documented as non-issues in single-process MCP context. Server-side V-04 will land with the Vercel KV integration.

## Threat model

MCPs run in user-trust zone. The signing API is the only multi-tenant surface. Audit history at https://github.com/CSOAI-ORG/MEOK-LABS/security
