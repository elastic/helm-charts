
default: install

RELEASE := helm-kibana-security

install:
	helm upgrade --wait --timeout=600 --install --values ./security.yml $(RELEASE) ../../ ; \
	
purge:
	helm del --purge $(RELEASE)
