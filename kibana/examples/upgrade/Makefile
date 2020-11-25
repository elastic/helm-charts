default: test

include ../../../helpers/examples.mk

CHART := kibana
RELEASE := helm-kibana-upgrade
FROM := 7.4.0	# versions before 7.4.O aren't compatible with Kubernetes >= 1.16.0
TO := 7.10.0	# required to use with Elasticsearch 7.10.0

install:
	../../../helpers/upgrade.sh --chart $(CHART) --release $(RELEASE) --from $(FROM) --to $(TO)
	kubectl rollout status deployment $(RELEASE)-kibana

test: install goss

purge:
	helm del $(RELEASE)
