# 6.x

This example deploy a 3 nodes Elasticsearch 6.8.8 cluster.


## Usage

* Deploy Elasticsearch chart with the default values: `make install`

* You can now setup a port forward to query Elasticsearch API:

  ```
  kubectl port-forward svc/six-master 9200
  curl localhost:9200/_cat/indices
  ```


## Testing

You can also run [goss integration tests][] using `make test`


[goss integration tests]: https://github.com/elastic/helm-charts/tree/master/elasticsearch/examples/6.x/test/goss.yaml
