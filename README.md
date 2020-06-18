# Elastic Stack Kubernetes Helm Charts

[![Build Status](https://img.shields.io/jenkins/s/https/devops-ci.elastic.co/job/elastic+helm-charts+7.8.svg)](https://devops-ci.elastic.co/job/elastic+helm-charts+7.8/)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Charts](#charts)
- [Supported Configurations](#supported-configurations)
  - [Support Matrix](#support-matrix)
  - [Kubernetes Versions](#kubernetes-versions)
  - [Helm versions](#helm-versions)
- [ECK](#eck)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Charts

Please look in the chart directories for the documentation for each chart. These
Helm charts are designed to be a lightweight way to configure our official
Docker images. Links to the relevant Docker image documentation has also been
added below.

| Chart                                      | Docker documentation                                                            |
|--------------------------------------------|---------------------------------------------------------------------------------|
| [APM-Server](./apm-server/README.md)       | https://www.elastic.co/guide/en/apm/server/7.8/running-on-docker.html       |
| [Elasticsearch](./elasticsearch/README.md) | https://www.elastic.co/guide/en/elasticsearch/reference/7.8/docker.html     |
| [Filebeat](./filebeat/README.md)           | https://www.elastic.co/guide/en/beats/filebeat/7.8/running-on-docker.html   |
| [Kibana](./kibana/README.md)               | https://www.elastic.co/guide/en/kibana/7.8/docker.html                      |
| [Logstash](./logstash/README.md)           | https://www.elastic.co/guide/en/logstash/7.8/docker.html                    |
| [Metricbeat](./metricbeat/README.md)       | https://www.elastic.co/guide/en/beats/metricbeat/7.8/running-on-docker.html |

## Supported Configurations

Starting with 7.7.0 release, some charts are reaching GA.

Note that only the released charts coming from [Elastic Helm repo][] or
[GitHub releases][] are supported.

### Support Matrix

|     | Elasticsearch | Kibana | Logstash | Filebeat | Metricbeat | APM Server |
|-----|---------------|--------|----------|----------|------------|------------|
| 7.0 | Alpha         | Alpha  | /        | /        | /          | /          |
| 7.1 | Beta          | Beta   | /        | Beta     | /          | /          |
| 7.2 | Beta          | Beta   | /        | Beta     | Beta       | /          |
| 7.3 | Beta          | Beta   | /        | Beta     | Beta       | /          |
| 7.4 | Beta          | Beta   | /        | Beta     | Beta       | /          |
| 7.5 | Beta          | Beta   | Beta     | Beta     | Beta       | Alpha      |
| 7.6 | Beta          | Beta   | Beta     | Beta     | Beta       | Alpha      |
| 7.7 | GA            | GA     | Beta     | GA       | GA         | Beta       |
| 7.8 | GA            | GA     | Beta     | GA       | GA         | Beta       |

### Kubernetes Versions

The charts are [currently tested][] against all GKE versions available. The
exact versions are defined under `KUBERNETES_VERSIONS` in
[helpers/matrix.yml][].

### Helm versions

While we are checking backward compatibility, the charts are only tested with
Helm version mentioned in [helm-tester Dockerfile][] (currently 2.16.9).
Note that we don't support [Helm 3][] version.

## ECK

In addition of these Helm charts, Elastic also provides
[Elastic Cloud on Kubernetes][] which is based on [Operator pattern][] and is
Elastic recommended way to deploy Elasticsearch, Kibana and APM Server on
Kubernetes.


[currently tested]: https://devops-ci.elastic.co/job/elastic+helm-charts+7.8/
[elastic cloud on kubernetes]: https://github.com/elastic/cloud-on-k8s
[elastic helm repo]: https://helm.elastic.co
[github releases]: https://github.com/elastic/helm-charts/releases
[helm 3]: https://v3.helm.sh
[helm-tester Dockerfile]: https://github.com/elastic/helm-charts/blob/7.8/helpers/helm-tester/Dockerfile
[helpers/matrix.yml]: https://github.com/elastic/helm-charts/blob/7.8/helpers/matrix.yml
[operator pattern]: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
