# Breaking changes
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [7.8.0 - 2020/06/18](#780---20200618)
    - [Stable Elasticsearch deprecated](#stable-elasticsearch-deprecated)
    - [APM Server memory limit](#apm-server-memory-limit)
    - [Elasticsearch service selector change](#elasticsearch-service-selector-change)
  - [7.7.0 - 2020/05/13](#770---20200513)
    - [Known Issues](#known-issues)
    - [GA support](#ga-support)
    - [New branching model](#new-branching-model)
    - [Filebeat container inputs](#filebeat-container-inputs)
    - [Metricbeat upgrade issue](#metricbeat-upgrade-issue)
    - [Metricbeat split values for daemonset and deployment](#metricbeat-split-values-for-daemonset-and-deployment)
  - [6.8.9 - 2020/05/13](#689---20200513)
  - [7.6.2 - 2020/03/31](#762---20200331)
    - [Kibana default resources](#kibana-default-resources)
  - [7.6.0 - 2020/02/11](#760---20200211)
    - [Elasticsearch default resources](#elasticsearch-default-resources)
  - [7.5.0 - 2019/12/02](#750---20191202)
    - [Metricbeat kube-state-metrics upgrade](#metricbeat-kube-state-metrics-upgrade)
  - [7.0.0-alpha1 - 2019/04/17](#700-alpha1---20190417)
    - [Elasticsearch upgrade from 6.x](#elasticsearch-upgrade-from-6x)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!-- Use this to update TOC: -->
<!-- docker run --rm -it -v $(pwd):/usr/src jorgeandrada/doctoc --github -->


# 7.8.0 - 2020/06/18

### Stable Elasticsearch deprecated

[Stable Elasticsearch chart][] is now deprecated in favor of
[Elastic Elasticsearch chart][] (see [Stable Elasticsearch chart notice][]).

Existing users of [Stable Elasticsearch chart][] can use the [migration guide][].

### APM Server memory limit

APM Servers default memory limit is increased in [#664][].

This change may impact memory available resources capacity in your Kubernetes
cluster.

To come back to former default values, use the following values:

```yaml
resources:
  limits:
    memory: "200Mi"
```

### Elasticsearch service selector change

Elasticsearch service selector is no more including `heritage` label.

This label is immutable and causes issues with the latest Helm v3 version which
does more verification (heritage has `Tiller` value with Helm 2 but `Helm`
value in Helm 3).

As this change is forcing `Service` recreation, a short disruption of a few
seconds can be noted during upgrade to 7.8.0.

See [#437][] for more details.


## 7.7.0 - 2020/05/13

### Known Issues

Elasticsearch nodes could be restarted too quickly during an upgrade or rolling
restart, potentially resulting in service disruption.
This is due to a bug introduced by the changes to the Elasticsearch
`readinessProbe` in [#586][].

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

Warning: When upgrading Metricbeat while using custom `metricbeatConfig` value
for `kube-state-metrics-metricbeat.yml`, Metricbeat deployment fails with
`missing field accessing 'metricbeat.modules.0.hosts.0' (source:'metricbeat.yml')`.

In this case `metricbeatConfig.kube-state-metrics-metricbeat.yml` value should
be migrated to `deployment.metricbeatConfig.metricbeat.yml`. See [#623][] for
more details.

## 6.8.9 - 2020/05/13

See [7.7.0 Breaking changes](#770---20200513)


## 7.6.2 - 2020/03/31

### Kibana default resources

Kibana default resources (cpu/memory requests and limits) are increased in
[#540][].

This change may impact cpu/memory available resources capacity in your
Kubernetes cluster.

To come back to former default values, use the following values:

```yaml
extraEnvs:
- name: "NODE_OPTIONS"
  value: ""
resources:
  requests:
    cpu: "100m"
    memory: "500Mi"
  limits:
    cpu: "1000m"
    memory: "1Gi"
```


## 7.6.0 - 2020/02/11

### Elasticsearch default resources

Elasticsearch default cpu requests is increased in [#458][] following our
recommendation that resources requests and limits should have the same values.

This change may impact available cpu capacity in your Kubernetes cluster.

To come back to former default values, use the following values:

```yaml
resources:
  requests:
    cpu: "100m"
```


## 7.5.0 - 2019/12/02

### Metricbeat kube-state-metrics upgrade

[kube-state-metrics][] chart dependency is upgraded from 1.6.0 to 2.4.1 in
[#352][]. This is causing Metricbeat chart upgrade from versions < 7.5.0 failing
with the following error:

```
UPGRADE FAILED
Error: Deployment.apps "metricbeat-kube-state-metrics" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:map[string]string{"app.kubernetes.io/name":"kube-state-metrics"}, MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field is immutable && Deployment.apps "metricbeat-metricbeat-metrics" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:map[string]string{"app":"metricbeat-metricbeat-metrics", "chart":"metricbeat-7.5.0", "heritage":"Tiller", "release":"metricbeat"}, MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field is immutable
Error: UPGRADE FAILED: Deployment.apps "metricbeat-kube-state-metrics" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:map[string]string{"app.kubernetes.io/name":"kube-state-metrics"}, MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field is immutable && Deployment.apps "metricbeat-metricbeat-metrics" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:map[string]string{"app":"metricbeat-metricbeat-metrics", "chart":"metricbeat-7.5.0", "heritage":"Tiller", "release":"metricbeat"}, MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field is immutable
```

The workaround is to use `--force` argument for `helm upgrade` command which
will force Metricbeat resources update through delete/recreate.


## 7.0.0-alpha1 - 2019/04/17

### Elasticsearch upgrade from 6.x

If you were using the default Elasticsearch version from the previous release
(6.6.2-alpha1) you will first need to upgrade to Elasticsearch 6.7.1 before
being able to upgrade to 7.0.0. You can do this by adding this to your values
file:

```yaml
esMajorVersion: 6
imageTag: 6.7.1
```

If you are upgrading an existing cluster that did not override the default
`storageClassName` you will now need to specify the `storageClassName`. This
only affects existing clusters and was changed in [#94][]. The advantage of this
is that now the Helm chart will just use the default `storageClassName` rather
than needing to override it for any providers where it is not called `standard`.

```
volumeClaimTemplate:
  storageClassName: "standard"
```


[#94]: https://github.com/elastic/helm-charts/pull/94
[#352]: https://github.com/elastic/helm-charts/pull/352
[#437]: https://github.com/elastic/helm-charts/pull/437
[#458]: https://github.com/elastic/helm-charts/pull/458
[#540]: https://github.com/elastic/helm-charts/pull/540
[#568]: https://github.com/elastic/helm-charts/pull/568
[#572]: https://github.com/elastic/helm-charts/pull/572
[#586]: https://github.com/elastic/helm-charts/pull/586
[#621]: https://github.com/elastic/helm-charts/pull/621
[#623]: https://github.com/elastic/helm-charts/pull/623
[#664]: https://github.com/elastic/helm-charts/pull/664
[container input]: https://www.elastic.co/guide/en/beats/filebeat/7.7/filebeat-input-container.html
[docker input]: https://www.elastic.co/guide/en/beats/filebeat/7.7/filebeat-input-docker.html
[elastic elasticsearch chart]: https://github.com/elastic/helm-charts/tree/master/elasticsearch
[elastic helm repo]: https://helm.elastic.co
[github releases]: https://github.com/elastic/helm-charts/releases
[migration guide]: https://github.com/elastic/helm-charts/blob/master/elasticsearch/examples/migration/README.md
[new branching model]: https://github.com/elastic/helm-charts/blob/master/CONTRIBUTING.md#branching
[kube-state-metrics]: https://github.com/helm/charts/tree/master/stable/kube-state-metrics
[stable elasticsearch chart]: https://github.com/helm/charts/tree/master/stable/elasticsearch
[stable elasticsearch chart notice]: https://github.com/helm/charts/tree/master/stable#elasticsearch#this-helm-chart-is-deprecated
