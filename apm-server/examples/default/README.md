# Default

This example deploy APM Server 8.0.0-SNAPSHOT using [default values][].


## Usage

* Deploy [Elasticsearch Helm chart][].

* Deploy APM Server chart with the default values: `make install`

* You can now setup a port forward to query APM indices:

  ```
  kubectl port-forward svc/elasticsearch-master 9200
  curl localhost:9200/_cat/indices
  ```


## Testing

You can also run [goss integration tests][] using `make test`


[elasticsearch helm chart]: https://github.com/elastic/helm-charts/tree/master/elasticsearch/examples/default/
[goss integration tests]: https://github.com/elastic/helm-charts/tree/master/apm-server/examples/default/test/goss.yaml
[default values]: https://github.com/elastic/helm-charts/tree/master/apm-server/values.yaml
