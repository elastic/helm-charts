default: test

include ../../../helpers/examples.mk

CHART := logstash
RELEASE := helm-logstash-upgrade
FROM := 6.8.11 # upgrade from version < 6.8.11 is failing due to headless service breaking change

install:
	../../../helpers/upgrade.sh --chart $(CHART) --release $(RELEASE) --from $(FROM)
	kubectl rollout status statefulset $(RELEASE)-logstash

test: install goss

purge:
	helm del $(RELEASE)
