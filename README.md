# ChainX — SIH26183 Fraud-Linked VASP Tracer

Real-time identification of fraud-linked crypto exchanges from victim-reported wallets — TRON/ETH/BNB live tracing, freezability-ranked VASP attribution, campaign + sponsor graphs, s.63-ready evidence packs for LEAs | SIH 2026 SIH26183 MHA-I4C

Stack: Python 3.12 FastAPI + Postgres16 + Redis7 + Neo4j5 single-node Docker. Spec Phases 0-26 core, Phase 27 optional. `EXT_ENABLED=false` default.

## 1. Prereqs
- Docker Desktop 24+ + Compose v2, git 2.40+, gh 2.40+, make, uv 0.4+
- 4vCPU/8GB, 10GB free; python 3.12, node 20 + npm
- Windows: WSL2 bash preferred

## 2. Clone + remote (gh)
gh auth login
gh repo clone <owner>/ChainX && cd ChainX
cp .env.example .env
# fresh repo: git init -b main && gh repo create ChainX --private --source=. --push

## 3. Full stack (Docker)
docker compose config
docker compose up -d --build
docker compose exec api alembic upgrade head
docker compose exec api python scripts/seed-demo.py
curl http://localhost:8000/health
curl http://localhost:8000/ready
docker compose --profile demo up -d --build
# frontend: http://localhost:5173

## 4. Daily dev with uv + npm (faster)
docker compose up -d postgres redis neo4j
uv venv --python 3.12
source .venv/bin/activate
uv pip install -e ".[dev]"
uv run uvicorn app.main:app --reload --port 8000
# new shell:
cd frontend; npm install; npm run dev
# VITE_API_URL=http://localhost:8000

## 5. Make shortcuts
make up | make logs | make migrate | make seed-demo
make test | make eval | make down | make shell
make lint | make format | make check | make clean

## 6. Git + gh flow
git status; git add -A; git commit -m "feat: ..."
git push -u origin main
gh pr create --base develop --fill
gh run list --limit 5

## 7. Verify
curl -s localhost:8000/health | jq
curl -s -X POST localhost:8000/trace -H 'content-type: application/json' -d '{"address":"TXYZ12345678901234567890123456789012","chain":"TRON"}' | jq
uv run pytest -q
uv run ruff check app/ tests/
# eval: 6 cases in eval/cases.json (direct/1-hop/multi/mixer-abstain/bridge/false-hub)

## 8. Env (.env never committed)
DEMO_MODE=true, EXT_ENABLED=false, SECRET_KEY, JWT_*,
POSTGRES_*, REDIS_*, NEO4J_*, ATTRIBUTION_MAX_HOPS=5, BRIDGE_DECAY=0.8,
PROVIDER_TRON|ETH|BNB|SOL|POL|BTC_ENABLED, KMS_SALT_VERSION=1, VITE_API_URL

## 9. Ports
8000 api, 5432 pg, 6379 redis, 7474/7687 neo4j, 5173 web

## 10. Troubleshoot
- CRLF warnings: `* text=auto eol=lf` is set
- Port busy: override *_PORT in .env
- Neo4j cold boot: wait 30s, /ready 503 = warming
- Reset: docker compose down -v (wipes pgdata/neodat)

## 11. Layout
app/ (api/providers/indexer/normalize/graph/engine/risk_ml/cases/evidence/reports/alerts/security + core/)
ext/ (campaign/sponsor/upi_link/mempool, gated) | optional_d27/ (D01-D08, gated)
eval/canned/ | tests/ | vasp_data/ | scripts/ | frontend/src/ | docs/TRACEABILITY.md
