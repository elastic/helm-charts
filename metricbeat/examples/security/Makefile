default: test

include ../../../helpers/examples.mk

RELEASE := helm-metricbeat-security
GOSS_SELECTOR = release=$(RELEASE),app=helm-metricbeat-security-metricbeat

install:
	helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
	helm dependency update ../../
	helm upgrade --wait --timeout=$(TIMEOUT) --install --values values.yaml $(RELEASE) ../../

test-metrics:
	 GOSS_FILE=goss-metrics.yaml make goss GOSS_SELECTOR=release=$(RELEASE),app=helm-metricbeat-security-metricbeat-metrics

test: install goss test-metrics

purge:
	helm del $(RELEASE)
