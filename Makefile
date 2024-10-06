install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

publish:
	poetry publish --dry-run

run:
	poetry run gendiff

lint:
	poetry run flake8 gendiff
