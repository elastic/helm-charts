# The name of the thing you are deploying. This setting affects the name of
# the k8s resources.
project := secure

# The kubernetes namespace to use.
namespace := default

# The kubectl config to use.
k8s := $(shell kubectl config current-context)

# Where to write temporary files.
workdir := $(shell mktemp -d)

.PHONY: prepare
prepare:
	-rm ../secure-elasticsearch/charts/*.tgz
	helm dep build ../secure-elasticsearch/
	helm dep update

# Initial deployment and ugprading
.PHONY: deploy
deploy:
	@$(MAKE) confirm warning='This will create or updgrade an Elasticsearch cluster and deploy the helm release'
	helm upgrade --namespace $(namespace) --install $(project) .

# Pop reference: http://hyperboleandahalf.blogspot.com/2010/06/this-is-why-ill-never-be-adult.html
# This task removes all non-secret kubernetes/helm resources for this chart.
.PHONY: clean-all-the-things
clean-all-the-things:
	@$(MAKE) confirm warning='This will destroy the Elasticsearch cluster and delete the helm release.'
	-helm delete --purge $(project)
	@# Sometimes pvc and pdb resources stick around.
	-kubectl delete pvc --namespace $(namespace) -l app=$(project)-data
	-kubectl delete pvc --namespace $(namespace) -l app=$(project)-master
	-kubectl delete pdb --namespace $(namespace) secure-{data,master}-pdb

# Pop reference: Setec Astronomy - https://en.wikipedia.org/wiki/Sneakers_(1992_film)
# Remove all the secrets.
.PHONY: too-many-secrets
too-many-secrets:
	@$(MAKE) confirm warning='This will delete all secrets associated with this helm chart.'
	-kubectl delete secret --namespace $(namespace) elastic-{credentials,certificates,certificate-pem} kibana-{certificate,encryption-key} nginx-certificate elastic-license

# Generate all required secrets.
.PHONY: secrets
secrets:
	@$(MAKE) confirm warning='This will generate secrets for the Elasticsearch cluster.'
	@$(MAKE) create-secrets

.PHONY: create-secrets
create-secrets: secret.elasticsearch.credentials secret.elasticsearch.ssl 
create-secrets: secret.kibana.encryptionKey secret.kibana.ssl
create-secrets: secret.nginx.ssl
	@echo "Don't forget to create the x-pack license secret:"
	@echo "kubectl create secret --namespace $(namespace) generic elastic-license --from-literal=license='the-license-json-content'"

.PHONY: secret.elasticsearch.credentials
secret.elasticsearch.credentials: password := $(shell pwgen -s 15 1)
secret.elasticsearch.credentials:
	@kubectl create secret --namespace $(namespace) generic elastic-credentials --from-literal=username=elastic --from-literal=password="$(password)"

	@echo =[ Cluster Credentials ]=
	@echo   User: elastic
	@echo   Password: $(password)
	@echo ==========================

.PHONY: secret.elasticsearch.ssl
secret.elasticsearch.ssl: $(workdir)/elastic-certificates.p12 $(workdir)/elastic-certificate.pem
	@kubectl create secret --namespace $(namespace) generic elastic-certificates --from-file="$(workdir)/elastic-certificates.p12"
	@kubectl create secret --namespace $(namespace) generic elastic-certificate-pem --from-file="$(workdir)/elastic-certificate.pem"

.PHONY: secret.kibana.ssl
secret.kibana.ssl: $(workdir)/kibana/kibana.crt $(workdir)/kibana/kibana.key
	@kubectl create secret --namespace $(namespace) generic kibana-certificate --from-file="$(workdir)/kibana/"

$(workdir)/kibana:
	@mkdir $@

.INTERMEDIATE: $(workdir)/kibana/kibana.crt
$(workdir)/kibana/kibana.crt: $(workdir)/kibana/kibana.key

.INTERMEDIATE: $(workdir)/kibana/kibana.key
$(workdir)/kibana/kibana.key: $(workdir)/kibana
	# TODO(sissel): Build a better self-signed certificate which includes SANs
	@openssl req -x509 -batch -nodes -newkey rsa:2048 -keyout $@ -out $(dir $@)/kibana.crt -subj /CN=$(project)-kibana

.PHONY: secret.nginx.ssl
secret.nginx.ssl: $(workdir)/nginx/tls.crt $(workdir)/nginx/tls.key
	@kubectl create secret --namespace $(namespace) generic nginx-certificate --from-file="$(workdir)/nginx/"

$(workdir)/nginx:
	@mkdir $@

.INTERMEDIATE: $(workdir)/nginx/tls.crt
$(workdir)/nginx/tls.crt: $(workdir)/nginx/tls.key

.INTERMEDIATE: $(workdir)/nginx/tls.key
$(workdir)/nginx/tls.key: san := "DNS:es.$(project).dev.inf.elasticnet.co,DNS:kibana.$(project).dev.inf.elasticnet.co"
$(workdir)/nginx/tls.key: $(workdir)/nginx
	@# Newer openssl verisons have a `-addext` for the `req` command, but it's pretty new (2018)
	@# To enable older openssl versions, build our openssl config from the system default plus subjectAltName
	@(cat "$$(openssl version -a |awk '/^OPENSSLDIR: / { print $$2 }' | tr -d '"')/openssl.cnf"; printf "[san]\nsubjectAltName=$(san)") | openssl req -x509 -batch -nodes -newkey rsa:2048 -keyout $@ -out $(dir $@)/tls.crt -config - -extensions san

.INTERMEDIATE: $(workdir)/elastic-certificate.pem
$(workdir)/elastic-certificate.pem: $(workdir)/elastic-certificates.p12
	@openssl pkcs12 -cacerts -nokeys -nodes -passin pass: -in $< | sed -ne '/BEGIN CERTIFICATE/,/END CERTIFICATE/p' > $@

# Generate certificates for the cluster using Elasticsearch's elasticsearch-certutil.
.INTERMEDIATE: $(workdir)/elastic-certificates.p12
$(workdir)/elastic-certificates.p12: owner=$(shell id -u)
$(workdir)/elastic-certificates.p12:
	@echo "Generating Elastic Stack Certificates for TLS"
	@# Running elasticsearch-certutil via docker is a simple way to achieve this.
	@docker run -it -v $(@D):/certs:Z docker.elastic.co/elasticsearch/elasticsearch:6.5.3 elasticsearch-certutil cert \
		--pass "" --out /certs/elastic-certificates.p12 -s --dns $(project)-data,$(project)-data-headless,$(project)-master,$(project)-master-headless,localhost,$(project)-data.default,$(project)-master.default
	@docker run -it -v $(@D):/certs:Z docker.elastic.co/elasticsearch/elasticsearch:6.5.3 chown $(owner) /certs/$(@F)

# Generate a 32-character secrets key for Kibana (xpack.security.encryptionKey)
.PHONY: secret.kibana.encryptionKey
secret.kibana.encryptionKey: key := $(shell dd if=/dev/urandom count=32 bs=1 2> /dev/null | base64 | cut -c 1-32)
secret.kibana.encryptionKey: 
	@kubectl create secret --namespace $(namespace) generic kibana-encryption-key "--from-literal=key=$(key)"

.PHONY: confirm
confirm:
ifndef warning
	$(error 'confirm' invoked without a $$warning message.)
endif
	@echo "!! !! !! !! !! !! !!"
	@echo "$(warning). Are you sure?"
	@echo "Current Kubernetes Cluster: $(k8s)"
	@echo
	@echo -n "Type the full cluster name to confirm> "
	@read c; if [ "$(k8s)" != "$$c" ] ; then echo "Incorrect cluster name given. Cancelling..."; exit 1; fi
