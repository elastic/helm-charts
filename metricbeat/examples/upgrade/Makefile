default: test

include ../../../helpers/examples.mk

CHART := metricbeat
RELEASE := helm-metricbeat-upgrade
FROM := 6.8.14 # upgrade from version < 6.8.13 is failing due to selector
               # breaking change in https://github.com/elastic/helm-charts/pull/516

install:
	../../../helpers/upgrade.sh --chart $(CHART) --release $(RELEASE) --from $(FROM)

test: install goss

purge:
	helm del $(RELEASE)
