default: test

include ../../../helpers/examples.mk

RELEASE := helm-logstash-security

install:
	helm upgrade --wait --timeout=900 --install $(RELEASE) --values values.yaml ../../

test: install goss

purge:
	helm del --purge $(RELEASE)
	kubectl delete $$(kubectl get pvc -l release=$(RELEASE) -o name)
