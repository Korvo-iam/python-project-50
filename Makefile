install:
	uv pip install -r requirements.txt

test:
	uv run pytest

build:
	poetry build

test-coverage:
	uv run pytest --cov=gendiff tests --cov-report xml

package-install:
	python3 -m pip install --user dist/*.whl

package-install-venv:
	python3 -m pip install dist/*.whl

publish:
	poetry publish --dry-run

lint:
	uv run flake8

check:
	uv run pytest
