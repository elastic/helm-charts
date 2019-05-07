# Filebeat Helm Chart

This functionality is in alpha status and may be changed or removed completely in a future release. Elastic will take a best effort approach to fix any issues, but alpha features are not subject to the support SLA of official GA features.

This helm chart is a lightweight way to configure and run our official [Filebeat docker image](https://www.elastic.co/guide/en/beats/filebeat/current/running-on-docker.html).

## Requirements

* Kubernetes >= 1.8
* [Helm](https://helm.sh/) >= 2.8.0

## Installing

* Add the elastic helm charts repo
  ```
  helm repo add elastic https://helm.elastic.co
  ```
* Install it
  ```
  helm install --name filebeat elastic/filebeat --version 7.0.1-alpha1
  ```

## Compatibility

This chart is tested with the latest supported versions. The currently tested versions are:

| 5.x    | 6.x   | 7.x   |
| ------ | ----- | ----- |
| 5.6.16 | 6.7.2 | 7.0.1 |

Examples of installing older major versions can be found in the [examples](./examples) directory.

While only the latest releases are tested, it is possible to easily install old or new releases by overriding the `imageTag`. To install version `7.0.1` of Filebeat it would look like this:

```
helm install --name filebeat elastic/filebeat --version 7.0.1-alpha1 --set imageTag=7.0.1
```


## Configuration
| Parameter                | Description                                                                                                                                                                                                                                                                         | Default                                                                                                                   |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `filebeatConfig`         | Allows you to add any config files in `/usr/share/filebeat` such as `filebeat.yml`. See [values.yaml](./values.yaml) for an example of the formatting.                                                                                                                              | `{}`                                                                                                                      |
| `extraEnvs`              | Extra [environment variables](https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/#using-environment-variables-inside-of-your-config) which will be appended to the `env:` definition for the container                                  | `[]`                                                                                                                      |
| `extraVolumeMounts`      | Any extra volumes mounts to define for the Filebeat container                                                                                                                                                                                                                       | `[]`                                                                                                                      |
| `extraVolumes`           | Any extra volumes to define for the pod                                                                                                                                                                                                                                             | `[]`                                                                                                                      |
| `hostPathRoot`           | Fully-qualified [hostPath](https://kubernetes.io/docs/concepts/storage/volumes/#hostpath) that will be used to persist Filebeat registry data                                                                                                                                       | `/var/lib`                                                                                                                |
| `image`                  | The Filebeat docker image                                                                                                                                                                                                                                                           | `docker.elastic.co/beats/filebeat`                                                                                        |
| `imageTag`               | The Filebeat docker image tag                                                                                                                                                                                                                                                       | `7.0.1`                                                                                                                   |
| `imagePullPolicy`        | The Kubernetes [imagePullPolicy](https://kubernetes.io/docs/concepts/containers/images/#updating-images) value                                                                                                                                                                      | `IfNotPresent`                                                                                                            |
| `imagePullSecrets`       | Configuration for [imagePullSecrets](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#create-a-pod-that-uses-your-secret) so that you can use a private registry for your image                                                                | `[]`                                                                                                                      |
| `managedServiceAccount`  | Whether the `serviceAccount` should be managed by this helm chart. Set this to `false` in order to manage your own service account and related roles.                                                                                                                               | `true`                                                                                                                    |
| `podAnnotations`         | Configurable [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) applied to all Filebeat pods                                                                                                                                             | `{}`                                                                                                                      |
| `podSecurityContext`     | Configurable [podSecurityContext](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) for Filebeat pod execution environment                                                                                                                                | `fsGroup: 1000`<br>`runAsUser: 0`<br>`privileged: false`                                                                  |
| `livenessProbe`          | Parameters to pass to [liveness probe](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/) checks for values such as timeouts and thresholds.                                                                                            | `failureThreshold: 3`<br>`initialDelaySeconds: 10`<br>`periodSeconds: 10`<br>`successThreshold: 3`<br>`timeoutSeconds: 5` |
| `readinessProbe`         | Parameters to pass to [readiness probe](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/) checks for values such as timeouts and thresholds.                                                                                           | `failureThreshold: 3`<br>`initialDelaySeconds: 10`<br>`periodSeconds: 10`<br>`successThreshold: 3`<br>`timeoutSeconds: 5` |
| `resources`              | Allows you to set the [resources](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/) for the `DaemonSet`                                                                                                                                        | `requests.cpu: 100m`<br>`requests.memory: 100Mi`<br>`limits.cpu: 1000m`<br>`limits.memory: 200Mi`                         |
| `serviceAccount`         | The [serviceAccount](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) that Filebeat will use during execution                                                                                                                                   | `filebeat`                                                                                                                |
| `secretMounts`           | Allows you easily mount a secret as a file inside the `DaemonSet`. Useful for mounting certificates and other secrets. See [values.yaml](./values.yaml) for an example                                                                                                              | `[]`                                                                                                                      |
| `terminationGracePeriod` | Termination period (in seconds) to wait before killing Filebeat pod process on pod shutdown                                                                                                                                                                                         | `30`                                                                                                                      |
| `tolerations`            | Configurable [tolerations](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/)                                                                                                                                                                                 | `[]`                                                                                                                      |
| `updateStrategy`         | The [updateStrategy](https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/#updating-statefulsets) for the `DaemonSet`. By default Kubernetes will kill and recreate pods on updates. Setting this to `OnDelete` will require that pods be deleted manually. | `RollingUpdate`                                                                                                           |

## Examples

In [examples/](./examples) you will find some example configurations. These examples are used for the automated testing of this helm chart.

### Default

* Deploy the [default Elasticsearch helm chart](../elasticsearch/README.md#default)
* Deploy Filebeat with the default values
  ```
  cd examples/default
  make
  ```
* You can now setup a port forward for Elasticsearch to observe Filebeat indices
  ```
  kubectl port-forward svc/elasticsearch-master 9200
  curl localhost:9200/_cat/indices
  ```

## Testing

This chart uses [pytest](https://docs.pytest.org/en/latest/) to test the templating logic. The dependencies for testing can be installed from the [`requirements.txt`](../requirements.txt) in the parent directory.

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

Integration tests are run using [goss](https://github.com/aelsabbahy/goss/blob/master/docs/manual.md) which is a serverspec like tool written in golang. See [goss.yaml](examples/default/test/goss.yaml) for an example of what the tests look like.

To run the goss tests against the default example:
```
cd examples/default
make goss
```
