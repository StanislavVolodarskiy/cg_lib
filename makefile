.PHONY: help
help:
	cat makefile

.PHONY: clean
clean:
	find * -name '*.pyc' -delete
	find * -name __pycache__ -delete

.PHONY: setup
setup:
	pip install -r requirements.txt

.PHONY: test2
test2:
	bash -ci "pyenv-on; flake8"
	bash -ci "pyenv-on; PYTHONPATH=. pytest -v -s --cov=cg_lib --cov-report=term-missing ."

.PHONY: test3
test3:
	bash -ci "pyenv-on 3; flake8"
	bash -ci "pyenv-on 3; PYTHONPATH=. pytest -v -s --cov=cg_lib --cov-report=term-missing ."

.PHONY: test
test: test2 test3
