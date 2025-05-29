install:
	poetry pip install -r requirements.txt

test:
	poetry run pytest

build:
	poetry build

test-coverage:
	poetry run pytest --cov=gendiff tests --cov-report xml

package-install:
	python3 -m pip install --user dist/*.whl

package-install-venv:
	python3 -m pip install dist/*.whl

publish:
	poetry publish --dry-run

lint:
	poetry run flake8

check:
	poetry run pytest
