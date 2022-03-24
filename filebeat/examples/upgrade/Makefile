default: test

include ../../../helpers/examples.mk

CHART := filebeat
RELEASE := helm-filebeat-upgrade
# K8S 1.22 doesn't support anymore rbac.authorization.k8s.io/v1beta1 used in 7.9.0
FROM := 7.10.0

install:
	../../../helpers/upgrade.sh --chart $(CHART) --release $(RELEASE) --from $(FROM)
	kubectl rollout status daemonset $(RELEASE)-filebeat

test: install goss

purge:
	helm del $(RELEASE)
