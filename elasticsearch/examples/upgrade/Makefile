default: test

include ../../../helpers/examples.mk

RELEASE := helm-es-upgrade

install:
	./scripts/upgrade.sh --release $(RELEASE)

init:
	helm init --client-only

test: init install goss

purge:
	helm del --purge $(RELEASE)
