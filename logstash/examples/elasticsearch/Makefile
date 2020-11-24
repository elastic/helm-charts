default: test

include ../../../helpers/examples.mk

RELEASE := helm-logstash-elasticsearch

install:
	helm upgrade --wait --timeout=1200s --install $(RELEASE) --values ./values.yaml ../../

restart:
	helm upgrade --set terminationGracePeriod=121 --wait --timeout=1200s --install $(RELEASE) ../../

test: install goss

purge:
	helm del $(RELEASE)
	kubectl delete $$(kubectl get pvc -l release=$(RELEASE) -o name)
