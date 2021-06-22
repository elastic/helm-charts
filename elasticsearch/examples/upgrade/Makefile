default: test

include ../../../helpers/examples.mk

CHART := elasticsearch
RELEASE := helm-es-upgrade
FROM := 7.4.0	# versions before 7.4.O aren't compatible with Kubernetes >= 1.16.0
TO := 7.13.0	# upgrade from 7.x to 8.0.0-SNAPSHOT currently doesn't work

install:
	../../../helpers/upgrade.sh --chart $(CHART) --release $(RELEASE) --from $(FROM) --to $(TO)
	kubectl rollout status statefulset upgrade-master

test: install goss

purge:
	helm del $(RELEASE)
