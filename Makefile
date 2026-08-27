.PHONY: all build start run dev test coverage lint clean docker-build docker-up

all: build test

build:
	cd frontend && npm install && npm run build
	pip install -r backend/requirements.txt

start:
	python main.py

run: start

dev:
	python main.py

test:
	pytest --cov=backend/app --cov-report=term-missing --cov-report=xml backend/tests

coverage:
	pytest --cov=backend/app --cov-report=html --cov-report=xml backend/tests

lint:
	flake8 backend/app --max-line-length=120 --ignore=E501,W503 || true
	cd frontend && npm run lint || true

clean:
	rm -rf frontend/dist backend/__pycache__ .pytest_cache .coverage htmlcov coverage.xml

docker-build:
	docker build -t peoplepulse-crm:latest .

docker-up:
	docker compose up -d
