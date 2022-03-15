default: test

include ../../../helpers/examples.mk

RELEASE = helm-metricbeat-default
GOSS_SELECTOR = release=$(RELEASE),app=helm-metricbeat-default-metricbeat

install:
	helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
	helm dependency update ../../
	helm upgrade --wait --timeout=$(TIMEOUT) --install $(RELEASE) ../../

test-metrics:
	 GOSS_FILE=goss-metrics.yaml make goss GOSS_SELECTOR=release=$(RELEASE),app=helm-metricbeat-default-metricbeat-metrics

test: install goss test-metrics

purge:
	helm del $(RELEASE)
