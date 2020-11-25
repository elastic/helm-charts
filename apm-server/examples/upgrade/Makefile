default: test

include ../../../helpers/examples.mk

CHART := apm-server
RELEASE := helm-apm-server-upgrade
FROM := 6.8.9 # this is the first 6.x release

install:
	../../../helpers/upgrade.sh --chart $(CHART) --release $(RELEASE) --from $(FROM)
	kubectl rollout status deployment $(RELEASE)-apm-server

test: install goss

purge:
	helm del $(RELEASE)
