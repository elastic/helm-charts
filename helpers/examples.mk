GOSS_VERSION := v0.3.6

goss:
	kubectl cp test/*.yaml $(GOSS_CONTAINER):/tmp/goss.yaml
	kubectl exec $(GOSS_CONTAINER) -- sh -c "cd /tmp/ && curl -s -L https://github.com/aelsabbahy/goss/releases/download/$(GOSS_VERSION)/goss-linux-amd64 -o /usr/local/bin/goss && chmod +rx /usr/local/bin/goss && goss validate --color --format documentation"

