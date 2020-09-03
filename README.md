# Elastic Stack Kubernetes Helm Charts

[![Build Status](https://img.shields.io/jenkins/s/https/devops-ci.elastic.co/job/elastic+helm-charts+7.9.svg)](https://devops-ci.elastic.co/job/elastic+helm-charts+7.9/)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Charts](#charts)
- [Supported Configurations](#supported-configurations)
  - [Support Matrix](#support-matrix)
  - [Kubernetes Versions](#kubernetes-versions)
  - [Helm versions](#helm-versions)
    - [Helm 3 beta](#helm-3-beta)
- [ECK](#eck)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Charts

These Helm charts are designed to be a lightweight way to configure our official
Docker images. Links to the relevant Docker image documentation has also been
added below.

We recommend that the Helm chart version is aligned to the version of the product
you want to deploy. This will ensure that you using a chart version that has been
tested against the corresponding production version.
This will also ensure that the documentation and examples for the chart will work
with the version of the product you are installing.

For example if you want to deploy an Elasticsearch `7.7.1` cluster, use the
corresponding `7.7.1` [tag][elasticsearch-771].

The `master` version of these charts are intended to support the latest pre-release
versions of our products, and therefore may or may not work with current released
versions.

| Chart                                      | Docker documentation                                                        | Latest 7 Version           | Latest 6 Version            |
|--------------------------------------------|-----------------------------------------------------------------------------|----------------------------|-----------------------------|
| [APM-Server](./apm-server/README.md)       | https://www.elastic.co/guide/en/apm/server/7.9/running-on-docker.html       | [`7.9.1`][apm-7]           | [`6.8.12`][apm-6]           |
| [Elasticsearch](./elasticsearch/README.md) | https://www.elastic.co/guide/en/elasticsearch/reference/7.9/docker.html     | [`7.9.1`][elasticsearch-7] | [`6.8.12`][elasticsearch-6] |
| [Filebeat](./filebeat/README.md)           | https://www.elastic.co/guide/en/beats/filebeat/7.9/running-on-docker.html   | [`7.9.1`][filebeat-7]      | [`6.8.12`][filebeat-6]      |
| [Kibana](./kibana/README.md)               | https://www.elastic.co/guide/en/kibana/7.9/docker.html                      | [`7.9.1`][kibana-7]        | [`6.8.12`][kibana-6]        |
| [Logstash](./logstash/README.md)           | https://www.elastic.co/guide/en/logstash/7.9/docker.html                    | [`7.9.1`][logstash-7]      | [`6.8.12`][logstash-6]      |
| [Metricbeat](./metricbeat/README.md)       | https://www.elastic.co/guide/en/beats/metricbeat/7.9/running-on-docker.html | [`7.9.1`][metricbeat-7]    | [`6.8.12`][metricbeat-6]    |

## Supported Configurations

Starting with the `7.7.0` release, some charts are reaching GA.

Note that only the released charts coming from [Elastic Helm repo][] or
[GitHub releases][] are supported.

### Support Matrix

|     | Elasticsearch | Kibana | Logstash | Filebeat | Metricbeat | APM Server |
|-----|---------------|--------|----------|----------|------------|------------|
| 6.8 | Beta          | Beta   | Beta     | Beta     | Beta       | Alpha      |
| 7.0 | Alpha         | Alpha  | /        | /        | /          | /          |
| 7.1 | Beta          | Beta   | /        | Beta     | /          | /          |
| 7.2 | Beta          | Beta   | /        | Beta     | Beta       | /          |
| 7.3 | Beta          | Beta   | /        | Beta     | Beta       | /          |
| 7.4 | Beta          | Beta   | /        | Beta     | Beta       | /          |
| 7.5 | Beta          | Beta   | Beta     | Beta     | Beta       | Alpha      |
| 7.6 | Beta          | Beta   | Beta     | Beta     | Beta       | Alpha      |
| 7.7 | GA            | GA     | Beta     | GA       | GA         | Beta       |
| 7.8 | GA            | GA     | Beta     | GA       | GA         | Beta       |
| 7.9 | GA            | GA     | Beta     | GA       | GA         | Beta       |

### Kubernetes Versions

The charts are [currently tested][] against all GKE versions available. The
exact versions are defined under `KUBERNETES_VERSIONS` in
[helpers/matrix.yml][].

### Helm versions

While we are checking backward compatibility, the charts are only tested with
Helm version mentioned in [helm-tester Dockerfile][] (currently 2.16.10).

#### Helm 3 beta

While we don't have automated tests for [Helm 3][] yet, we fixed the main
blockers to use it. We now have enough feedbacks from internal and external
users to add support in beta.

## ECK

In addition of these Helm charts, Elastic also provides
[Elastic Cloud on Kubernetes][] which is based on [Operator pattern][] and is
Elastic recommended way to deploy Elasticsearch, Kibana and APM Server on
Kubernetes.


[currently tested]: https://devops-ci.elastic.co/job/elastic+helm-charts+7.9/
[elastic cloud on kubernetes]: https://github.com/elastic/cloud-on-k8s
[elastic helm repo]: https://helm.elastic.co
[github releases]: https://github.com/elastic/helm-charts/releases
[helm 3]: https://v3.helm.sh
[helm-tester Dockerfile]: https://github.com/elastic/helm-charts/blob/7.9/helpers/helm-tester/Dockerfile
[helpers/matrix.yml]: https://github.com/elastic/helm-charts/blob/7.9/helpers/matrix.yml
[operator pattern]: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
[elasticsearch-771]: https://github.com/elastic/helm-charts/tree/7.7.1/elasticsearch/

[apm-7]: https://github.com/elastic/helm-charts/tree/7.9.1/apm-server/README.md
[apm-6]: https://github.com/elastic/helm-charts/tree/6.8.12/apm-server/README.md
[elasticsearch-7]: https://github.com/elastic/helm-charts/tree/7.9.1/elasticsearch/README.md
[elasticsearch-6]: https://github.com/elastic/helm-charts/tree/6.8.12/elasticsearch/README.md
[filebeat-7]: https://github.com/elastic/helm-charts/tree/7.9.1/filebeat/README.md
[filebeat-6]: https://github.com/elastic/helm-charts/tree/6.8.12/filebeat/README.md
[kibana-7]: https://github.com/elastic/helm-charts/tree/7.9.1/kibana/README.md
[kibana-6]: https://github.com/elastic/helm-charts/tree/6.8.12/kibana/README.md
[logstash-7]: https://github.com/elastic/helm-charts/tree/7.9.1/logstash/README.md
[logstash-6]: https://github.com/elastic/helm-charts/tree/6.8.12/logstash/README.md
[metricbeat-7]: https://github.com/elastic/helm-charts/tree/7.9.1/metricbeat/README.md
[metricbeat-6]: https://github.com/elastic/helm-charts/tree/6.8.12/metricbeat/README.md
