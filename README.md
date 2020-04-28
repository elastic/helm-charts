# Elastic Stack Kubernetes Helm Charts

[![Build Status](https://img.shields.io/jenkins/s/https/devops-ci.elastic.co/job/elastic+helm-charts+7.7.svg)](https://devops-ci.elastic.co/job/elastic+helm-charts+7.7/)

This functionality is in beta and is subject to change. The design and code is
less mature than official GA features and is being provided as-is with no
warranties. Beta features are not subject to the support SLA of official GA
features.

## Charts

Please look in the chart directories for the documentation for each chart. These
Helm charts are designed to be a lightweight way to configure our official
Docker images. Links to the relevant Docker image documentation has also been
added below.

| Chart                                      | Docker documentation                                                            |
|--------------------------------------------|---------------------------------------------------------------------------------|
| [APM-Server](./apm-server/README.md)       | https://www.elastic.co/guide/en/apm/server/current/running-on-docker.html       |
| [Elasticsearch](./elasticsearch/README.md) | https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html     |
| [Filebeat](./filebeat/README.md)           | https://www.elastic.co/guide/en/beats/filebeat/current/running-on-docker.html   |
| [Kibana](./kibana/README.md)               | https://www.elastic.co/guide/en/kibana/current/docker.html                      |
| [Logstash](./logstash/README.md)           | https://www.elastic.co/guide/en/logstash/current/docker.html                    |
| [Metricbeat](./metricbeat/README.md)       | https://www.elastic.co/guide/en/beats/metricbeat/current/running-on-docker.html |

## Kubernetes Versions

The charts are [currently tested][] against all GKE versions available. The
exact versions are defined under `KUBERNETES_VERSIONS` in
[helpers/matrix.yml][].

## Helm versions

While we are checking backward compatibility, the charts are only tested with
Helm version mentioned in [helm-tester Dockerfile][] (currently 2.16.6).
Note that we don't support [Helm 3][] version.

[currently tested]: https://devops-ci.elastic.co/job/elastic+helm-charts+7.7/
[helm 3]: https://v3.helm.sh
[helm-tester Dockerfile]: https://github.com/elastic/helm-charts/blob/7.7/helpers/helm-tester/Dockerfile
[helpers/matrix.yml]: https://github.com/elastic/helm-charts/blob/7.7/helpers/matrix.yml
