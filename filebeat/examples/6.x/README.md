# 6.x

This example deploy Filebeat 6.8.10.


## Usage

* Deploy [Elasticsearch Helm chart][].

* Deploy Filebeat chart with the default values: `make install`

* You can now setup a port forward to query Filebeat indices:

  ```
  kubectl port-forward svc/six-master 9200
  curl localhost:9200/_cat/indices
  ```


## Testing

You can also run [goss integration tests][] using `make test`


[elasticsearch helm chart]: https://github.com/elastic/helm-charts/tree/master/elasticsearch/examples/6.x/
[goss integration tests]: https://github.com/elastic/helm-charts/tree/master/filebeat/examples/6.x/test/goss.yaml
