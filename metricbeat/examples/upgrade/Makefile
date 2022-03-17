default: test

include ../../../helpers/examples.mk

CHART := metricbeat
RELEASE := helm-metricbeat-upgrade
FROM := 7.17.1	# upgrade from version < 7.17.1 is failing due to kube-state-metrics
								# dependency upgrade in https://github.com/elastic/helm-charts/pull/1524

install:
	helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
	helm dependency update ../../
	../../../helpers/upgrade.sh --chart $(CHART) --release $(RELEASE) --from $(FROM)
	kubectl rollout status daemonset $(RELEASE)-metricbeat
	kubectl rollout status deployment $(RELEASE)-metricbeat-metrics
	kubectl rollout status deployment $(RELEASE)-kube-state-metrics

test: install goss

purge:
	helm del $(RELEASE)
