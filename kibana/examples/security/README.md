# Security

This example deploy Kibana 8.5.1 using authentication and TLS to connect to
Elasticsearch (see [values][]).


## Usage

* Deploy [Elasticsearch Helm chart][].

* Deploy Kibana chart with security: `make secrets install`

* You can now retrieve the `elastic` user password and setup a port forward to connect Kibana:

  ```
  # Get elastic user password:
  kubectl get secrets --namespace=default security-master-credentials -ojsonpath='{.data.password}' | base64 -d
  # Setup port forward
  kubectl port-forward svc/helm-kibana-security-kibana 5601
  ```


## Testing

You can also run [goss integration tests][] using `make test`


[elasticsearch helm chart]: https://github.com/elastic/helm-charts/tree/main/elasticsearch/examples/security/
[goss integration tests]: https://github.com/elastic/helm-charts/tree/main/kibana/examples/security/test/goss.yaml
[values]: https://github.com/elastic/helm-charts/tree/main/kibana/examples/security/values.yaml
