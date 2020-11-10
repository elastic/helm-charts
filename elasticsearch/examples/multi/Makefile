default: test

include ../../../helpers/examples.mk

PREFIX := helm-es-multi
RELEASE := helm-es-multi-master

install:
	helm upgrade --wait --timeout=600s --install --values ./master.yml $(PREFIX)-master ../../
	helm upgrade --wait --timeout=600s --install --values ./data.yml $(PREFIX)-data ../../
	helm upgrade --wait --timeout=600s --install --values ./client.yml $(PREFIX)-client ../../

test: install goss

purge:
	helm del $(PREFIX)-master
	helm del $(PREFIX)-data
	helm del $(PREFIX)-client
