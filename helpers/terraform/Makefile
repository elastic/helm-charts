GOOGLE_PROJECT := elastic-ci-prod
CLUSTER_NAME := helm-elasticsearch-test
KUBERNETES_VERSION := 1.9.7-gke.6
CHART := elasticsearch
SUITE := default
NAMESPACE := helm-charts-testing

export TF_VAR_cluster_name=$(CLUSTER_NAME)
export TF_VAR_project=$(GOOGLE_PROJECT)
export TF_VAR_kubernetes_version=$(KUBERNETES_VERSION)

.ONESHELL:

credentials.json:
	vault read -field=value \
		"secret/devops-ci/helm-charts/gce/service-account" \
		> credentials.json

.terraform/terraform.tfstate: credentials.json
	terraform init -input=false -reconfigure \
		-backend-config="bucket=terraform-$(GOOGLE_PROJECT)" \
		-backend-config="prefix=$(CLUSTER_NAME)"

.PHONY: init
init: .terraform/terraform.tfstate

.PHONY: fmt
fmt:
	terraform fmt -check=true -diff=true

fmt-write:
	terraform fmt -write=true

.PHONY: output
output: init fmt
	terraform output

.PHONY: plan
plan: init fmt
	terraform plan -input=false

.PHONY: apply
apply: init fmt
	terraform apply -input=false -auto-approve

.PHONY: destroy
destroy: init credentials.json creds
	kubectl delete namespace $(NAMESPACE)
	terraform destroy -input=false --force

creds: credentials.json
	gcloud auth activate-service-account --key-file=${GOOGLE_CREDENTIALS}
	gcloud --project=$(GOOGLE_PROJECT) container clusters get-credentials $(CLUSTER_NAME) --zone us-central1-a
	kubectl create namespace $(NAMESPACE) || true
	kubectl config set-context $$(kubectl config current-context) --namespace=$(NAMESPACE)

k8s: apply creds
	kubectl get cs

up: k8s
	kubectl create clusterrolebinding add-on-cluster-admin --clusterrole=cluster-admin --serviceaccount=kube-system:default || true
	for i in 1 2 3 4 5; do helm init --wait --upgrade && break || sleep 5; done

integration: creds
	cd ../../$(CHART)/examples/$(SUITE) && \
	make

build: 
	docker build -t helm-charts .
