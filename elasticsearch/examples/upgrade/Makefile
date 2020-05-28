default: test

include ../../../helpers/examples.mk

RELEASE := helm-es-upgrade
KUBE_MINOR_VERSION := $(shell kubectl version -o json | jq -c '.serverVersion.minor' | sed 's/[^0-9]*//g')
VERSION := $(shell test $(KUBE_MINOR_VERSION) -lt 16 && echo 7.0.0-alpha1 || echo 7.4.0)

install:
	helm repo add elastic https://helm.elastic.co && \
	helm upgrade --wait --timeout=600 --install $(RELEASE) elastic/elasticsearch --version $(VERSION) --set clusterName=upgrade ; \
	kubectl rollout status sts/upgrade-master --timeout=600s
	helm upgrade --wait --timeout=600 --set terminationGracePeriod=121 --install $(RELEASE) ../../ --set clusterName=upgrade ; \
	kubectl rollout status sts/upgrade-master --timeout=600s

init:
	helm init --client-only

test: init install goss

purge:
	helm del --purge $(RELEASE)
