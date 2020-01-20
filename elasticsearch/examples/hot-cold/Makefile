default: test

include ../../../helpers/examples.mk

RELEASE := helm-es-hot-cold

install:
	helm init --client-only
	helm dependency update
	helm upgrade --wait --timeout=600 --install $(RELEASE) .

test: install goss

purge:
	helm del --purge $(RELEASE)
