# Traceability REQ-001..028 -> code (SIH26183, PS 183)

Source: `SIH26183_Technical_Specification.md` Phases 0-1. Tags: [A] mandatory, [A-opt] may-include (built as core), [B] interpretation, [C] enhancement, [D] cuttable.

| REQ | Title | Phase | Code |
|-----|-------|-------|------|
| REQ-001 | Ingest NCRP+SAHYOG wallets | P7 | `app/api/routes.py:/ingest/ncrp-csv`, `app/intake/ncrp.py` |
| REQ-002 | Auto forward trace | P10 A-B | `app/engine/attribution.py`, `app/graph/queries.cypher` |
| REQ-003 | Nearest fraud-linked VASP deposit | P3/P10 | `app/engine/attribution.py:rank`, `tiers.py` |
| REQ-004 | Peel/fan-out/layering/burner patterns | P10 C + P15 | `app/engine/attribution.py`, `app/risk_ml/m1_lgbm` |
| REQ-005 | Ranked VASP + action + evidence refs | P10 G-H | `app/api/routes.py:/trace`, `app/evidence/store.py` |
| REQ-006 | Six chains + adapter | P4/P24 | `app/providers/tron|eth|bnb|sol|pol|btc`, `base.py`, `demo.py` |
| REQ-007 | Real-time (cached s-scale, mempool pre-confirm) | P18/P26 | `ext/mempool/replay.py`, `app/indexer/watch.py`, `/health /ready` |
| REQ-008 | Freeze-first recommendations | P3 | `app/engine/attribution.py:freezability` |
| REQ-009 | LEA dashboards | P19 | `frontend/src/pages/*`, `components/*` |
| REQ-010 | Real-time intel generation | P7/P10 | `app/api/routes.py:/trace` |
| REQ-011 | Automated VASP identification | P10 | `app/engine/*` |
| REQ-012 | Suspect wallet tracing | P10 A-B | `app/graph/*` |
| REQ-013 | Cross-chain analytics | P14 | `BRIDGE_DECAY=0.8`, `vasp_data/fee_tables/bridges.csv`, `CrossChainView.tsx` |
| REQ-014 | Fund-flow visualization | P19 | `FundFlowGraph.tsx` (mixer dead-end, bridge dashed) |
| REQ-015 | LEA integration (NCRP/SAHYOG packet) | P7/P23 | `GET /export/sahyog-packet.json` (nonce + acknowledged_by gate) |
| REQ-016 | Standardized reports + s.63 pack | P20 | `app/reports/generator.py`, `app/evidence/store.py`, `scripts/verify.py` |
| REQ-017 | Reduce response / improve freeze / evidence goals | P26 | `eval/cases.json`, `tests/` gates |
| REQ-018 | API integrations | P7 | `app/main.py:create_app`, `app/api/routes.py` |
| REQ-019 | Scalable indexing | P26 | `docker-compose.yml` pg/redis/neo4j single-node, parquet caches |
| REQ-020 | AI/ML risk detection | P16 | `app/risk_ml/m1_lgbm`, `m2_mixer` |
| REQ-021 | Typology pattern recognition | P16 | `app/risk_ml/m4_typology_ner`, `m3_bridge` |
| REQ-022 | Tx graph analysis [A-opt→core] | P11 | `app/graph/queries.cypher` |
| REQ-023 | Exchange wallet clustering [A-opt→core] | P11 | engine evidence (CIO/behavioral stub) |
| REQ-024 | Intermediary laundering detect [A-opt→core] | P10 C-D | filter + evidence |
| REQ-025 | Cross-chain movement [A-opt→core] | P14 | bridge matcher |
| REQ-026 | SAHYOG+NCRP integration [A-opt→core] | P7 | ingest + packet export (offline-first, contracts unpublished) |
| REQ-027 | Automated alerts [A-opt→core] | P18 | `app/alerts/watch.py` (dedup_key + nonce, REPLAY badge) |
| REQ-028 | Wallet risk categorization [A-opt→core] | P16 | M1 triage-only + bands High≥70/Med40-69/Low<40 |

Gates (P26): Top-1≥0.70, false-High=0, mixer abstain-precision≥0.95, p95 cached≤3s/live≤60s/mempool≤4s (rig 10k-tx, 4vCPU/8GB, n=100, MAX_HOPS=5).
EXT (gated, `EXT_ENABLED=false`): campaign P12, sponsor P13, UPI join P17, mempool live P18 → `ext/*`.
Optional [D] P27: `optional_d27/D01-D08` isolated, never on core path.
