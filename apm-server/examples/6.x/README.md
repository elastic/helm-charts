# 6.x

This example deploy APM Server 6.8.8.


## Usage

* Deploy [Elasticsearch Helm chart][].

* Deploy APM Server chart with the default values: `make install`

* You can now setup a port forward to query APM indices:

  ```
  kubectl port-forward svc/six-master 9200
  curl localhost:9200/_cat/indices
  ```


## Testing

You can also run [goss integration tests][] using `make test`


[elasticsearch helm chart]: https://github.com/elastic/helm-charts/tree/master/elasticsearch/examples/6.x/
[goss integration tests]: https://github.com/elastic/helm-charts/tree/master/apm-server/examples/6.x/test/goss.yaml
