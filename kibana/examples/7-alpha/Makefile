
default: test

RELEASE := helm-kibana-seven

install:
	helm upgrade --wait --timeout=600 --install --values ./values.yml $(RELEASE) ../../ ; \
	
purge:
	helm del --purge $(RELEASE)

health:
	kubectl exec -ti $$(kubectl get pods -l release=$(RELEASE) -o name | awk -F'/' '{ print $$NF }' | shuf -n 1) -- curl --fail -I 'http://localhost:5601/app/kibana'

test: install health
