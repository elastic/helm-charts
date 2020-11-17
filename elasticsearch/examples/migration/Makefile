PREFIX := helm-es-migration

data:
	helm upgrade --wait --timeout=900s --install --values ./data.yml $(PREFIX)-data ../../

master:
	helm upgrade --wait --timeout=900s --install --values ./master.yml $(PREFIX)-master ../../

client:
	helm upgrade --wait --timeout=900s --install --values ./client.yml $(PREFIX)-client ../../
