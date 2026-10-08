# Security Policy — ChainX SIH26183 (PS 183, not 182)

LEA evidence system. Do NOT file public issues for vulnerabilities — contact maintainers privately (see `.github/CODEOWNERS`).

## 183-specific controls (Phase 22/21/20/23)

- **RBAC:** `investigator/reviewer/admin` + row-level case ACL (`lead_investigator_id`). MFA required for `reviewer/admin` and `POST /reports/{id}/sign`.
- **Human gate:** SAHYOG packet export requires `acknowledged_by`; each export carries `request_id UUID UNIQUE` replay nonce. System never auto-freezes, never proves ownership.
- **UPI vault:** store only `SHA256(KMS_salt||vpa_norm)` + `salt_version` (KMS-fetched at boot). Never store raw VPA. Per-install salt forbidden (breaks cross-district join).
- **Evidence integrity:** WORM store, `audit_logs` append-only (no UPDATE/DELETE), candidates immutable (re-run = new row), reports versioned with `content_hash + day_root + sig1/sig2 + kms_key_id`. 1-byte tamper → VERIFY red.
- **Input:** strict address-regex before any query/shell; Pydantic on every boundary; parameterized queries; allowlisted provider endpoints only (SSRF guard).
- **Secrets:** `.env` git-ignored, Vault/KMS in prod, never in image layers. Logs redact `SECRET_KEY/DATABASE_URL/passwords`. Per-user rate limits, mTLS internal, TLS1.2+, at-rest encryption, watermarked gated exports.

## Threats → mitigations

| Threat | Mitigation |
|--------|------------|
| Insider cross-case read | Row ACL + RBAC |
| Evidence/report tamper | WORM + hash chain + dual-sign quorum |
| Spoofed SAHYOG routing | Human gate + nonce |
| Provider label poison | Multi-source + `source_provider/response_hash` provenance |
| SSRF/injection/exfiltration | Allowlist + regex + parameterized + logged export gate |

## Disclosure

Report privately with component, repro, impact, scope. Ack in 2 business days; critical/high fix in 7 days; coordinated disclosure after fix on `main`.
