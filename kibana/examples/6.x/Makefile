default: test
include ../../../helpers/examples.mk

RELEASE := helm-kibana-six

install:
	helm upgrade --wait --timeout=600s --install --values ./values.yml $(RELEASE) ../../

purge:
	helm del $(RELEASE)

test: install goss
