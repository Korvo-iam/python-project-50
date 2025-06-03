install:
	uv pip sync requirements.txt

test:
	uv run pytest

build:
	uv build

test-coverage:
	uv run pytest --cov=gendiff tests --cov-report xml

package-install:
	uv tool install dist/*.whl

package-install-venv:
	uv tool install dist/*.whl

publish:
	uv run poetry publish --dry-run

lint:
	uv run ruff check gendiff

