# Elastic Stack Kubernetes Helm Charts

[![Build Status](https://img.shields.io/jenkins/s/https/devops-ci.elastic.co/job/elastic+helm-charts+main.svg)](https://devops-ci.elastic.co/job/elastic+helm-charts+main/) [![Artifact HUB](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/elastic)](https://artifacthub.io/packages/search?repo=elastic)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Elastic Stack Kubernetes Helm Charts](#elastic-stack-kubernetes-helm-charts)
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

| Chart                                      | Latest 7 Version                             | Latest 6 Version                   |
|--------------------------------------------|----------------------------------------------|------------------------------------|
| [APM-Server](./apm-server/README.md)       | [`7.16.3`][apm-7] (Beta since 7.7.0)         | [`6.8.22`][apm-6] (Alpha)          |
| [Elasticsearch](./elasticsearch/README.md) | [`7.16.3`][elasticsearch-7] (GA since 7.7.0) | [`6.8.22`][elasticsearch-6] (Beta) |
| [Filebeat](./filebeat/README.md)           | [`7.16.3`][filebeat-7] (GA since 7.7.0)      | [`6.8.22`][filebeat-6] (Beta)      |
| [Kibana](./kibana/README.md)               | [`7.16.3`][kibana-7] (GA since 7.7.0)        | [`6.8.22`][kibana-6] (Beta)        |
| [Logstash](./logstash/README.md)           | [`7.16.3`][logstash-7] (Beta since 7.5.0)    | [`6.8.22`][logstash-6] (Beta)      |
| [Metricbeat](./metricbeat/README.md)       | [`7.16.3`][metricbeat-7] (GA since 7.7.0)    | [`6.8.22`][metricbeat-6] (Beta)    |

### Kubernetes Versions

The charts are [currently tested][] against all GKE versions available. The
exact versions are defined under `KUBERNETES_VERSIONS` in
[helpers/matrix.yml][].

### Helm Versions

While we are checking backward compatibility, the charts are only tested with
Helm version mentioned in [helm-tester Dockerfile][] (currently 3.8.0).


## ECK

In addition to these Helm charts, Elastic also provides
[Elastic Cloud on Kubernetes][] which is based on [Operator pattern][] and is
Elastic recommended way to deploy Elasticsearch, Kibana, and APM Server on
Kubernetes. There is a dedicated Helm chart for ECK which can be found
[in ECK repo][eck-chart] ([documentation][eck-chart-doc]).


[currently tested]: https://devops-ci.elastic.co/job/elastic+helm-charts+main/
[eck-chart]: https://github.com/elastic/cloud-on-k8s/tree/master/deploy
[eck-chart-doc]: https://www.elastic.co/guide/en/cloud-on-k8s/current/k8s-install-helm.html
[elastic cloud on kubernetes]: https://github.com/elastic/cloud-on-k8s
[elastic helm repo]: https://helm.elastic.co
[github releases]: https://github.com/elastic/helm-charts/releases
[helm-tester Dockerfile]: https://github.com/elastic/helm-charts/blob/main/helpers/helm-tester/Dockerfile
[helpers/matrix.yml]: https://github.com/elastic/helm-charts/blob/main/helpers/matrix.yml
[operator pattern]: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
[elasticsearch-771]: https://github.com/elastic/helm-charts/tree/7.7.1/elasticsearch/
[apm-7]: https://github.com/elastic/helm-charts/tree/7.16/apm-server/README.md
[apm-6]: https://github.com/elastic/helm-charts/tree/6.8/apm-server/README.md
[elasticsearch-7]: https://github.com/elastic/helm-charts/tree/7.16/elasticsearch/README.md
[elasticsearch-6]: https://github.com/elastic/helm-charts/tree/6.8/elasticsearch/README.md
[filebeat-7]: https://github.com/elastic/helm-charts/tree/7.16/filebeat/README.md
[filebeat-6]: https://github.com/elastic/helm-charts/tree/6.8/filebeat/README.md
[kibana-7]: https://github.com/elastic/helm-charts/tree/7.16/kibana/README.md
[kibana-6]: https://github.com/elastic/helm-charts/tree/6.8/kibana/README.md
[logstash-7]: https://github.com/elastic/helm-charts/tree/7.16/logstash/README.md
[logstash-6]: https://github.com/elastic/helm-charts/tree/6.8/logstash/README.md
[metricbeat-7]: https://github.com/elastic/helm-charts/tree/7.16/metricbeat/README.md
[metricbeat-6]: https://github.com/elastic/helm-charts/tree/6.8/metricbeat/README.md
