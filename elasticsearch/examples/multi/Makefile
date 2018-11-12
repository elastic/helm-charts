
default: test

RELEASE := helm-es-multi

install:
	helm upgrade --wait --timeout=600 --install --values ./master.yml $(RELEASE)-master ../../
	helm upgrade --wait --timeout=600 --install --values ./data.yml $(RELEASE)-data ../../

test: install
	helm test $(RELEASE)-master
	helm test $(RELEASE)-data

purge:
	helm del --purge $(RELEASE)-master
	helm del --purge $(RELEASE)-data
