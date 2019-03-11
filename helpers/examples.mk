GOSS_VERSION := v0.3.6

goss:
	GOSS_CONTAINER=$$(kubectl get pods -l release=$(RELEASE) -o name | awk -F'/' 'NR==1{ print $$NF }') && \
	echo Testing with pod: $$GOSS_CONTAINER && \
	kubectl cp test/*.yaml $$GOSS_CONTAINER:/tmp/goss.yaml && \
	kubectl exec $$GOSS_CONTAINER -- sh -c "cd /tmp/ && curl -s -L https://github.com/aelsabbahy/goss/releases/download/$(GOSS_VERSION)/goss-linux-amd64 -o goss && chmod +rx ./goss && ./goss validate --retry-timeout 30s --sleep 5s --color --format documentation"

