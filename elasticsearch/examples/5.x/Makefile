
default: test

RELEASE := helm-es-fivex

install:
	helm upgrade --wait --timeout=600 --install $(RELEASE) --values ./values.yaml ../../ ; \

restart:
	helm upgrade --set terminationGracePeriod=121 --wait --timeout=600 --install $(RELEASE) ../../ ; \

purge:
	helm del --purge $(RELEASE)

secrets:
	kubectl delete secrets elastic-fivex-credentials || true
	kubectl create secret generic elastic-fivex-credentials --from-literal=password=changeme --from-literal=username=elastic

health:
	kubectl exec -ti $$(kubectl get pods -l release=$(RELEASE) -o name | awk -F'/' '{ print $$NF }' | shuf -n 1) -- curl --fail -u elastic:changeme -k 'http://localhost:9200/'

test: secrets install health
