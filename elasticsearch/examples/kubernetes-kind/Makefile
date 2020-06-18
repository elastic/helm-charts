default: test

RELEASE := helm-es-kind

install:
	helm upgrade --wait --timeout=900 --install --values values.yaml $(RELEASE) ../../

install-local-path:
	kubectl apply -f https://raw.githubusercontent.com/rancher/local-path-provisioner/master/deploy/local-path-storage.yaml
	helm upgrade --wait --timeout=900 --install --values values-local-path.yaml $(RELEASE) ../../

test: install
	helm test $(RELEASE)

purge:
	helm del --purge $(RELEASE)
