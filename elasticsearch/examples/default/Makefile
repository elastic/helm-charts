include ../../../helpers/examples.mk

default: test

RELEASE := helm-es-default
GOSS_CONTAINER := elasticsearch-master-0

install:
	helm upgrade --wait --timeout=600 --install $(RELEASE) ../../ ; \

restart:
	helm upgrade --set terminationGracePeriod=121 --wait --timeout=600 --install $(RELEASE) ../../ ; \

test: goss install

purge:
	helm del --purge $(RELEASE)
