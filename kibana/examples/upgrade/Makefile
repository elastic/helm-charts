default: test

include ../../../helpers/examples.mk

CHART := kibana
RELEASE := helm-kibana-upgrade
FROM := 7.17.1	# same version as Elasticsearch chart

install:
	../../../helpers/upgrade.sh --chart $(CHART) --release $(RELEASE) --from $(FROM) --to $(TO)
	kubectl rollout status deployment $(RELEASE)-kibana

test: install goss

purge:
	helm del $(RELEASE)
