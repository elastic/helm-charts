default: test

include ../../../helpers/examples.mk

RELEASE := helm-es-upgrade

install:
	./scripts/upgrade.sh --release $(RELEASE)

test: install goss

purge:
	helm del $(RELEASE)
