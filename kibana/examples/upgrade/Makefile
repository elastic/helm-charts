default: test

include ../../../helpers/examples.mk

CHART := kibana
ES_CLUSTER := kibana-upgrade
ES_RELEASE := helm-kibana-upgrade-es
RELEASE := helm-kibana-upgrade-kb
FROM := 7.17.1

repo:
	helm repo add elastic https://helm.elastic.co

install-es:
	helm install $(ES_RELEASE) elastic/elasticsearch --wait --version $(FROM) --set clusterName=$(ES_CLUSTER)

install-kb:
	helm install $(RELEASE) elastic/kibana --wait --version $(FROM) --set elasticsearchHosts="http://$(ES_CLUSTER)-master:9200"

upgrade-es:
	helm upgrade $(ES_RELEASE) ../../../elasticsearch/ --wait --set clusterName=$(ES_CLUSTER) --set updateStrategy=OnDelete
	# Rollout ES pods
	kubectl delete pod --selector=app=$(ES_CLUSTER)-master

upgrade-kb:
	helm upgrade $(RELEASE) ../../ --wait --values values.yaml
	kubectl rollout status deployment $(RELEASE)-kibana

install: repo install-es install-kb upgrade-es upgrade-kb

test: install goss

purge:
	helm delete $(RELEASE)
	helm delete $(ES_RELEASE)
	kubectl delete $$(kubectl get pvc -o name | grep $(ES_CLUSTER))
