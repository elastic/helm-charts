default: test
include ../../../helpers/examples.mk

RELEASE := elasticsearch

template:
	helm template --values ./values.yaml ../../

install:
	helm upgrade --wait --timeout=900s --install $(RELEASE) --values ./values.yaml ../../

test: install goss

purge:
	helm del $(RELEASE)
