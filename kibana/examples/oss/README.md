# OSS

This example deploy Kibana 6.8.23-SNAPSHOT using [Kibana OSS][] version.


## Usage

* Deploy [Elasticsearch Helm chart][].

* Deploy Kibana chart with the default values: `make install`

* You can now setup a port forward to query Kibana indices:

  ```
  kubectl port-forward svc/oss-master 9200
  curl localhost:9200/_cat/indices
  ```


## Testing

You can also run [goss integration tests][] using `make test`


[kibana oss]: https://www.elastic.co/downloads/kibana-oss
[elasticsearch helm chart]: https://github.com/elastic/helm-charts/tree/6.8/elasticsearch/examples/oss/
[goss integration tests]: https://github.com/elastic/helm-charts/tree/6.8/kibana/examples/oss/test/goss.yaml
