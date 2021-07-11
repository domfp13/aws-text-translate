
.PHONY: package
package: ## Rebuilds the container image and remove orphan containers
	@ echo "1.- Building image"
	docker image build --rm -t aws-translate-image .

.PHONY: start
start: ## (Local Testing): Stand up services
	@ echo "Standing up Services"
	docker-compose up --build --remove-orphans -d
	docker container exec -it agent_python /bin/bash

.PHONY: stop
stop: ## (Local Testing): Remove services
	@ echo "Removing Services"
	docker-compose down -v

help:
	@ echo "Please use \`make <target>' where <target> is one of"
	@ perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help