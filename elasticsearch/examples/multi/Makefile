default: test

include ../../../helpers/examples.mk

PREFIX := helm-es-multi
RELEASE := helm-es-multi-master

install:
	helm upgrade --wait --timeout=600 --install --values ./master.yml $(PREFIX)-master ../../
	helm upgrade --wait --timeout=600 --install --values ./data.yml $(PREFIX)-data ../../

test: install goss

purge:
	helm del $(PREFIX)-master
	helm del $(PREFIX)-data
