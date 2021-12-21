# Default

This example deploy Metricbeat 6.8.23-SNAPSHOT using [default values][].


## Usage

* Deploy [Elasticsearch Helm chart][].

* Deploy Metricbeat chart with the default values: `make install`

* You can now setup a port forward to query Metricbeat indices:

  ```
  kubectl port-forward svc/elasticsearch-master 9200
  curl localhost:9200/_cat/indices
  ```


## Testing

You can also run [goss integration tests][] using `make test`


[elasticsearch helm chart]: https://github.com/elastic/helm-charts/tree/6.8/elasticsearch/examples/default/
[goss integration tests]: https://github.com/elastic/helm-charts/tree/6.8/metricbeat/examples/default/test/goss.yaml
[default values]: https://github.com/elastic/helm-charts/tree/6.8/metricbeat/values.yaml
