# OSS

This example deploy APM Server 7.17.3 using [APM Server OSS][] version.


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


[apm server oss]: https://www.elastic.co/downloads/apm-oss
[elasticsearch helm chart]: https://github.com/elastic/helm-charts/tree/7.17/elasticsearch/examples/default/
[goss integration tests]: https://github.com/elastic/helm-charts/tree/7.17/apm-server/examples/oss/test/goss.yaml
