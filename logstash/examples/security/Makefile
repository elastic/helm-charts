default: test

include ../../../helpers/examples.mk

RELEASE := helm-logstash-security

install:
	helm upgrade --wait --timeout=1200s --install $(RELEASE) --values values.yaml ../../

test: install goss

purge:
	helm del $(RELEASE)
	kubectl delete $$(kubectl get pvc -l release=$(RELEASE) -o name)
