# Upgrade

This example deploy a 3 nodes Elasticsearch cluster using an old chart version,
then upgrade it to 7.7.0 version.

The following upgrades are tested:
- Upgrade from [7.0.0-alpha1][] version on K8S <1.16
- Upgrade from [7.4.0][] version on K8S >=1.16 (Elasticsearch chart < 7.4.0 are
not compatible with K8S >= 1.16)


## Usage

Running `make install` command will do first install and 7.7.0 upgrade


## Testing

You can also run [goss integration tests][] using `make test`


[7.0.0-alpha1]: https://github.com/elastic/helm-charts/releases/tag/7.0.0-alpha1
[7.4.0]: https://github.com/elastic/helm-charts/releases/tag/7.4.0
[goss integration tests]: https://github.com/elastic/helm-charts/tree/master/elasticsearch/examples/upgrade/test/goss.yaml
