help:
	@echo "setup - setup pyenv and pipenv for the project"
	@echo "format - performing black formatting on the project"
	@echo "pylint - performing pylint to check the code quality"
	@echo "jupyter - open jupyter notebook on the project"

setup:
	bash ./libs/setup.sh

format:
	black ./src

pylint:
	pylint ./src

jupyter:
	pipenv run jupyter notebook