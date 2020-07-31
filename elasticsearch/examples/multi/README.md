# Multi

This example deploy an Elasticsearch 8.0.0-SNAPSHOT cluster composed of 2 different Helm
releases:

- `helm-es-multi-master` for the 3 master nodes using [master values][]
- `helm-es-multi-data` for the 3 data nodes using [data values][]

## Usage

* Deploy the 2 Elasticsearch releases: `make install`

* You can now setup a port forward to query Elasticsearch API:

  ```
  kubectl port-forward svc/multi-master 9200
  curl -u elastic:changeme http://localhost:9200/_cat/indices
  ```

## Testing

You can also run [goss integration tests][] using `make test`


[data values]: https://github.com/elastic/helm-charts/tree/master/elasticsearch/examples/multi/data.yml
[goss integration tests]: https://github.com/elastic/helm-charts/tree/master/elasticsearch/examples/multi/test/goss.yaml
[master values]: https://github.com/elastic/helm-charts/tree/master/elasticsearch/examples/multi/master.yml
