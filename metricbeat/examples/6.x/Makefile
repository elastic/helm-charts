default: test

include ../../../helpers/examples.mk

RELEASE := helm-metricbeat-six
GOSS_SELECTOR = release=$(RELEASE),app=helm-metricbeat-six-metricbeat

install:
	helm upgrade --wait --timeout=600 --install $(RELEASE) --values values.yaml ../../

purge:
	helm del --purge $(RELEASE)

test-metrics:
	 GOSS_FILE=goss-metrics.yaml make goss GOSS_SELECTOR=release=$(RELEASE),app=helm-metricbeat-six-metricbeat-metrics

test: install goss test-metrics
