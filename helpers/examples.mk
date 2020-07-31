GOSS_VERSION := v0.3.6
GOSS_FILE ?= goss.yaml
GOSS_SELECTOR ?= release=$(RELEASE)
STACK_VERSION := 8.0.0-SNAPSHOT

.PHONY: help
help: ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

.PHONY: goss
goss: ## Run goss tests
	GOSS_CONTAINER=$$(kubectl get --no-headers=true pods -l $(GOSS_SELECTOR) -o custom-columns=:metadata.name | sed -n 1p ) && \
	echo Testing with pod: $$GOSS_CONTAINER && \
	kubectl cp test/$(GOSS_FILE) $$GOSS_CONTAINER:/tmp/$(GOSS_FILE) && \
	kubectl exec $$GOSS_CONTAINER -- sh -c "cd /tmp/ && curl -s -L https://github.com/aelsabbahy/goss/releases/download/$(GOSS_VERSION)/goss-linux-amd64 -o goss && chmod +rx ./goss && ./goss --gossfile $(GOSS_FILE) validate --retry-timeout 300s --sleep 5s --color --format documentation"
