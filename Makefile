.PHONY: init
init: ## install package
	pip3 install pipenv
	pipenv install --dev

.PHONY: python_tests
python_tests: ## run unit tests
	pytest --cov=samplePackage tests/
	flake8 

.PHONY: help
help: ## display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)
