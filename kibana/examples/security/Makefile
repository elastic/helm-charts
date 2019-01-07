default: test
include ../../../helpers/examples.mk

RELEASE := helm-kibana-security

install: secrets
	helm upgrade --wait --timeout=600 --install --values ./security.yml $(RELEASE) ../../ ; \

test: install goss
	
purge:
	helm del --purge $(RELEASE)

secrets:
	kubectl delete secret kibana-certificates || true
	vault read -field=kibana.crt secret/devops-ci/helm-charts/kibana/security/certificates | base64 --decode > kibana.crt
	vault read -field=kibana.key secret/devops-ci/helm-charts/kibana/security/certificates | base64 --decode > kibana.key
	kubectl create secret generic kibana-certificates --from-file=kibana.crt --from-file=kibana.key && \
	rm -f kibana.crt kibana.key

