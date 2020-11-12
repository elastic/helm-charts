default: test

include ../../../helpers/examples.mk

RELEASE := helm-logstash-oss

install:
	helm upgrade --wait --timeout=1200 --install $(RELEASE)  --values ./values.yaml ../../

restart:
	helm upgrade --set terminationGracePeriod=121 --wait --timeout=1200 --install $(RELEASE) ../../

test: install goss

purge:
	helm del --purge $(RELEASE)
