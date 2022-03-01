default: test

include ../../../helpers/examples.mk

CHART := elasticsearch
RELEASE := helm-es-upgrade
FROM := 7.4.0	# versions before 7.4.O aren't compatible with Kubernetes >= 1.16.0

install:
	../../../helpers/upgrade.sh --chart $(CHART) --release $(RELEASE) --from $(FROM)
	# Rolling upgrade doesn't work when upgrading from clusters with security disabled.
	# This is because nodes with security enabled can't join a cluster with security disabled.
	# Every nodes need to be recreated at the same time so they can recreate a cluster with security enabled
	kubectl delete pod --selector=app=upgrade-master

test: install goss

purge:
	helm del $(RELEASE)
