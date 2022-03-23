default: test

include ../../../helpers/examples.mk

CHART := apm-server
RELEASE := helm-apm-server-upgrade
FROM := 7.17.1	# upgrade from version < 7.17.1 is failing due to kube-state-metrics

install:
	../../../helpers/upgrade.sh --chart $(CHART) --release $(RELEASE) --from $(FROM)
	kubectl rollout status deployment $(RELEASE)-apm-server

test: install goss

purge:
	helm del $(RELEASE)
