.PHONY: test release clean docs

all: test

test:
	pytest -v

release:
	python3 setup.py sdist bdist_wheel upload

clean:
	find -name *.pyc -delete
	find -name __pycache__ -delete
