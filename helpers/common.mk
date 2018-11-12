default: test

.ONESHELL:

lint:
	helm lint ./

template:
	helm template ./

build:
	cd ../helpers/helm-tester && \
	docker build -t helm-tester .

pytest:
	pytest -sv --color=yes

test: build
	docker run --rm -i --user "$$(id -u):$$(id -g)" -v $$(pwd)/../:/app -w /app/$$(basename $$(pwd)) helm-tester make template
	docker run --rm -i --user "$$(id -u):$$(id -g)" -v $$(pwd)/../:/app -w /app/$$(basename $$(pwd)) helm-tester make lint
	docker run --rm -i --user "$$(id -u):$$(id -g)" -v $$(pwd)/../:/app -w /app/$$(basename $$(pwd)) helm-tester make pytest

helm:
	kubectl get cs
	kubectl create clusterrolebinding add-on-cluster-admin --clusterrole=cluster-admin --serviceaccount=kube-system:default || true
	helm init --wait --upgrade
