# Default

This example deploy Kibana 8.5.1 using [default values][].


## Usage

* Deploy [Elasticsearch Helm chart][].

* Deploy Kibana chart with the default values: `make install`

* You can now retrieve the `elastic` user password and setup a port forward to connect Kibana:

  ```
  # Get elastic user password:
  kubectl get secrets --namespace=default elasticsearch-master-credentials -ojsonpath='{.data.password}' | base64 -d
  # Setup port forward
  kubectl port-forward svc/helm-kibana-default-kibana 5601
  ```


## Testing

You can also run [goss integration tests][] using `make test`


[elasticsearch helm chart]: https://github.com/elastic/helm-charts/tree/main/elasticsearch/examples/default/
[goss integration tests]: https://github.com/elastic/helm-charts/tree/main/kibana/examples/default/test/goss.yaml
[default values]: https://github.com/elastic/helm-charts/tree/main/kibana/values.yaml
