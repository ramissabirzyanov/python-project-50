lint:
		poetry run flake8 gendiff

test:
		poetry run pytest

check:
		poetry run pytest
		poetry run flake8 gendiff

install:
		poetry install

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --force-reinstall dist/*.whl

test-coverage:
		poetry run pytest --cov=gendiff --cov-report xml
