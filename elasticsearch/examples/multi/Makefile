default: test

include ../../../helpers/examples.mk

RELEASE := helm-es-multi

GOSS_CONTAINER := multi-master-0

install:
	helm upgrade --wait --timeout=600 --install --values ./master.yml $(RELEASE)-master ../../
	helm upgrade --wait --timeout=600 --install --values ./data.yml $(RELEASE)-data ../../

test: install goss

purge:
	helm del --purge $(RELEASE)-master
	helm del --purge $(RELEASE)-data
