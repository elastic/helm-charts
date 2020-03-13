default: test
include ../../../helpers/examples.mk

RELEASE := kibana

template:
	helm template --values ./values.yml ../../

install: 
	helm upgrade --wait --timeout=600s --install --values ./values.yml $(RELEASE) ../../

test: install goss
	
purge:
	helm del $(RELEASE)
