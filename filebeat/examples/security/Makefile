default: test

include ../../../helpers/examples.mk

RELEASE := helm-filebeat-security

install:
	helm upgrade --wait --timeout=600 --install $(RELEASE) --values values.yaml ../../

test: install goss

purge:
	helm del --purge $(RELEASE)
