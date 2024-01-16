lint:
		poetry run flake8 gendiff_package

test:
		poetry run pytest

install:
		poetry install

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --force-reinstall dist/*.whl

test-coverage:
		poetry run pytest --cov=gendiff_package --cov-report xml
