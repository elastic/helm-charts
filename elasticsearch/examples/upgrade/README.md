# Upgrade

This example deploy a 3 nodes Elasticsearch cluster using [7.0.0-alpha1][] chart
version, then upgrade it to 7.6.2 version.


## Usage

Running `make install` command will do both 7.0.0-alpha1 install and 7.6.2
upgrade


## Testing

You can also run [goss integration tests][] using `make test`


[7.0.0-alpha1]: https://github.com/elastic/helm-charts/releases/tag/7.0.0-alpha1
[goss integration tests]: https://github.com/elastic/helm-charts/tree/master/elasticsearch/examples/upgrade/test/goss.yaml
