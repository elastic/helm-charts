# Elastic Stack Kubernetes Helm Charts

[![Build Status](https://img.shields.io/jenkins/s/https/devops-ci.elastic.co/job/elastic+helm-charts+master.svg)](https://devops-ci.elastic.co/job/elastic+helm-charts+master/)

This functionality is in beta status and may be changed or removed completely in a future release. Elastic will take a best effort approach to fix any issues, but beta features are not subject to the support SLA of official GA features.

## Charts

Please look in the chart directories for the documentation for each chart. These helm charts are designed to be a lightweight way to configure our official docker images. Links to the relevant docker image documentation has also been added below.

* [Elasticsearch](./elasticsearch/README.md) - [docker image docs](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html)
* [Kibana](./kibana/README.md) - [docker image docs](https://www.elastic.co/guide/en/kibana/current/docker.html)
* [Filebeat](./filebeat/README.md) - [docker image docs](https://www.elastic.co/guide/en/beats/filebeat/current/running-on-docker.html)

## Kubernetes versions

The charts are [currently tested](https://devops-ci.elastic.co/job/elastic+helm-charts+master/) against all GKE versions available. 



