# Elasticsearch

This example deploy Logstash 6.8.23-SNAPSHOT which connects to Elasticsearch (see
[values][]).


## Usage

* Deploy [Elasticsearch Helm chart][].

* Deploy Logstash chart: `make install`

* You can now setup a port forward to query Logstash indices:

  ```
  kubectl port-forward svc/elasticsearch-master 9200
  curl localhost:9200/_cat/indices
  ```


## Testing

You can also run [goss integration tests][] using `make test`


[elasticsearch helm chart]: https://github.com/elastic/helm-charts/tree/6.8/elasticsearch/examples/default/
[goss integration tests]: https://github.com/elastic/helm-charts/tree/6.8/logstash/examples/elasticsearch/test/goss.yaml
[values]: https://github.com/elastic/helm-charts/tree/6.8/logstash/examples/elasticsearch/values.yaml
