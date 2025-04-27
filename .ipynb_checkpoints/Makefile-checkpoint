.PHONY: format lint all

isort:
	poetry run isort .

black:
	poetry run black .

lint:
	poetry run pylint your_module_or_file.py

format: isort black

all: format lint