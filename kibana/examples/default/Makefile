
default: test

RELEASE := helm-kibana-default

install:
	helm upgrade --wait --timeout=600 --install $(RELEASE) ../../ ; \

test: install
	helm test $(RELEASE)

purge:
	helm del --purge $(RELEASE)
