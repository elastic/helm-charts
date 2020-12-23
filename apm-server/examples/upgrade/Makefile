default: test

include ../../../helpers/examples.mk

CHART := apm-server
RELEASE := helm-apm-server-upgrade
FROM := 7.6.0	# 7.6.0 is the first release for apm-server

install:
	../../../helpers/upgrade.sh --chart $(CHART) --release $(RELEASE) --from $(FROM)
	kubectl rollout status deployment $(RELEASE)-apm-server

test: install goss

purge:
	helm del $(RELEASE)
