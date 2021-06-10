default: test

include ../../../helpers/examples.mk

CHART := elasticsearch
RELEASE := helm-es-upgrade
FROM := 6.8.9 # this is the first 6.x release

install:
	../../../helpers/upgrade.sh --chart $(CHART) --release $(RELEASE) --from $(FROM)
	kubectl rollout status statefulset upgrade-master

test: install goss

purge:
	helm del $(RELEASE)
