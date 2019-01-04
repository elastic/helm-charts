
default: test

RELEASE := helm-es-seven

install:
	helm upgrade --wait --timeout=600 --install $(RELEASE) --values ./values.yaml ../../ ; \

restart:
	helm upgrade --set terminationGracePeriod=121 --wait --timeout=600 --install $(RELEASE) --values ./values.yaml ../../ ; \

test: install
	helm test $(RELEASE)

purge:
	helm del --purge $(RELEASE)
