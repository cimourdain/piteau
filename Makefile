PYVERSION ?= py36

PROJECT_FOLDER = piteau/
TESTS_FOLDER = tests/
SAMPLES_FOLDER = samples/

STYLE_FOLDERS = $(PROJECT_FOLDER) $(TESTS_FOLDER) $(SAMPLES_FOLDER)

DOCKER_IMG_NAME = $(PYVERSION)
DOCKER_IMG_NAME_DEV = $(PYVERSION)-dev

DOCKER_RUN = docker-compose run --rm $(DOCKER_IMG_NAME)
DOCKER_RUN_DEV = docker-compose run --rm $(DOCKER_IMG_NAME_DEV) poetry run

deinit:
	docker system prune

init:
	docker-compose build --no-cache $(DOCKER_IMG_NAME)

run:
	$(DOCKER_RUN) sh scripts/run.sh "PYTHONPATH=. python"

init-dev:
	docker-compose build --no-cache $(DOCKER_IMG_NAME_DEV)

test:
	$(DOCKER_RUN_DEV) pytest $(TESTS_FOLDER)

style:
	$(DOCKER_RUN_DEV) poetry run flake8 $(STYLE_FOLDERS)
	$(DOCKER_RUN_DEV) poetry run black $(STYLE_FOLDERS) --check --diff
	$(DOCKER_RUN_DEV) poetry run mypy $(PROJECT_FOLDER) --disallow-untyped-defs  --disallow-incomplete-defs --ignore-missing-imports
	$(DOCKER_RUN_DEV) poetry run isort -rc $(STYLE_FOLDERS) --diff

black:
	$(DOCKER_RUN_DEV) poetry run black $(STYLE_FOLDERS)

isort:
	$(DOCKER_RUN_DEV) poetry run isort -rc $(STYLE_FOLDERS)


docs:
	$(DOCKER_RUN) poetry run mkdocs build --clean

ci: test style docs
