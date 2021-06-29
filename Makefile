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


all: lint test

$(VENV): requirements-dev.txt setup.py
	$(PY) -m venv $(VENV)
	$(BIN)/pip install --upgrade -r requirements-dev.txt
	$(BIN)/pip install -e .
	touch $(VENV)

.PHONY: test
test: $(VENV)
	$(BIN)/pytest

.PHONY: lint
lint: $(VENV)
	$(BIN)/flake8

.PHONY: release
release: $(VENV)
	rm -rf dist
	$(BIN)/python setup.py sdist bdist_wheel
	$(BIN)/twine upload dist/*

.PHONY: docs
docs: $(VENV)
	$(BIN)/sphinx-build $(DOCS_SRC) $(DOCS_OUT)

.PHONY: clean
clean:
	rm -rf build dist *.egg-info
	rm -rf $(VENV)
	rm -rf $(DOCS_OUT)
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete
	# coverage
	rm -rf htmlcov .coverage
