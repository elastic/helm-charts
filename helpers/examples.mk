SHELL := /bin/bash
GOSS_VERSION := v0.3.18
GOSS_FILE ?= goss.yaml
GOSS_SELECTOR ?= release=$(RELEASE)
STACK_VERSION := 8.5.1
TIMEOUT := 900s

.PHONY: help
help: ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

.PHONY: goss
goss: ## Run goss tests
	set -e; \
	for i in $$(seq 1 5); do \
		curl -s -L "https://github.com/aelsabbahy/goss/releases/download/$(GOSS_VERSION)/goss-linux-amd64" -o /tmp/goss; \
		if [ -z "$$GOSS_CONTAINER" ]; then \
			sleep 5; \
			echo "Retrieving pod ($$i/5)"; \
			GOSS_CONTAINER=$$(kubectl get --no-headers=true pods -l "$(GOSS_SELECTOR)" -o custom-columns=:metadata.name --field-selector=status.phase=Running --sort-by=.metadata.creationTimestamp | tail -1 ); \
		else \
			echo "Testing with pod: $$GOSS_CONTAINER" && \
			kubectl cp "test/$(GOSS_FILE)" "$$GOSS_CONTAINER:/tmp/$(GOSS_FILE)" && \
			kubectl cp "/tmp/goss" "$$GOSS_CONTAINER:/tmp/goss" && \
			kubectl exec "$$GOSS_CONTAINER" -- sh -c "chmod +rx /tmp/goss && if [ -f ~/.elasticsearch-serviceaccounttoken ]; then . ~/.elasticsearch-serviceaccounttoken; fi; /tmp/goss --gossfile \"/tmp/$(GOSS_FILE)\" validate --retry-timeout 300s --sleep 5s --color --format documentation"; \
			break; \
		fi; \
	done
