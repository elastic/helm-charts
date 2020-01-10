default: test
include ../../../helpers/examples.mk

RELEASE := helm-kibana-six

install:
	helm upgrade --wait --timeout=600 --install --values ./values.yml $(RELEASE) ../../

purge:
	helm del --purge $(RELEASE)

test: install goss
