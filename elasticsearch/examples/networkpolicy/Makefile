default: test
include ../../../helpers/examples.mk

RELEASE := helm-es-networkpolicy

install:
	helm upgrade --wait --timeout=600s --install $(RELEASE) --values ./values.yaml ../../ ; \

restart:
	helm upgrade --set terminationGracePeriod=121 --wait --timeout=600s --install $(RELEASE) --values ./values.yaml ../../ ; \

purge:
	helm del --purge $(RELEASE)
