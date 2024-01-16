lint:
	poetry run flake8 gendiff_package

test:
	poetry run pytest

install:
	poetry install

test-coverage:
	poetry run pytest --cov=gendiff_package --cov-report xml
