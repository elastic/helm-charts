# Breaking changes
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [6.8.9 - 2020/05/13](#689---20200513)
  - [Known Issues](#known-issues)
  - [GA support](#ga-support)
  - [New branching model](#new-branching-model)
  - [Filebeat container inputs](#filebeat-container-inputs)
  - [Metricbeat upgrade issue](#metricbeat-upgrade-issue)
  - [Metricbeat split values for daemonset and deployment](#metricbeat-split-values-for-daemonset-and-deployment)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!-- Use this to update TOC: -->
<!-- docker run --rm -it -v $(pwd):/usr/src jorgeandrada/doctoc --github -->


## 6.8.9 - 2020/05/13

### Known Issues

Elasticsearch nodes could be restarted too quickly during an upgrade or rolling restart, potentially resulting in service disruption.
This is due to a bug introduced by the changes to the Elasticsearch `readinessProbe` in [#586][].

### GA support

Elasticsearch, Kibana, Filebeat and Metricbeat are moving from beta to GA and
are supported by Elastic following these limitations:
- only released charts coming from [Elastic Helm repo][] or
[GitHub releases][] are supported.
- released charts are only supported when using the same chart version and
application version (ie: using 7.7.0 chart with 6.8.8 or 7.6.2 application is
not supported).

### New branching model

Elastic Helm charts repository is now following a [new branching model][]:
- `master` branch is now a development branch for next major release.
- new `7.x` branch is a development branch for next minor release using SNAPSHOT
Docker images.
- new `7.7` branch is a development branch for next patch release using SNAPSHOT
Docker images

### Filebeat container inputs

Filebeat chart default config is now using [container input][] instead of
[docker input][] in [#568][].

### Metricbeat upgrade issue

Metricbeat upgrade are failing with
`spec.selector: Invalid value: ... field is immutable` error. This is related to
Metricbeat deployment selector including chart version which is not immutable.
You should use `helm upgrade --force` to upgrade Metricbeat. See [#621][] for
more details.

### Metricbeat split values for daemonset and deployment

Metricbeat is now using dedicated values for daemonset and deployment config.
The old values are still working but are now deprecated. See [#572][] for more
details.

[#94]: https://github.com/elastic/helm-charts/pull/94
[#352]: https://github.com/elastic/helm-charts/pull/352
[#458]: https://github.com/elastic/helm-charts/pull/458
[#540]: https://github.com/elastic/helm-charts/pull/540
[#568]: https://github.com/elastic/helm-charts/pull/568
[#572]: https://github.com/elastic/helm-charts/pull/572
[#586]: https://github.com/elastic/helm-charts/pull/586
[#621]: https://github.com/elastic/helm-charts/pull/621
[container input]: https://www.elastic.co/guide/en/beats/filebeat/7.7/filebeat-input-container.html
[docker input]: https://www.elastic.co/guide/en/beats/filebeat/7.7/filebeat-input-docker.html
[elastic helm repo]: https://helm.elastic.co
[github releases]: https://github.com/elastic/helm-charts/releases
[new branching model]: https://github.com/elastic/helm-charts/blob/master/CONTRIBUTING.md#branching
[kube-state-metrics]: https://github.com/helm/charts/tree/master/stable/kube-state-metrics
