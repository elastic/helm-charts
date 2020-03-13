default: test

RELEASE := helm-es-minikube

install:
	helm upgrade --wait --timeout=900s --install --values values.yaml $(RELEASE) ../../

test: install
	helm test $(RELEASE)

purge:
	helm del $(RELEASE)
