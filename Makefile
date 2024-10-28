install:
	poetry install

build:
	poetry build

test-coverage:
	hash -r pytest
	pytest --version
	pytest --cov=.

package-install:
	python3 -m pip install --user dist/*.whl

publish:
	poetry publish --dry-run

lint:
	poetry run flake8

check:
	poetry run pytest
