default: test

include ../../../helpers/examples.mk

CHART := metricbeat
RELEASE := helm-metricbeat-upgrade
FROM := 6.8.14 # upgrade from version < 6.8.13 is failing due to selector
               # breaking change in https://github.com/elastic/helm-charts/pull/516

install:
	helm repo add stable https://charts.helm.sh/stable
	helm dependency update ../../
	../../../helpers/upgrade.sh --chart $(CHART) --release $(RELEASE) --from $(FROM)
	kubectl rollout status daemonset $(RELEASE)-metricbeat
	kubectl rollout status deployment $(RELEASE)-metricbeat-metrics
	kubectl rollout status deployment $(RELEASE)-kube-state-metrics

test: install goss

purge:
	helm del $(RELEASE)
