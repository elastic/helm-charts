# OSS

This example deploy a 3 nodes Elasticsearch 8.0.0-SNAPSHOT cluster using
[Elasticsearch OSS][] version.

## Usage

* Deploy Elasticsearch chart with the default values: `make install`

* You can now setup a port forward to query Elasticsearch API:

  ```
  kubectl port-forward svc/oss-master 9200
  curl localhost:9200/_cat/indices
  ```

## Testing

You can also run [goss integration tests][] using `make test`


[elasticsearch oss]: https://www.elastic.co/downloads/elasticsearch-oss
[goss integration tests]: https://github.com/elastic/helm-charts/tree/master/elasticsearch/examples/oss/test/goss.yaml
