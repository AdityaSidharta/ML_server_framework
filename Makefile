help:
	@echo "setup - setup pyenv and pipenv for the project"
	@echo "format - performing black formatting on the project"

setup:
	bash ./libs.setup.sh

format:
	black ./src

pylint:
	pylint ./src