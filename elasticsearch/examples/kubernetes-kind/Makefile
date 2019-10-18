default: test

RELEASE := helm-es-kind

install:
	helm upgrade --wait --timeout=900 --install --values values.yaml $(RELEASE) ../../

test: install
	helm test $(RELEASE)

purge:
	helm del --purge $(RELEASE)
	kubectl delete $$(kubectl get pvc -l release=$(RELEASE) -o name)
