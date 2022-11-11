# system python interpreter. used only to create virtual environment
PY = python3
VENV = venv
BIN=$(VENV)/bin

DOCS_SRC = docs
DOCS_OUT = $(DOCS_SRC)/_build


ifeq ($(OS), Windows_NT)
	BIN=$(VENV)/Scripts
	PY=python
endif


all: lint mypy test

$(VENV): pyproject.toml
	$(PY) -m venv $(VENV)
	$(BIN)/pip install --upgrade -e .[dev]
	touch $(VENV)

.PHONY: test
test: $(VENV)
	$(BIN)/pytest

.PHONY: mypy
mypy: $(VENV)
	$(BIN)/mypy

.PHONY: lint
lint: $(VENV)
	$(BIN)/flake8

.PHONY: release
release: $(VENV)
	rm -rf dist
	$(BIN)/python3 -m build
	$(BIN)/twine upload dist/*

.PHONY: docs
docs: $(VENV)
	$(BIN)/sphinx-build $(DOCS_SRC) $(DOCS_OUT)

.PHONY: clean
clean:
	rm -rf dist *.egg-info
	rm -rf $(VENV)
	rm -rf $(DOCS_OUT)
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete
	# coverage
	rm -rf htmlcov .coverage
	rm -rf .mypy_cache
