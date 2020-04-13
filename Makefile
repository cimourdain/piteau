PYVERSION ?= py36

PROJECT_FOLDER = piteau/
TESTS_FOLDER = tests/
DOCKER_RUN = docker-compose run --rm piteau-$(PYVERSION)

shell:
	$(DOCKER_RUN) bash

style:
	$(DOCKER_RUN) make style-local

docs:
	$(DOCKER_RUN) make docs-local

test:
	$(DOCKER_RUN) make test-local

ci:
	$(DOCKER_RUN) make ci-local


init-local:
	poetry install

test-local: init-local
	poetry run pytest $(TESTS_FOLDER) -x

style-check-local: init-local
	poetry run flake8 $(PROJECT_FOLDER)
	poetry run black $(PROJECT_FOLDER) --check --diff
	poetry run mypy $(PROJECT_FOLDER) --disallow-untyped-defs  --disallow-incomplete-defs --ignore-missing-imports
	poetry run isort -rc $(PROJECT_FOLDER) --diff

docs-local: init-local
	pip install -r docs/requirements.txt
	poetry run mkdocs build --clean

style-fix-local: init-local
	poetry run black $(PROJECT_FOLDER)
	poetry run isort -rc $(PROJECT_FOLDER)

ci-local: test-local style-check-local docs-local
