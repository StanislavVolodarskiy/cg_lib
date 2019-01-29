.PHONY: help
help:
	cat makefile

.PHONY: clean
clean:
	find * -name '*.pyc' -delete
	find * -name __pycache__ -delete

.PHONY: test
test:
	bash -ic "ac; flake8"
	bash -ic "ac; pytest -v -s --cov=cg_lib --cov-report=term-missing ."
	bash -ic "ac 3; flake8"
	bash -ic "ac 3; pytest -v -s --cov=cg_lib --cov-report=term-missing ."
