# ChainX SIH26183 — no git commands here (user handles git)
up:
	docker compose up -d --build
down:
	docker compose down
logs:
	docker compose logs -f api
build:
	docker compose build
migrate:
	docker compose exec api alembic upgrade head
shell:
	docker compose exec api bash
seed-demo:
	docker compose exec api python scripts/seed-demo.py || python scripts/seed-demo.py
test:
	pytest -q
lint:
	ruff check app/ tests/
format:
	ruff format app/ tests/
check:
	ruff check app/ tests/ && pytest -q
eval:
	python scripts/verify.py
clean:
	docker system prune -f
