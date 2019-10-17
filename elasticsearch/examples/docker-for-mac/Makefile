default: test

RELEASE := helm-es-docker-for-mac

install:
	helm upgrade --wait --timeout=900 --install --values values.yaml $(RELEASE) ../../

test: install
	helm test $(RELEASE)

purge:
	helm del --purge $(RELEASE)
	for pvc in $$(kubectl get pvc -o name | grep $(RELEASE)); do kubectl delete $$pvc; done
