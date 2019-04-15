include config.env
include deploy.env

VERSION_FILE = VERSION

.DEFAULT_GOAL := help

.PHONY: help
help:
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' Makefile \
		| awk 'BEGIN {FS = ":.*?## "}{printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' \
		| sed -e 's/\[32m##/[33m/'

## Vagrant targets

.PHONY: up
up: ## Perform a Vagrant up
	@vagrant up

.PHONY: provision
provision: ## Re-run Vagrant ansible provisioners
	@vagrant provision --provision-with ansible_local

.PHONY: clean
clean: ## Teardown working environment
	@vagrant destroy --force
	@vboxmanage list runningvms \
	| grep $(APP_NAME) \
	| awk '{ print $$2 }' \
	| xargs -I vmid vboxmanage controlvm vmid poweroff
	@vboxmanage list vms \
	| grep $(APP_NAME) \
	| awk '{ print $$2 }' \
	| xargs -I vmid vboxmanage unregistervm vmid

.PHONY: connect
connect: ## Connect to guest
	@vagrant ssh

.PHONY: status
status: ## Query status of vagrant machines
	@vagrant status

## Development targets

.PHONY: install
install: ## Install pipenv virtual environment
	@pipenv install

.PHONY: run-naked
run-naked: ## Run flask embedded web server
	# --host=0.0.0.0
	# listen on all public IP addresses
	@pipenv run flask run --host=0.0.0.0

## Docker targets

.PHONY: build
build: ## Build docker container
	@docker build -t $(APP_NAME) .

.PHONY: run
run: ## Run docker container
	docker run -i -t --rm --name=$(APP_NAME) -p=$(PORT):$(PORT) $(APP_NAME)

.PHONY: stop
stop: ## Stop and tear down docker container
	@docker stop $(APP_NAME)
	@docker rm $(APP_NAME)

## Tagging targets

.PHONY: tag
tag: git-tag docker-tag-latest docker-tag-version

.PHONY: git-tag
git-tag: ## Tag git repos with current version
	$(eval VERSION := $(shell cat $(VERSION_FILE)))
	@git add $(VERSION_FILE)
	@git commit -m "Bumped version to $(VERSION)"
	@git tag $(VERSION)
	@git push origin
	@git push origin $(VERSION)

.PHONY: docker-tag-latest
docker-tag-latest: ## Tag current docker image as latest
	@docker tag $(APP_NAME) $(DOCKER_REPO)/$(APP_NAME):latest

.PHONY: docker-tag-version
docker-tag-version: ## Tag docker image with version specified in VERSION file
	$(eval VERSION := $(shell cat $(VERSION_FILE)))
	@docker tag $(APP_NAME) $(DOCKER_REPO)/$(APP_NAME):$(VERSION)

## Release targets

.PHONY: release
release: bump-version

.PHONY: bump-version
bump-version: ## Increment version patch number
	@$(eval VERSION := $(shell awk -F. 'BEGIN {OFS="."}; {$$NF+=1; print $$0}' $(VERSION_FILE)))
	$(file > $(VERSION_FILE), $(VERSION))
	@echo "Version bumped to $(VERSION)"
