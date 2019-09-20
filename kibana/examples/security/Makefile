default: test
include ../../../helpers/examples.mk

RELEASE := helm-kibana-security

install:
	helm upgrade --wait --timeout=600 --install --values ./security.yml $(RELEASE) ../../

test: secrets install goss

purge:
	kubectl delete secret kibana || true
	helm del --purge $(RELEASE)

secrets:
	encryptionkey=$$(echo $$(docker run --rm docker.elastic.co/elasticsearch/elasticsearch:$(STACK_VERSION) /bin/sh -c "< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c50")) && \
	kubectl create secret generic kibana --from-literal=encryptionkey=$$encryptionkey
