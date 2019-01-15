default: test

include ../../../helpers/examples.mk

RELEASE := helm-es-security

install:
	# This starts a command in the background to install the license once the cluster has formed
	until kubectl exec -ti security-master-0 -- curl --fail -k -XPUT 'https://security-master-headless:9200/_xpack/license' -H "Content-Type: application/json" -d @/usr/share/elasticsearch/config/license/license.json > /dev/null 2>&1 ; do sleep 5; done & \
	helm upgrade --wait --timeout=600 --install --values ./security.yml $(RELEASE) ../../ ; \
	
purge:
	helm del --purge $(RELEASE)

license:
	kubectl exec -ti security-master-0 -- curl --fail -k -XPUT 'https://security-master-headless:9200/_xpack/license' -H "Content-Type: application/json" -d @/usr/share/elasticsearch/config/license/license.json
	
test: secrets install goss

secrets:
	kubectl delete secrets elastic-credentials elastic-license elastic-certificates elastic-certificate-pem || true && \
	vault read -field=value secret/devops-ci/helm-charts/elasticsearch/security/license > license.json && \
	vault read -field=value secret/devops-ci/helm-charts/elasticsearch/security/certificates | base64 --decode > elastic-certificates.p12 && \
	vault read -field=value secret/devops-ci/helm-charts/elasticsearch/security/certificate-pem | base64 --decode > elastic-certificate.pem && \
	kubectl create secret generic elastic-credentials  --from-literal=password=changeme --from-literal=username=elastic && \
	kubectl create secret generic elastic-license --from-file=license.json && \
	kubectl create secret generic elastic-certificates --from-file=elastic-certificates.p12 && \
	kubectl create secret generic elastic-certificate-pem --from-file=elastic-certificate.pem && \
	rm -f license.json elastic-certificates.p12 elastic-certificate.pem
