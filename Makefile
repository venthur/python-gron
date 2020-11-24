all: lint test

test:
	pytest
.PHONY: test

lint:
	flake8 gron
.PHONY: lint

docs:
	$(MAKE) -C docs html
.PHONY: docs

release:
	python3 setup.py sdist bdist_wheel upload
.PHONY: release

clean:
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete
.PHONY: clean
