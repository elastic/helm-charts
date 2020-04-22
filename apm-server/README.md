# APM Server Helm Chart

This functionality is in alpha and is subject to change. The design and code is
less mature than official GA features and is being provided as-is with no
warranties. Alpha features are not subject to the support SLA of official GA
features.

This Helm chart is a lightweight way to configure and run our official
[APM Server Docker image][].

## Requirements

* Kubernetes >= 1.9
* [Helm][] >= 2.8.0

## Usage notes and getting started

* The default APM Server configuration file for this chart is configured to use
an Elasticsearch endpoint as configured by the rest of these Helm charts. This
can easily be overridden in the config value `apmConfig.apm-server.yml`.

* Automated testing of this chart is currently only run against GKE (Google
Kubernetes Engine).

## Installing

* Add the Elastic Helm charts repo:

  ```
  helm repo add elastic https://helm.elastic.co
  ```

* Install it:

  ```
  helm install --name apm-server elastic/apm-server
  ```

### Using master branch

* Clone the git repo:

  ```
  git clone git@github.com:elastic/helm-charts.git
  ```

* Install it:

  ```
  helm install --name apm-server ./helm-charts/apm-server
  ```

## Compatibility

This chart is tested with the latest supported versions. The currently tested
versions are:

| 6.x   | 7.x   |
|-------|-------|
| 6.8.8 | 7.6.2 |

Examples of installing older major versions can be found in the [examples][]
directory.

While only the latest releases are tested, it is possible to easily install old
or new releases by overriding the `imageTag`. To install version `7.6.2` of APM
Server it would look like this:

```
helm install --name apm-server elastic/apm-server --set imageTag=7.6.2
```

## Configuration

| Parameter                | Description                                                                                                                                                | Default                            |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| `affinity`               | Configurable [affinity][]                                                                                                                                  | `{}`                               |
| `apmConfig`              | Allows you to add any config files in `/usr/share/apm-server/config` such as `apm-server.yml`                                                              | see [values.yaml][]                |
| `autoscaling`            | Enable the [horizontal pod autoscaler][]                                                                                                                   | `enabled: false`                   |
| `extraContainers`        | Templatable string of additional containers to be passed to the `tpl` function                                                                             | `""`                               |
| `extraEnvs`              | Extra [environment variables][] which will be appended to the `env:` definition for the container                                                          | `[]`                               |
| `extraInitContainers`    | Templatable string of additional containers to be passed to the `tpl` function                                                                             | `""`                               |
| `extraVolumeMounts`      | List of additional `volumeMounts`                                                                                                                          | `[]`                               |
| `extraVolumes`           | List of additional `volumes`                                                                                                                               | `[]`                               |
| `fullnameOverride`       | Overrides the full name of the resources. If not set the name will default to `.Release.Name` - `.Values.nameOverride` or `.Chart.Name`                    | `""`                               |
| `imagePullPolicy`        | The Kubernetes [imagePullPolicy][] value                                                                                                                   | `IfNotPresent`                     |
| `imagePullSecrets`       | Configuration for [imagePullSecrets][] so that you can use a private registry for your image                                                               | `[]`                               |
| `imageTag`               | The APM Server Docker image tag                                                                                                                            | `7.6.2`                            |
| `image`                  | The APM Server Docker image                                                                                                                                | `docker.elastic.co/apm/apm-server` |
| `ingress`                | Configurable [ingress][] to expose the APM Server service                                                                                                  | see [values.yaml][]                |
| `labels`                 | Configurable [labels][] applied to all APM server pods                                                                                                     | `{}`                               |
| `lifecycle`              | Configurable [lifecycle hooks][]                                                                                                                           | `false`                            |
| `livenessProbe`          | Parameters to pass to liveness [probe][] checks for values such as timeouts and thresholds                                                                 | see [values.yaml][]                |
| `managedServiceAccount`  | Whether the `serviceAccount` should be managed by this Helm chart. Set this to `false` in order to manage your own service account and related roles       | `true`                             |
| `nameOverride`           | Overrides the chart name for resources. If not set the name will default to `.Chart.Name`                                                                  | `""`                               |
| `nodeSelector`           | Configurable [nodeSelector][]                                                                                                                              | `{}`                               |
| `podAnnotations`         | Configurable [annotations][] applied to all APM Server pods                                                                                                | `{}`                               |
| `podSecurityContext`     | Configurable [podSecurityContext][] for APM Server pod execution environment                                                                               | see [values.yaml][]                |
| `priorityClassName`      | The name of the [PriorityClass][]. No default is supplied as the `PriorityClass` must be created first                                                     | `""`                               |
| `readinessProbe`         | Parameters to pass to readiness [probe][] checks for values such as timeouts and thresholds                                                                | see [values.yaml][]                |
| `replicas`               | Number of APM servers to run                                                                                                                               | `1`                                |
| `resources`              | Allows you to set the [resources][] for the `Deployment`                                                                                                   | see [values.yaml][]                |
| `secretMounts`           | Allows you easily mount a secret as a file inside the `Deployment`. Useful for mounting certificates and other secrets. See [values.yaml][] for an example | `[]`                               |
| `serviceAccount`         | Custom [serviceAccount][] that APM Server will use during execution. By default will use the `serviceAccount` created by this chart                        | `""`                               |
| `service`                | Configurable [service][] to expose the APM Server service. See [values.yaml][] for an example                                                              | see [values.yaml][]                |
| `terminationGracePeriod` | Termination period (in seconds) to wait before killing APM Server pod process on pod shutdown                                                              | `30`                               |
| `tolerations`            | Configurable [tolerations][]                                                                                                                               | `[]`                               |
| `updateStrategy`         | Allows you to change the default [updateStrategy][] for the deployment                                                                                     | see [values.yaml][]                |

