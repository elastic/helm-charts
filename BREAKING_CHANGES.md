# Breaking changes
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


  - [8.5.1](#851)
    - [Last Elastic Helm charts release](#last-elastic-helm-charts-release)
    - [Security by default for Elasticsearch](#security-by-default-for-elasticsearch)
    - [Kibana use a Service Account Token to connect to Elasticsearch](#kibana-use-a-service-account-token-to-connect-to-elasticsearch)
    - [Elasticsearch new node.roles settings](#elasticsearch-new-noderoles-settings)
    - [APM Server OSS removal](#apm-server-oss-removal)
    - [Supported K8S versions](#supported-k8s-versions)
  - [7.17.1](#7171)
    - [Metricbeat kube-state-metrics upgrade](#metricbeat-kube-state-metrics-upgrade)
  - [7.11.1](#7111)
    - [License update for Elasticsearch & Kibana](#license-update-for-elasticsearch--kibana)
  - [6.8.14](#6814)
  - [7.10.0](#7100)
    - [Migration to Helm 3](#migration-to-helm-3)
    - [End of K8S < 1.14 compatibility](#end-of-k8s--114-compatibility)
      - [Metricbeat upgrade](#metricbeat-upgrade)
      - [Elasticsearch upgrade with persistence.labels.enabled](#elasticsearch-upgrade-with-persistencelabelsenabled)
      - [Rendered manifests contain a resource that already exists error](#rendered-manifests-contain-a-resource-that-already-exists-error)
  - [7.9.3 - 2020/10/22](#793---20201022)
    - [Fix Logstash headless Service (end)](#fix-logstash-headless-service-end)
  - [6.8.13 - 2020/10/22](#6813---20201022)
  - [7.9.1 - 2020/09/03](#791---20200903)
    - [Fix Logstash headless Service](#fix-logstash-headless-service)
  - [7.9.0 - 2020/08/18](#790---20200818)
    - [Add Helm 3 support in beta](#add-helm-3-support-in-beta)
  - [6.8.12 - 2020/08/18](#6812---20200818)
  - [7.8.1 - 2020/07/28](#781---20200728)
    - [Add headless Service for StatefulSet](#add-headless-service-for-statefulset)
  - [6.8.11 - 2020/07/28](#6811---20200728)
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
    - [Metricbeat kube-state-metrics upgrade](#metricbeat-kube-state-metrics-upgrade-1)
  - [7.0.0-alpha1 - 2019/04/17](#700-alpha1---20190417)
    - [Elasticsearch upgrade from 6.x](#elasticsearch-upgrade-from-6x)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!-- Use this to update TOC: -->
<!-- docker run --entrypoint doctoc --rm -it -v $(pwd):/usr/src jorgeandrada/doctoc BREAKING_CHANGES.md --github --no-title -->

## 8.5.1

### Last Elastic Helm charts release

8.5.1 is expected to be the last Elastic Helm chart release. This repository will stay active for 6
months before being archived.

See <https://github.com/elastic/helm-charts/issues/1731> for more details.

### Security by default for Elasticsearch

Starting with 8.0.0, Elasticsearch comes with security (TLS + authentication) enabled and
auto-configured by default.
Therefore, the Elasticsearch chart has been updated to generate credentials and TLS certificate by
default.
Similarly, all charts have been updated to connect to a secured Elasticsearch deployed by the
Elasticsearch chart by default.

Consequently, running the Elasticsearch chart with security disabled isn't anymore supported.
The other charts are also not supporting anymore connection to an Elasticsearch without security.

Note that in addition to the security configured by default, it is still possible to use your own
TLS certificates, credentials and security configurations (see the `security` examples for each
chart).

See the related PRs for more details:

- <https://github.com/elastic/helm-charts/pull/1384>
- <https://github.com/elastic/helm-charts/pull/1399>
- <https://github.com/elastic/helm-charts/pull/1400>
- <https://github.com/elastic/helm-charts/pull/1401>
- <https://github.com/elastic/helm-charts/pull/1402>
- <https://github.com/elastic/helm-charts/pull/1403>
- <https://github.com/elastic/helm-charts/pull/1519>
- <https://github.com/elastic/helm-charts/pull/1623>
- <https://github.com/elastic/helm-charts/pull/1624>
- <https://github.com/elastic/helm-charts/pull/1625>
- <https://github.com/elastic/helm-charts/pull/1627>
- <https://github.com/elastic/helm-charts/pull/1628>
- <https://github.com/elastic/helm-charts/pull/1677>
- <https://github.com/elastic/helm-charts/pull/1691>

### Kibana use a Service Account Token to connect to Elasticsearch

In addition to the changes related to security by default, starting with 8.0.0, Kibana can't anymore
use the `elastic` super user to connect to Elasticsearch but needs to use service account token
instead. The Kibana chart is now using a `pre-install` Helm chart hook to request the creation of
this service account and register it in a K8S Secret that can be used by the Kibana pods.

See the related PRs for more details:

- <https://github.com/elastic/helm-charts/pull/1679>
- <https://github.com/elastic/helm-charts/pull/1695>
- <https://github.com/elastic/helm-charts/pull/1720>
- <https://github.com/elastic/helm-charts/pull/1727>

### Elasticsearch new node.roles settings

Starting with 8.5.1, the `roles` values in Elasticsearch chart support a simple list of the roles
to configure, instead of a dictionnary. All roles defined in the [Elasticsearch node roles doc][]
are now supported.

See the related PRs for more details:

- <https://github.com/elastic/helm-charts/pull/1186>
- <https://github.com/elastic/helm-charts/pull/1693>

### APM Server OSS removal

Starting with 8.0.0, APM Server doesn't provide anymore OSS version. Consequently this option
is removed from the APM Server chart.

See <https://github.com/elastic/helm-charts/pull/1442> for more details.

### Supported K8S versions

This release remove the support of K8S 1.19 and 1.20, and add the support of 1.23 and 1.24.

See <https://github.com/elastic/helm-charts/pull/1703> for more details.

## 7.17.1

### Metricbeat kube-state-metrics upgrade

[kube-state-metrics][] chart dependency is upgraded from 2.4.1 to 4.7.0 in
[#1524][]. This is causing Metricbeat chart upgrade from versions < 7.17.1 failing
with the following error:

```
UPGRADE FAILED
Error: UPGRADE FAILED: cannot patch "helm-metricbeat-default-kube-state-metrics" with kind Deployment: Deployment.apps "helm-metricbeat-default-kube-state-metrics" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:map[string]string{"app.kubernetes.io/instance":"helm-metricbeat-default", "app.kubernetes.io/name":"kube-state-metrics"}, MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field is immutable
```

Unfortunately `helm upgrade --force` is also failing. The workaround is to uninstall the previous chart version and reinstall it.

## 7.11.1

### License update for Elasticsearch & Kibana

Following recent license change, Elasticsearch and Kibana OSS versions are no more
available starting 7.11.0. See [Elastic blog post][] for more details.


## 6.8.14

See [7.10.0 Breaking changes](#7100)


## 7.10.0

### Migration to Helm 3

Starting from the 7.10.0 release, Helm 3 is fully supported in Elastic Helm charts
and Helm 2 is deprecated.

In most cases, [Helm 2to3][] can be used to migrate from previous charts
releases deployed with Helm 2:

```shell
# Install Helm 3

# Install 2to3 plugin
helm plugin install https://github.com/helm/helm-2to3.git

# Migrate Helm 2 local config
helm3 2to3 move config

# Migrate Helm 2 releases
helm3 2to3 convert <release-name>

# Upgrade to 7.10.0
helm upgrade <release-name> elastic/<chart-name> --version 7.10.0

# Cleanup Helm 2 data
helm3 2to3 cleanup
```

Migration to Helm 3 with 7.10.0 charts release should work smoothly for the
following charts.

- apm-server >= 7.6.0
- elasticsearch >= 7.4.0 (except when `persistence.labels.enabled` is true)
- filebeat >= 7.9.0
- kibana >= 7.4.0
- logstash >= 7.9.0

### End of K8S < 1.14 compatibility

[#916][] remove some helpers used for K8S version < 1.14.

If you are using an older K8S version, you should upgrade it or stay with
helm-charts < 7.10.

#### Metricbeat upgrade

Metricbeat 7.10.0 introduce a breaking change in [#516][] to make it compatible
with Helm 3.

The removing of some `heritage` labels in Metricbeat deployment make upgrade
fail with the following error:

```
UPGRADE FAILED
Error: Deployment.apps "mb-metricbeat-metrics" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:map[string]string{"app":"mb-metricbeat-metrics", "release":"mb"}, MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field is immutable
Error: UPGRADE FAILED: Deployment.apps "mb-metricbeat-metrics" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:map[string]string{"app":"mb-metricbeat-metrics", "release":"mb"}, MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field is immutable
```

Unfortunately using `helm upgrade --force` with Helm 3 is not enough. This chart
will need to be uninstalled and re-installed.

#### Elasticsearch upgrade with persistence.labels.enabled

If you are using `persistence.labels.enabled=true` with Elasticsearch, upgrade
will fail even with `--force`.

You'll need to deploy a new release with the same `clusterName` using Helm 3,
migrate your data, then remove the old release.

#### Rendered manifests contain a resource that already exists error

We experimented some `rendered manifests contain a resource that already exists`
errors with some charts upgrade, mostly for charts deploying `ClusterRole` and
`ClusterRoleBinding`resources.

Helm 3 is automatically adding some new annotations (`meta.helm.sh/release-name`
and `meta.helm.sh/release-namespace`) and labels (`app.kubernetes.io/managed-by`)
to the charts resources during upgrade. However it sometimes fail to add the annotations with the below error:

```
Error: UPGRADE FAILED: rendered manifests contain a resource that already exists. Unable to continue with update: ClusterRole "apm-apm-server-cluster-role" in namespace "" exists and cannot be imported into the current release: invalid ownership metadata; label validation error: missing key "app.kubernetes.io/managed-by": must be set to "Helm"; annotation validation error: missing key "meta.helm.sh/release-name": must be set to "apm"; annotation validation error: missing key "meta.helm.sh/release-namespace": must be set to "default"
```

The workaround is to manually add these annotations and labels to the existing failing resources
using `kubectl edit` for example, then relaunch the upgrade command.


## 7.9.3 - 2020/10/22

### Fix Logstash headless Service (end)

[#839][] fix the issue reported in [#807][] when using a `NodePort` `Service`
(see [Fix Logstash headless Service](#fix-logstash-headless-service) for more
details).

## 6.8.13 - 2020/10/22

See [7.9.3 - 2020/10/22](#793---20201022) and [7.9.1 - 2020/09/03](#791---20200903)


## 7.9.1 - 2020/09/03

### Fix Logstash headless Service

[#776][] fixed an issue with headless `Service` when using `extraPorts` value
(see [Add headless Service for StatefulSet](#add-headless-service-for-statefulset)
for more details). Unfortunately, it introduced a new bug when using a `NodePort`
`Service` ([#807][]). This is fixed by [#839][] in 7.9.3 (and 6.8.13).

## 7.9.0 - 2020/08/18

### Add Helm 3 support in beta

Starting with 7.9.0, all the main blockers for Helm 3 are fixed. While automated
CI tests are not updated to use Helm 3 yet, deploying these charts Helm 3 with
Helm 3 is now supported in beta.


## 6.8.12 - 2020/08/18

See [7.9.0 Breaking changes](#790---20200818)

## 7.8.1 - 2020/07/28

### Add headless Service for StatefulSet

A headless `Service` has been added to Logstash chart in [#695][].

The headless `Service` is required for `Statefulsets`. Helm 2 allowed
deploying a `Statefulset` without a `serviceName`, however Helm 3 enforces this
requirement and fails if `serviceName` is missing.

`Statefulset` does not accept the `serviceName` field update during release upgrades.
Upgrading the Logstash chart from a previous version will require using
`helm upgrade --force`.

**Edit:** This change introduced a bug when using `extraPorts` value ([#765][]).
This will be fixed by [#776][] with 7.9.1 (and 6.8.13) release.

Meanwhile, you should rollback to 7.8.0 (or 6.8.10) release of Logstash chart if
you are using some custom `extraPorts` value.


## 6.8.11 - 2020/07/28

See [7.8.1 Breaking changes](#781---20200728)


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


[#1524]: https://github.com/elastic/helm-charts/pull/1524
[#352]: https://github.com/elastic/helm-charts/pull/352
[#437]: https://github.com/elastic/helm-charts/pull/437
[#458]: https://github.com/elastic/helm-charts/pull/458
[#516]: https://github.com/elastic/helm-charts/pull/516
[#540]: https://github.com/elastic/helm-charts/pull/540
[#568]: https://github.com/elastic/helm-charts/pull/568
[#572]: https://github.com/elastic/helm-charts/pull/572
[#586]: https://github.com/elastic/helm-charts/pull/586
[#621]: https://github.com/elastic/helm-charts/pull/621
[#623]: https://github.com/elastic/helm-charts/pull/623
[#664]: https://github.com/elastic/helm-charts/pull/664
[#695]: https://github.com/elastic/helm-charts/pull/695
[#765]: https://github.com/elastic/helm-charts/issues/765
[#776]: https://github.com/elastic/helm-charts/issues/776
[#807]: https://github.com/elastic/helm-charts/issues/807
[#839]: https://github.com/elastic/helm-charts/issues/839
[#916]: https://github.com/elastic/helm-charts/pull/916
[#94]: https://github.com/elastic/helm-charts/pull/94
[container input]: https://www.elastic.co/guide/en/beats/filebeat/7.7/filebeat-input-container.html
[docker input]: https://www.elastic.co/guide/en/beats/filebeat/7.7/filebeat-input-docker.html
[elastic blog post]: https://www.elastic.co/blog/licensing-change
[elastic elasticsearch chart]: https://github.com/elastic/helm-charts/tree/main/elasticsearch
[elastic helm repo]: https://helm.elastic.co
[elasticsearch node roles doc]: https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-node.html#node-roles
[github releases]: https://github.com/elastic/helm-charts/releases
[helm 2to3]: https://helm.sh/blog/migrate-from-helm-v2-to-helm-v3/
[kube-state-metrics]: https://github.com/helm/charts/tree/master/stable/kube-state-metrics
[migration guide]: https://github.com/elastic/helm-charts/blob/main/elasticsearch/examples/migration/README.md
[new branching model]: https://github.com/elastic/helm-charts/blob/main/CONTRIBUTING.md#branching
[stable elasticsearch chart notice]: https://github.com/helm/charts/tree/master/stable#elasticsearch#this-helm-chart-is-deprecated
[stable elasticsearch chart]: https://github.com/helm/charts/tree/master/stable/elasticsearch
