default: test

include ../../../helpers/examples.mk

RELEASE := helm-logstash-default

install:
	helm upgrade --wait --timeout=1200s --install $(RELEASE) ../../

restart:
	helm upgrade --set terminationGracePeriod=121 --wait --timeout=1200s --install $(RELEASE) ../../

test: install goss

purge:
	helm del $(RELEASE)
