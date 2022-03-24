default: test

include ../../../helpers/examples.mk

CHART := filebeat
RELEASE := helm-filebeat-upgrade
# upgrade from versions before 7.17.1 isn't compatible with 8.x
FROM := 7.17.1

install:
	../../../helpers/upgrade.sh --chart $(CHART) --release $(RELEASE) --from $(FROM)
	kubectl rollout status daemonset $(RELEASE)-filebeat

test: install goss

purge:
	helm del $(RELEASE)
