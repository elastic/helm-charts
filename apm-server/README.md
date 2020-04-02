# APM Server Helm Chart

This functionality is in alpha and is subject to change. The design and code is
less mature than official GA features and is being provided as-is with no
warranties. Alpha features are not subject to the support SLA of official GA
features.

This helm chart is a lightweight way to configure and run our official
[APM Server docker image](https://www.elastic.co/guide/en/apm/server/current/running-on-docker.html).

## Requirements

* Kubernetes >= 1.9
* [Helm](https://helm.sh/) >= 2.8.0

## Usage notes and getting started
* The default APM Server configuration file for this chart is configured to use an
Elasticsearch endpoint as configured by the rest of these helm charts. This can
easily be overridden in the config value `apmConfig.apm-server.yml`.
* Automated testing of this chart is currently only run against GKE (Google Kubernetes Engine).

## Installing

* Add the elastic helm charts repo
  ```
  helm repo add elastic https://helm.elastic.co
  ```
* Install it
  ```
  helm install --name apm-server elastic/apm-server
  ```

### Using master branch

* Clone the git repo
  ```
  git clone git@github.com:elastic/helm-charts.git
  ```
* Install it
  ```
  helm install --name apm-server ./helm-charts/apm-server
  ```

## Compatibility

This chart is tested with the latest supported versions. The currently tested versions are:

| 6.x   | 7.x   |
| ----- | ----- |
| 6.8.8 | 7.6.2 |

Examples of installing older major versions can be found in the
[examples](https://github.com/elastic/helm-charts/tree/master/apm-server/examples) directory.

While only the latest releases are tested, it is possible to easily install old
or new releases by overriding the `imageTag`. To install version `7.6.2` of APM
Server it would look like this:

```
helm install --name apm-server elastic/apm-server --set imageTag=7.6.2
```


## Configuration
| Parameter                | Description                                                                                                                                                                                                                                                                 | Default                                                                                                                   |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `apmConfig`              | Allows you to add any config files in `/usr/share/apm-server/config` such as `apm-server.yml`. See [values.yaml](https://github.com/elastic/helm-charts/tree/master/apm-server/values.yaml) for an example of the formatting with the default configuration.                | see [values.yaml](https://github.com/elastic/helm-charts/tree/master/apm-server/values.yaml)                              |
| `replicas`               | Number of APM servers to run                                                                                                                                                                                                                                                | `1`                                                                                                                       |
| `extraContainers`        | Templatable string of additional containers to be passed to the `tpl` function                                                                                                                                                                                              | `""`                                                                                                                      |
| `extraInitContainers`    | Templatable string of additional containers to be passed to the `tpl` function                                                                                                                                                                                              | `""`                                                                                                                      |
| `extraEnvs`              | Extra [environment variables](https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/#using-environment-variables-inside-of-your-config) which will be appended to the `env:` definition for the container                          | `[]`                                                                                                                      |
| `extraVolumeMounts`      | List of additional volumeMounts                                                                                                                                                                                                                                             | `[]`                                                                                                                      |
| `extraVolumes`           | List of additional volumes                                                                                                                                                                                                                                                  | `[]`                                                                                                                      |
| `image`                  | The APM Server docker image                                                                                                                                                                                                                                                 | `docker.elastic.co/apm/apm-server`                                                                                        |
| `imageTag`               | The APM Server docker image tag                                                                                                                                                                                                                                             | `7.6.2`                                                                                                                   |
| `imagePullPolicy`        | The Kubernetes [imagePullPolicy](https://kubernetes.io/docs/concepts/containers/images/#updating-images) value                                                                                                                                                              | `IfNotPresent`                                                                                                            |
| `imagePullSecrets`       | Configuration for [imagePullSecrets](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#create-a-pod-that-uses-your-secret) so that you can use a private registry for your image                                                        | `[]`                                                                                                                      |
| `managedServiceAccount`  | Whether the `serviceAccount` should be managed by this helm chart. Set this to `false` in order to manage your own service account and related roles.                                                                                                                       | `true`                                                                                                                    |
| `podAnnotations`         | Configurable [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) applied to all APM Server pods                                                                                                                                   | `{}`                                                                                                                      |
| `labels`                 | Configurable [label](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) applied to all APM server pods                                                                                                                                              | `{}`                                                                                                                      |
| `podSecurityContext`     | Configurable [podSecurityContext](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) for APM Server pod execution environment                                                                                                                      | `runAsUser: 0`<br>`privileged: false`                                                                                     |
| `livenessProbe`          | Parameters to pass to [liveness probe](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/) checks for values such as timeouts and thresholds.                                                                                    | `failureThreshold: 3`<br>`initialDelaySeconds: 10`<br>`periodSeconds: 10`<br>`successThreshold: 3`<br>`timeoutSeconds: 5` |
| `readinessProbe`         | Parameters to pass to [readiness probe](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/) checks for values such as timeouts and thresholds.                                                                                   | `failureThreshold: 3`<br>`initialDelaySeconds: 10`<br>`periodSeconds: 10`<br>`successThreshold: 3`<br>`timeoutSeconds: 5` |
| `resources`              | Allows you to set the [resources](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/) for the `Deployment`                                                                                                                               | `requests.cpu: 100m`<br>`requests.memory: 100Mi`<br>`limits.cpu: 1000m`<br>`limits.memory: 200Mi`                         |
| `serviceAccount`         | Custom [serviceAccount](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) that APM Server will use during execution. By default will use the service account created by this chart.                                                      | `""`                                                                                                                      |
| `secretMounts`           | Allows you easily mount a secret as a file inside the `Deployment`. Useful for mounting certificates and other secrets. See [values.yaml](https://github.com/elastic/helm-charts/tree/master/apm-server/values.yaml) for an example                                         | `[]`                                                                                                                      |
| `terminationGracePeriod` | Termination period (in seconds) to wait before killing APM Server pod process on pod shutdown                                                                                                                                                                               | `30`                                                                                                                      |
| `tolerations`            | Configurable [tolerations](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/)                                                                                                                                                                         | `[]`                                                                                                                      |
| `nodeSelector`           | Configurable [nodeSelector](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector)                                                                                                                                                                | `{}`                                                                                                                      |
| `affinity`               | Configurable [affinity](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity)                                                                                                                                                      | `{}`                                                                                                                      |
| `priorityClassName`      | The [name of the PriorityClass](https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/#priorityclass). No default is supplied as the PriorityClass must be created first.                                                                               | `""`                                                                                                                      |
| `updateStrategy`         | Allows you to change the default update [strategy](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#updating-a-deployment) for the deployment.                                                                                                         | `RollingUpdate`                                                                                                           |
| `autoscaling.enabled`    | Enable the pod [horizonatal auto scaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)                                                                                                                                                        | `false`                                                                                                                   |
| `ingress`                | Configurable [ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) to expose the APM Server service. See [`values.yaml`](https://github.com/elastic/helm-charts/tree/master/apm-server/values.yaml) for an example                                    | `enabled: false`                                                                                                          |
| `service`                | Configurable [service](https://kubernetes.io/docs/concepts/services-networking/service/) to expose the APM Server service. See [`values.yaml`](https://github.com/elastic/helm-charts/tree/master/apm-server/values.yaml) for an example                                    | `type: ClusterIP`<br>`port: 8200`<br>`nodePort:`<br>`annotations: {}`                                                     |
| `lifecycle`              | Configurable [livecycle hooks](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/)                                                                                                                                                                   | `false`                                                                                                                   |
| `nameOverride`           | Overrides the chart name for resources. If not set the name will default to `.Chart.Name`                                                                                                                                                                                   | `""`                                                                                                                      |
| `fullnameOverride`       | Overrides the full name of the resources. If not set the name will default to `.Release.Name`-`.Values.nameOverride` or `.Chart.Name`                                                                                                                                       | `""`                                                                                                                      |

## Examples

In [examples/](ahttps://github.com/elastic/helm-charts/tree/master/apm-server/examples) you will find some example configurations. These examples
are used for the automated testing of this helm chart.

### Default

* Deploy the [default Elasticsearch helm chart](https://github.com/elastic/helm-charts/tree/master/elasticsearch/README.md#default)
* Deploy APM Server with the default values
  ```
  cd examples/default
  make
  ```
* You can now setup a port forward for Elasticsearch to observe APM indices
  ```
  kubectl port-forward svc/elasticsearch-master 9200
  curl localhost:9200/_cat/indices
  ```

## Testing

This chart uses [pytest](https://docs.pytest.org/en/latest/) to test the templating
logic. The dependencies for testing can be installed from the
[`requirements.txt`](https://github.com/elastic/helm-charts/tree/master/requirements.txt) in the parent directory.

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

Integration tests are run using
[goss](https://github.com/aelsabbahy/goss/blob/master/docs/manual.md) which is a
serverspec like tool written in golang. See [goss.yaml](https://github.com/elastic/helm-charts/tree/master/apm-server/examples/default/test/goss.yaml)
for an example of what the tests look like.

To run the goss tests against the default example:
```
cd examples/default
make goss
```
