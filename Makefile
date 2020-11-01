install:
	poetry install

lint:
	poetry run flake8 gendiff

build:
	poetry build

packege-install:
	pip install --user dist/*.whl

.PHONY: install lint build 
