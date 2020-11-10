default: test
include ../../../helpers/examples.mk

RELEASE := helm-kibana-default

install:
	echo "Goss container: $(GOSS_CONTAINER)"
	helm upgrade --wait --timeout=900 --install $(RELEASE) ../../

test: install goss

purge:
	helm del --purge $(RELEASE)
