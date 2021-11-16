# Upgrade

This example will deploy APM Server chart using an old chart version,
then upgrade it.


## Usage

* Add the Elastic Helm charts repo: `helm repo add elastic https://helm.elastic.co`

* Deploy [Elasticsearch Helm chart][]: `helm install elasticsearch elastic/elasticsearch`

* Deploy and upgrade APM Server chart with the default values: `make install`


## Testing

You can also run [goss integration tests][] using `make test`.


[goss integration tests]: https://github.com/elastic/helm-charts/tree/main/apm-server/examples/upgrade/test/goss.yaml
