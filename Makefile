install:
	poetry install

test:
	poetry run pytest tests --cov=gendiff

lint:
	poetry run flake8 gendiff

selfchek:
	poetry check

check: selfchek test lint 

build: check
	poetry build

packege-install:
	pip install --user dist/*.whl

.PHONY: install lint selfchek check build 
