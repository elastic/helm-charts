default: test

include ../../../helpers/examples.mk

RELEASE := helm-filebeat-security

install:
	helm upgrade --wait --timeout=600s --install $(RELEASE) --values values.yaml ../../

test: install goss

purge:
	helm del $(RELEASE)
