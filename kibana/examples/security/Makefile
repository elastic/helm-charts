default: test
include ../../../helpers/examples.mk

RELEASE := helm-kibana-security

install:
	helm upgrade --wait --timeout=600 --install --values ./security.yml $(RELEASE) ../../ ; \

test: install goss
	
purge:
	helm del --purge $(RELEASE)
