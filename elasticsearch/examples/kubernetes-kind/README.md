# KIND

This example deploy a 3 nodes Elasticsearch 7.7.0 cluster on [Kind][]
using [custom values][].

Note that this configuration should be used for test only and isn't recommended
for production.


## Requirements

There is currently an [kind issue][] with mount points created from PVCs not
writable by non-root users. [kubernetes-sigs/kind#1157][] should fix it in a
future release.

Meanwhile, the workaround is to install manually
[Rancher Local Path Provisioner][] and use `local-path` storage class for
Elasticsearch volumes (see [Makefile][] instructions).


## Usage

* Deploy Elasticsearch chart with the default values: `make install`

* You can now setup a port forward to query Elasticsearch API:

  ```
  kubectl port-forward svc/elasticsearch-master 9200
  curl localhost:9200/_cat/indices
  ```


[custom values]: https://github.com/elastic/helm-charts/blob/7.7/elasticsearch/examples/kubernetes-kind/values.yaml
[kind]: https://kind.sigs.k8s.io/
[kind issue]: https://github.com/kubernetes-sigs/kind/issues/830
[kubernetes-sigs/kind#1157]: https://github.com/kubernetes-sigs/kind/pull/1157
[rancher local path provisioner]: https://github.com/rancher/local-path-provisioner
[Makefile]: https://github.com/elastic/helm-charts/blob/7.7/elasticsearch/examples/kubernetes-kind/Makefile#L5
