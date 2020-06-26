GOOGLE_PROJECT := elastic-ci-prod
CLUSTER_NAME := helm-elasticsearch-test
KUBERNETES_VERSION := 1.15
CHART := elasticsearch
SUITE := default
NAMESPACE := helm-charts-testing

export TF_VAR_cluster_name=$(CLUSTER_NAME)
export TF_VAR_project=$(GOOGLE_PROJECT)
export TF_VAR_kubernetes_version=$(KUBERNETES_VERSION)

.ONESHELL:

.PHONY: help
help: ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

.PHONY: clean
clean: ## Delete terraform working directory and local state files
	rm credentials.json
	rm -rf .terraform/

credentials.json:
	vault read -field=value \
		"secret/devops-ci/helm-charts/gce/service-account" \
		> credentials.json

.terraform/terraform.tfstate: credentials.json
	terraform init -input=false -reconfigure \
		-backend-config="bucket=terraform-$(GOOGLE_PROJECT)" \
		-backend-config="prefix=$(CLUSTER_NAME)"

.PHONY: init
init: .terraform/terraform.tfstate ## Initialize terraform working directory

.PHONY: fmt
fmt: ## Check terraform files format
	terraform fmt -check=true -diff=true

.PHONY: fmt-write
fmt-write: ## Format terraform files
	terraform fmt -write=true

.PHONY: output
output: init fmt ## Show terraform outputs
	terraform output

.PHONY: plan
plan: init fmt ## Show terraform execution plan
	terraform plan -input=false

.PHONY: apply
apply: init fmt ## Apply terraform execution plan
	terraform apply -input=false -auto-approve

.PHONY: destroy
destroy: init credentials.json creds ## Destroy gke cluster
	kubectl delete namespace $(NAMESPACE)
	terraform destroy -input=false --force

.PHONY: creds
creds: credentials.json ## Get gke credentials
	gcloud auth activate-service-account --key-file=${GOOGLE_CREDENTIALS}
	gcloud --project=$(GOOGLE_PROJECT) container clusters get-credentials $(CLUSTER_NAME) --zone us-central1-a
	kubectl create namespace $(NAMESPACE) || true
	kubectl config set-context $$(kubectl config current-context) --namespace=$(NAMESPACE)

.PHONY: k8s
k8s: apply creds ## Configure gke cluster
	kubectl get cs

.PHONY: k8s-staging-registry
k8s-staging-registry: creds ## Create the staging registry auth secret in k8s
	@DOCKER_PASSWORD="$$(vault read -field=password secret/devops-ci/docker.elastic.co/devops-ci)" && \
		kubectl create secret docker-registry registry-staging \
		--docker-server="docker.elastic.co" \
		--docker-username="devops-ci" \
		--docker-password="$$DOCKER_PASSWORD"

.PHONY: up
up: k8s ## Install helm on gke cluster
	kubectl create clusterrolebinding add-on-cluster-admin --clusterrole=cluster-admin --serviceaccount=kube-system:default || true
	for i in 1 2 3 4 5; do helm init --wait --upgrade && break || sleep 5; done

.PHONY: integration
integration: creds ## Deploy helm chart and run integration tests
	cd ../../$(CHART)/ && \
	helm init --client-only && \
	helm dependency update && \
	cd ./examples/$(SUITE) && \
	make

.PHONY: build
build: ## Build helm-charts docker image
	for i in 1 2 3 4 5; do docker build -t helm-charts . && break || sleep 5; done

.PHONY: pull-private-images
pull-private-images: ## Pull private images used in testing
	cd ../../elasticsearch/examples/security/ && \
		make pull-elasticsearch-image

