default: test

include ../../../helpers/examples.mk

RELEASE := helm-es-default

install:
	helm upgrade --wait --timeout=900s --install $(RELEASE) ../../

restart:
	helm upgrade --set terminationGracePeriod=121 --wait --timeout=900s --install $(RELEASE) ../../

test: install goss

purge:
	helm del $(RELEASE)
