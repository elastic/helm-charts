default: test
include ../../../helpers/examples.mk

RELEASE := helm-kibana-oss

install:
	helm upgrade --wait --timeout=600s --install --values ./values.yml $(RELEASE) ../../

test: install goss

purge:
	helm del $(RELEASE)
