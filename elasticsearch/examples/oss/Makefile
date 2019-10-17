default: test
include ../../../helpers/examples.mk

RELEASE := helm-es-oss

install:
	helm upgrade --wait --timeout=600 --install $(RELEASE) --values ./values.yaml ../../

test: install goss

purge:
	helm del --purge $(RELEASE)
	for pvc in $$(kubectl get pvc -o name | grep $(RELEASE)); do kubectl delete $$pvc; done
