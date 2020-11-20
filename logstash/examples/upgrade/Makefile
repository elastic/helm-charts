default: test

include ../../../helpers/examples.mk

CHART := logstash
RELEASE := helm-logstash-upgrade
FROM := 7.9.0	# upgrade from version < 7.9.0 is failing due to headless service breaking change

install:
	../../../helpers/upgrade.sh --chart $(CHART) --release $(RELEASE) --from $(FROM)

test: install goss

purge:
	helm del $(RELEASE)
