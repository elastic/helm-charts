# OSS

This example deploy Metricbeat 6.8.23-SNAPSHOT using [Metricbeat OSS][] version.


## Usage

* Deploy [Elasticsearch Helm chart][].

* Deploy Metricbeat chart with the default values: `make install`

* You can now setup a port forward to query Metricbeat indices:

  ```
  kubectl port-forward svc/oss-master 9200
  curl localhost:9200/_cat/indices
  ```


## Testing

You can also run [goss integration tests][] using `make test`


[metricbeat oss]: https://www.elastic.co/downloads/beats/metricbeat-oss
[elasticsearch helm chart]: https://github.com/elastic/helm-charts/tree/6.8/elasticsearch/examples/oss/
[goss integration tests]: https://github.com/elastic/helm-charts/tree/6.8/metricbeat/examples/oss/test/goss.yaml
