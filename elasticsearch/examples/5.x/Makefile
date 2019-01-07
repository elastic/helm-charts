default: test

include ../../../helpers/examples.mk

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

test: secrets install goss
