default: test

include ../../../helpers/examples.mk

CHART := metricbeat
RELEASE := helm-metricbeat-upgrade
#FROM := 7.10.0	# upgrade from version < 7.10.0 is failing due to selector
								# breaking change in https://github.com/elastic/helm-charts/pull/516

install:
	../../../helpers/upgrade.sh --chart $(CHART) --release $(RELEASE) --from $(FROM)

#TODO: uncomment after 7.10.0 release
test: #install goss

purge:
	helm del $(RELEASE)
