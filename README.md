# Elastic Stack Kubernetes Helm Charts

[![Build Status](https://img.shields.io/jenkins/s/https/devops-ci.elastic.co/job/elastic+helm-charts+6.8.svg)](https://devops-ci.elastic.co/job/elastic+helm-charts+6.8/) [![Artifact HUB](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/elastic)](https://artifacthub.io/packages/search?repo=elastic)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Charts](#charts)
- [Supported Configurations](#supported-configurations)
  - [Stack Versions](#stack-versions)
  - [Kubernetes Versions](#kubernetes-versions)
  - [Helm Versions](#helm-versions)
- [ECK](#eck)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Charts

These Helm charts are designed to be a lightweight way to configure Elastic
official Docker images.

## Supported Configurations

We recommend that the Helm chart version is aligned to the version of the
product you want to deploy. This will ensure that you are using a chart version
that has been tested against the corresponding production version.
This will also ensure that the documentation and examples for the chart will
work with the version of the product, you are installing.

For example, if you want to deploy an Elasticsearch `7.7.1` cluster, use the
corresponding `7.7.1` [tag][elasticsearch-771].

The `master` version of these charts is intended to support the latest
pre-release versions of our products, and therefore may or may not work with
current released versions.
Note that only the released charts coming from [Elastic Helm repo][] or
[GitHub releases][] are supported.


### Stack Versions

Look at [Stack Versions table on master branch][stack-versions-master].

### Kubernetes Versions

The charts are [currently tested][] against all GKE versions available. The
exact versions are defined under `KUBERNETES_VERSIONS` in
[helpers/matrix.yml][].

### Helm Versions

While we are checking backward compatibility, the charts are only tested with
Helm version mentioned in [helm-tester Dockerfile][] (currently 3.6.2).


## ECK

In addition to these Helm charts, Elastic also provides
[Elastic Cloud on Kubernetes][] which is based on [Operator pattern][] and is
Elastic recommended way to deploy Elasticsearch, Kibana, and APM Server on
Kubernetes. There is a dedicated Helm chart for ECK which can be found
[in ECK repo][eck-chart] ([documentation][eck-chart-doc]).


[currently tested]: https://devops-ci.elastic.co/job/elastic+helm-charts+6.8/
[eck-chart]: https://github.com/elastic/cloud-on-k8s/tree/master/deploy
[eck-chart-doc]: https://www.elastic.co/guide/en/cloud-on-k8s/current/k8s-install-helm.html
[elastic cloud on kubernetes]: https://github.com/elastic/cloud-on-k8s
[elastic helm repo]: https://helm.elastic.co
[elasticsearch-771]: https://github.com/elastic/helm-charts/tree/7.7.1/elasticsearch/
[github releases]: https://github.com/elastic/helm-charts/releases
[helm-tester Dockerfile]: https://github.com/elastic/helm-charts/blob/6.8/helpers/helm-tester/Dockerfile
[helpers/matrix.yml]: https://github.com/elastic/helm-charts/blob/6.8/helpers/matrix.yml
[operator pattern]: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
[stack-versions-master]: https://github.com/elastic/helm-charts/blob/master/README.md#stack-versions