## Examples

In [examples][] you will find some example configurations. These examples are
used for the automated testing of this Helm chart.

### Default

* Deploy the [default Elasticsearch Helm chart][].

* Deploy APM Server with the default values:

  ```
  cd examples/default
  make
  ```

* You can now setup a port forward for Elasticsearch to observe APM indices:

  ```
  kubectl port-forward svc/elasticsearch-master 9200
  curl localhost:9200/_cat/indices
  ```

## Testing

This chart uses [pytest][] to test the templating logic. The dependencies for
testing can be installed from the [requirements.txt][] in the parent directory:

```
pip install -r ../requirements.txt
make pytest
```

You can also use `helm template` to look at the YAML being generated:

```
make template
```

It is possible to run all of the tests and linting inside of a Docker container:

```
make test
```

## Integration Testing

Integration tests are run using [goss][] which is a serverspec like tool written
in golang. See [goss.yaml][] for an example of what the tests look like.

To run the goss tests against the default example:

```
cd examples/default
make goss
```

[affinity]: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity
[annotations]: https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/
[apm server docker image]: https://www.elastic.co/guide/en/apm/server/current/running-on-docker.html
[default elasticsearch helm chart]: https://github.com/elastic/helm-charts/tree/master/elasticsearch/README.md#default
[environment variables]: https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/#using-environment-variables-inside-of-your-config
[examples]: https://github.com/elastic/helm-charts/tree/master/apm-server/examples
[goss]: https://github.com/aelsabbahy/goss/blob/master/docs/manual.md
[goss.yaml]: https://github.com/elastic/helm-charts/tree/master/apm-server/examples/default/test/goss.yaml
[helm]: https://helm.sh
[horizontal pod autoscaler]: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/
[imagePullPolicy]: https://kubernetes.io/docs/concepts/containers/images/#updating-images
[imagePullSecrets]: https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#create-a-pod-that-uses-your-secret
[ingress]: https://kubernetes.io/docs/concepts/services-networking/ingress/
[labels]: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
[lifecycle hooks]: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/
[nodeSelector]: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector
[podSecurityContext]: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
[priorityClass]: https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/#priorityclass
[probe]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/
[pytest]: https://docs.pytest.org/en/latest/
[requirements.txt]: https://github.com/elastic/helm-charts/tree/master/requirements.txt
[resources]: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
[service]: https://kubernetes.io/docs/concepts/services-networking/service/
[serviceAccount]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
[tolerations]: https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/
[updateStrategy]: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#updating-a-deployment
[values.yaml]: https://github.com/elastic/helm-charts/tree/master/apm-server/values.yaml
