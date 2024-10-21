install:
	poetry install

build:
	poetry build

test-coverage:
	poetry run pytest --cov

package-install:
	python3 -m pip install --user dist/*.whl

publish:
	poetry publish --dry-run

lint:
	poetry run flake8

check:
	poetry run pytest
