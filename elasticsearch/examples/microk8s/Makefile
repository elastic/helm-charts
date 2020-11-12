default: test

RELEASE := helm-es-microk8s

install:
	helm upgrade --wait --timeout=1200 --install --values values.yaml $(RELEASE) ../../

test: install
	helm test $(RELEASE)

purge:
	helm del --purge $(RELEASE)
