default: test

include ../../../helpers/examples.mk

PREFIX := helm-es-multi
RELEASE := helm-es-multi-master

install:
	helm init --client-only
	helm dep update
	helm upgrade --wait --timeout=600 --install $(RELEASE) .

test: install goss

purge:
	helm del --purge $(RELEASE)
