default: test

include ../../../helpers/examples.mk

CHART := filebeat
RELEASE := helm-filebeat-upgrade
FROM := 6.8.14	# Filebeat 6.8.13 fails with "Registry file path must be a file"
                # error with Elasticsearch 6.8.14-SNAPSHOT

install:
	../../../helpers/upgrade.sh --chart $(CHART) --release $(RELEASE) --from $(FROM)
	kubectl rollout status daemonset $(RELEASE)-filebeat

test: install goss

purge:
	helm del $(RELEASE)
