default: test

.ONESHELL:

.PHONY: help
help: ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

.PHONY: build
build: ## Build helm-tester docker image
	cd ../helpers/helm-tester && \
	for i in {1..5}; do docker build -t helm-tester . && break || sleep 15; done

.PHONY: deps
deps: ## Update helm charts dependencies
	sed --in-place '/charts\//d' ./.helmignore
	helm dependency update

.PHONY: helm
helm: ## Deploy helm on k8s cluster
	kubectl get cs
	kubectl create clusterrolebinding add-on-cluster-admin --clusterrole=cluster-admin --serviceaccount=kube-system:default || true
	helm init --wait --upgrade

.PHONY: lint
lint: ## Lint helm templates
	grep 'charts/' ./.helmignore || echo 'charts/' >> ./.helmignore
	helm lint --strict ./

.PHONY: lint-python
lint-python: ## Lint python scripts
	black --diff --check --exclude='ve/|venv/' .

.PHONY: pytest
pytest: ## Run python tests
	pytest -sv --color=yes

.PHONY: template
template: ## Render chart templates
	helm template ./

.PHONY: test
test: build ## Run all tests in a docker container
	docker run --rm -i --user "$$(id -u):$$(id -g)" -v $$(pwd)/../:/app -w /app/$$(basename $$(pwd)) helm-tester make test-all

.PHONY: test-all ## Run all tests
test-all: lint deps template pytest
