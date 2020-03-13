default: test

include ../../../helpers/examples.mk

RELEASE := helm-metricbeat-security
GOSS_SELECTOR = release=$(RELEASE),app=helm-metricbeat-security-metricbeat

install:
	helm upgrade --wait --timeout=600s --install $(RELEASE) --values values.yaml ../../

purge:
	helm del $(RELEASE)

test-metrics:
	 GOSS_FILE=goss-metrics.yaml make goss GOSS_SELECTOR=release=$(RELEASE),app=helm-metricbeat-security-metricbeat-metrics

test: install goss test-metrics
