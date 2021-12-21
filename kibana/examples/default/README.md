# Default

This example deploy Kibana 6.8.23-SNAPSHOT using [default values][].


## Usage

* Deploy [Elasticsearch Helm chart][].

* Deploy Kibana chart with the default values: `make install`

* You can now setup a port forward to query Kibana indices:

  ```
  kubectl port-forward svc/elasticsearch-master 9200
  curl localhost:9200/_cat/indices
  ```


## Testing

You can also run [goss integration tests][] using `make test`


[elasticsearch helm chart]: https://github.com/elastic/helm-charts/tree/6.8/elasticsearch/examples/default/
[goss integration tests]: https://github.com/elastic/helm-charts/tree/6.8/kibana/examples/default/test/goss.yaml
[default values]: https://github.com/elastic/helm-charts/tree/6.8/kibana/values.yaml
