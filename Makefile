# === Makefile for DS/ML Workflow ===

.PHONY: env clean format lint test notebook hooks

# Build environment from environment.yml
env:
	mamba env update --file environment.yml --prune
	poetry install --no-root

# Run all tests
test:
	pytest -v --maxfail=1 --disable-warnings

# Format code
format:
	black src tests
	isort src tests
	ruff check src tests --fix

# Lint only
lint:
	ruff check src tests
	mypy src

# Start JupyterLab
notebook:
	jupyter lab

# Clean caches
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	rm -rf .ruff_cache .mypy_cache

# Install pre-commit hooks
hooks:
	pre-commit install
