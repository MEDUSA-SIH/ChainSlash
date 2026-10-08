# SIH26183 — no git commands here (user handles git)
up:
	docker compose up --build

seed-demo:
	python scripts/seed-demo.py

test:
	pytest -q

eval:
	python scripts/verify.py
