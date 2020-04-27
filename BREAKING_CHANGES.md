# Breaking changes
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


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
[#458]: https://github.com/elastic/helm-charts/pull/458
[#540]: https://github.com/elastic/helm-charts/pull/540
[kube-state-metrics]: https://github.com/helm/charts/tree/master/stable/kube-state-metrics
