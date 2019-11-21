GOSS_VERSION := v0.3.6
GOSS_FILE ?= goss.yaml
GOSS_SELECTOR ?= release=$(RELEASE)
STACK_VERSION := 7.4.1

goss:
	GOSS_CONTAINER=$$(kubectl get --no-headers=true pods -l $(GOSS_SELECTOR) -o custom-columns=:metadata.name | sed -n 1p ) && \
	echo Testing with pod: $$GOSS_CONTAINER && \
	kubectl cp test/$(GOSS_FILE) $$GOSS_CONTAINER:/tmp/$(GOSS_FILE) && \
	kubectl exec $$GOSS_CONTAINER -- sh -c "cd /tmp/ && curl -s -L https://github.com/aelsabbahy/goss/releases/download/$(GOSS_VERSION)/goss-linux-amd64 -o goss && chmod +rx ./goss && ./goss --gossfile $(GOSS_FILE) validate --retry-timeout 300s --sleep 5s --color --format documentation"

