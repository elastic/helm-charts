default: test

include ../../../helpers/examples.mk

RELEASE := helm-apm-server-default

install:
	helm upgrade --wait --timeout=600 --install $(RELEASE) ../../

test: install goss

purge:
	helm del --purge $(RELEASE)
