.PHONY: test release clean docs

all: test

test:
	pytest -v

docs:
	$(MAKE) -C docs html

release:
	python3 setup.py sdist bdist_wheel upload

clean:
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete
