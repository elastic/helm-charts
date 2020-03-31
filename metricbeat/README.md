# Metricbeat Helm Chart

This functionality is in beta and is subject to change. The design and code is less mature than official GA features and is being provided as-is with no warranties. Beta features are not subject to the support SLA of official GA features.

This helm chart is a lightweight way to configure and run our official [Metricbeat docker image](https://www.elastic.co/guide/en/beats/metricbeat/current/running-on-docker.html).

## Breaking Changes

[7.5.1](https://github.com/elastic/helm-charts/releases/tag/7.5.1) release is introducing a breaking change for Metricbeat users upgrading from a previous chart version.
The breaking change tracked in [#395](https://github.com/elastic/helm-charts/issues/395) is failing `helm upgrade` command with the following error:
```
UPGRADE FAILED
Error: Deployment.apps "metricbeat-kube-state-metrics" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:map[string]string{"app.kubernetes.io/name":"kube-state-metrics"}, MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field is immutable && Deployment.apps "metricbeat-metricbeat-metrics" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:map[string]string{"app":"metricbeat-metricbeat-metrics", "chart":"metricbeat-7.5.1", "heritage":"Tiller", "release":"metricbeat"}, MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field is immutable
Error: UPGRADE FAILED: Deployment.apps "metricbeat-kube-state-metrics" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:map[string]string{"app.kubernetes.io/name":"kube-state-metrics"}, MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field is immutable && Deployment.apps "metricbeat-metricbeat-metrics" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:map[string]string{"app":"metricbeat-metricbeat-metrics", "chart":"metricbeat-7.5.1", "heritage":"Tiller", "release":"metricbeat"}, MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field is immutable
```

This is caused by the update of [kube-state-metrics](https://github.com/helm/charts/tree/master/stable/kube-state-metrics) chart dependency which is renaming some labels in [helm/charts#15261](https://github.com/helm/charts/pull/15261).

The workaround is to use `--force` argument for `helm upgrade` command which will force Metricbeat resources update through delete/recreate.

## Requirements

* [Helm](https://helm.sh/) >=2.8.0 and <3.0.0 (see parent [README](https://github.com/elastic/helm-charts/tree/master/README.md) for more details)
* Kubernetes >=1.9

## Installing

### Using Helm repository

* Add the elastic helm charts repo
  ```
  helm repo add elastic https://helm.elastic.co
  ```
* Install it
  ```
  helm install --name metricbeat elastic/metricbeat
  ```

### Using master branch

* Clone the git repo
  ```
  git clone git@github.com:elastic/helm-charts.git
  ```
* Install it
  ```
  helm install --name metricbeat ./helm-charts/metricbeat
  ```

## Compatibility

This chart is tested with the latest supported versions. The currently tested versions are:

| 6.x   | 7.x   |
| ----- | ----- |
| 6.8.8 | 7.6.2 |

Examples of installing older major versions can be found in the [examples](https://github.com/elastic/helm-charts/tree/master/metricbeat/examples) directory.

While only the latest releases are tested, it is possible to easily install old or new releases by overriding the `imageTag`. To install version `7.6.2` of metricbeat it would look like this:

```
helm install --name metricbeat elastic/metricbeat --set imageTag=7.6.2
```


## Configuration
| Parameter                | Description                                                                                                                                                                                                                                                                                                              | Default                                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| `metricbeatConfig`       | Allows you to add any config files in `/usr/share/metricbeat` such as `metricbeat.yml`. See [values.yaml](https://github.com/elastic/helm-charts/tree/master/metricbeat/values.yaml) for an example of the formatting with the default configuration.                                                                    | see [values.yaml](https://github.com/elastic/helm-charts/tree/master/metricbeat/values.yaml)                              |
| `extraContainers`        | Templatable string of additional containers to be passed to the `tpl` function                                                                                                                                                                                                                                           | `""`                                                                                                                      |
| `extraInitContainers`    | Templatable string of additional containers to be passed to the `tpl` function                                                                                                                                                                                                                                           | `""`                                                                                                                      |
| `extraEnvs`              | Extra [environment variables](https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/#using-environment-variables-inside-of-your-config) which will be appended to the `env:` definition for the container                                                                       | `[]`                                                                                                                      |
| `extraVolumeMounts`      | Templatable string of additional volumeMounts to be passed to the `tpl` function                                                                                                                                                                                                                                         | `""`                                                                                                                      |
| `extraVolumes`           | Templatable string of additional volumes to be passed to the `tpl` function                                                                                                                                                                                                                                              | `""`                                                                                                                      |
| `envFrom`                | Templatable string of envFrom to be passed to the  [environment from variables](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/#configure-all-key-value-pairs-in-a-configmap-as-container-environment-variables) which will be appended to the `envFrom:` definition for the container | `[]`                                                                                                                      |
| `hostPathRoot`           | Fully-qualified [hostPath](https://kubernetes.io/docs/concepts/storage/volumes/#hostpath) that will be used to persist Metricbeat registry data                                                                                                                                                                          | `/var/lib`                                                                                                                |
| `image`                  | The Metricbeat docker image                                                                                                                                                                                                                                                                                              | `docker.elastic.co/beats/metricbeat`                                                                                      |
| `imageTag`               | The Metricbeat docker image tag                                                                                                                                                                                                                                                                                          | `7.6.2`                                                                                                                   |
| `imagePullPolicy`        | The Kubernetes [imagePullPolicy](https://kubernetes.io/docs/concepts/containers/images/#updating-images) value                                                                                                                                                                                                           | `IfNotPresent`                                                                                                            |
| `imagePullSecrets`       | Configuration for [imagePullSecrets](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#create-a-pod-that-uses-your-secret) so that you can use a private registry for your image                                                                                                     | `[]`                                                                                                                      |
| `labels`                 | Configurable [label](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) applied to all Metricbeat pods                                                                                                                                                                                           | `{}`                                                                                                                      |
| `managedServiceAccount`  | Whether the `serviceAccount` should be managed by this helm chart. Set this to `false` in order to manage your own service account and related roles.                                                                                                                                                                    | `true`                                                                                                                    |
| `clusterRoleRules`       | Configurable [cluster role rules](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-and-clusterrole) that Metricbeat uses to access Kubernetes resources.                                                                                                                                               | see [values.yaml](https://github.com/elastic/helm-charts/tree/master/metricbeat/values.yaml)                              |
| `podAnnotations`         | Configurable [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) applied to all Metricbeat pods                                                                                                                                                                                | `{}`                                                                                                                      |
| `podSecurityContext`     | Configurable [podSecurityContext](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) for Metricbeat pod execution environment                                                                                                                                                                   | `runAsUser: 0`<br>`privileged: false`                                                                                     |
| `livenessProbe`          | Parameters to pass to [liveness probe](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/) checks for values such as timeouts and thresholds.                                                                                                                                 | `failureThreshold: 3`<br>`initialDelaySeconds: 10`<br>`periodSeconds: 10`<br>`successThreshold: 3`<br>`timeoutSeconds: 5` |
| `readinessProbe`         | Parameters to pass to [readiness probe](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/) checks for values such as timeouts and thresholds.                                                                                                                                | `failureThreshold: 3`<br>`initialDelaySeconds: 10`<br>`periodSeconds: 10`<br>`successThreshold: 3`<br>`timeoutSeconds: 5` |
| `resources`              | Allows you to set the [resources](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/) for the `DaemonSet`                                                                                                                                                                             | `requests.cpu: 100m`<br>`requests.memory: 100Mi`<br>`limits.cpu: 1000m`<br>`limits.memory: 200Mi`                         |
| `serviceAccount`         | Custom [serviceAccount](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) that Metricbeat will use during execution. By default will use the service account created by this chart.                                                                                                   | `""`                                                                                                                      |
| `secretMounts`           | Allows you easily mount a secret as a file inside the `DaemonSet`. Useful for mounting certificates and other secrets. See [values.yaml](https://github.com/elastic/helm-charts/tree/master/metricbeat/values.yaml) for an example                                                                                       | `[]`                                                                                                                      |
| `terminationGracePeriod` | Termination period (in seconds) to wait before killing Metricbeat pod process on pod shutdown                                                                                                                                                                                                                            | `30`                                                                                                                      |
| `tolerations`            | Configurable [tolerations](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/)                                                                                                                                                                                                                      | `[]`                                                                                                                      |
| `nodeSelector`           | Configurable [nodeSelector](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector)                                                                                                                                                                                                             | `{}`                                                                                                                      |
| `affinity`               | Configurable [affinity](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity)                                                                                                                                                                                                   | `{}`                                                                                                                      |
| `updateStrategy`         | The [updateStrategy](https://kubernetes.io/docs/tasks/manage-daemon/update-daemon-set/#daemonset-update-strategy) for the `DaemonSet`. By default Kubernetes will kill and recreate pods on updates. Setting this to `OnDelete` will require that pods be deleted manually.                                              | `RollingUpdate`                                                                                                           |
| `priorityClassName`      | The [name of the PriorityClass](https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/#priorityclass). No default is supplied as the PriorityClass must be created first.                                                                                                                            | `""`                                                                                                                      |
| `replicas`               | The replica count for the metricbeat deployment talking to kube-state-metrics                                                                                                                                                                                                                                            | `1`                                                                                                                       |
| `fullnameOverride`       | Overrides the full name of the resources. If not set the name will default to "`.Release.Name`-`.Values.nameOverride or .Chart.Name`"                                                                                                                                                                                    | `""`                                                                                                                      |

## Examples

In [examples/](https://github.com/elastic/helm-charts/tree/master/metricbeat/examples) you will find some example configurations. These examples are used for the automated testing of this helm chart.

### Default

* Deploy the [default Elasticsearch helm chart](https://github.com/elastic/helm-charts/tree/master/elasticsearch/README.md#default)
* Deploy Metricbeat with the default values
  ```
  cd examples/default
  make
  ```
* You can now setup a port forward for Elasticsearch to observe Metricbeat indices
  ```
  kubectl port-forward svc/elasticsearch-master 9200
  curl localhost:9200/_cat/indices
  ```

## Testing

This chart uses [pytest](https://docs.pytest.org/en/latest/) to test the templating logic. The dependencies for testing can be installed from the [`requirements.txt`](https://github.com/elastic/helm-charts/tree/master/requirements.txt) in the parent directory.

```
pip install -r ../requirements.txt
make pytest
```

You can also use `helm template` to look at the YAML being generated

```
make template
```

It is possible to run all of the tests and linting inside of a docker container

```
make test
```

## Integration Testing

Integration tests are run using [goss](https://github.com/aelsabbahy/goss/blob/master/docs/manual.md) which is a serverspec like tool written in golang. See [goss.yaml](https://github.com/elastic/helm-charts/tree/master/metricbeat/examples/default/test/goss.yaml) for an example of what the tests look like.

To run the goss tests against the default example:
```
cd examples/default
make goss
```
