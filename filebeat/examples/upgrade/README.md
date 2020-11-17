# Upgrade

This example will deploy Filebeat chart using an old chart version,
then upgrade it.


## Usage

* Deploy [Elasticsearch Helm chart][].

* Deploy and upgrade Filebeat chart with the default values: `make install`


## Testing

You can also run [goss integration tests][] using `make test`.


[goss integration tests]: https://github.com/elastic/helm-charts/tree/master/filebeat/examples/upgrade/test/goss.yaml
