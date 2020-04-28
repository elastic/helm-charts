# Filebeat Helm Chart
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Requirements](#requirements)
- [Installing](#installing)
  - [Using Helm repository](#using-helm-repository)
  - [Using the 7.7 branch](#using-the-77-branch)
- [Upgrading](#upgrading)
- [Usage notes](#usage-notes)
- [Configuration](#configuration)
- [Examples](#examples)
  - [Default](#default)
- [Contributing](#contributing)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!-- Use this to update TOC: -->
<!-- docker run --rm -it -v $(pwd):/usr/src jorgeandrada/doctoc --github -->


This functionality is in beta and is subject to change. The design and code is
less mature than official GA features and is being provided as-is with no
warranties. Beta features are not subject to the support SLA of official GA
features.

This Helm chart is a lightweight way to configure and run our official
[Filebeat Docker image][].


## Requirements

* [Helm][] >=2.8.0 and <3.0.0 (see [parent README][] for more details)
* Kubernetes >=1.9


## Installing

This chart is tested with the latest 7.7.0-SNAPSHOT versions.

### Using Helm repository

* Add the Elastic Helm charts repo:
`helm repo add elastic https://helm.elastic.co`

* Install the latest 7.7 release:
`helm install --name filebeat elastic/filebeat --version=7.7.0`

### Using the 7.7 branch

* Clone the git repo and checkout the right branch:

  ```shell
  git clone git@github.com:elastic/helm-charts.git
  cd helm-charts
  git checkout -b 7.7 origin/7.7
  ````

* Install the latest 7.7.0-SNAPSHOT:
`helm install --name filebeat ./helm-charts/filebeat`


## Upgrading

Please always check [CHANGELOG.md][] and [BREAKING_CHANGES.md][] before
upgrading to a new chart version.


## Usage notes

* The default Filebeat configuration file for this chart is configured to use an
Filebeat endpoint. Without any additional changes, Filebeat will send
documents to the service URL that the Filebeat Helm chart sets up by
default. You may either set the `FILEBEAT_HOSTS` environment variable in
`extraEnvs` to override this endpoint or modify the default `filebeatConfig` to
change this behavior.
* The default Filebeat configuration file is also configured to capture
container logs and enrich them with Kubernetes metadata by default. This will
capture all container logs in the cluster.
* This chart disables the [HostNetwork][] setting by default for compatibility
reasons with the majority of kubernetes providers and scenarios. Some kubernetes
providers may not allow enabling `hostNetwork` and deploying multiple Filebeat
pods on the same node isn't possible with `hostNetwork` However Filebeat does
recommend activating it. If your kubernetes provider is compatible with
`hostNetwork` and you don't need to run multiple Filebeat DaemonSets, you can
activate it by setting `hostNetworking: true` in [values.yaml][].


## Configuration

| Parameter                | Description                                                                                                                                                                     | Default                            |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| `affinity`               | Configurable [affinity][]                                                                                                                                                       | `{}`                               |
| `envFrom`                | Templatable string of envFrom to be passed to the [environment from variables][] which will be appended to the `envFrom:` definition for the container                          | `[]`                               |
| `extraContainers`        | List of additional init containers to be added at the DaemonSet                                                                                                                 | `""`                               |
| `extraEnvs`              | Extra [environment variables][] which will be appended to the `env:` definition for the container                                                                               | `[]`                               |
| `extraInitContainers`    | List of additional init containers to be added at the DaemonSet. It also accepts a templatable string of additional containers to be passed to the `tpl` function               | `[]`                               |
| `extraVolumeMounts`      | List of additional volumeMounts to be mounted on the DaemonSet                                                                                                                  | `[]`                               |
| `extraVolumes`           | List of additional volumes to be mounted on the DaemonSet                                                                                                                       | `[]`                               |
| `filebeatConfig`         | Allows you to add any config files in `/usr/share/filebeat` such as `filebeat.yml`                                                                                              | see [values.yaml][]                |
| `fullnameOverride`       | Overrides the full name of the resources. If not set the name will default to " `.Release.Name` - `.Values.nameOverride or .Chart.Name` "                                       | `""`                               |
| `hostNetworking`         | Use host networking in the DaemonSet so that hostname is reported correctly                                                                                                     | `false`                            |
| `hostPathRoot`           | Fully-qualified [hostPath][] that will be used to persist Filebeat registry data                                                                                                | `/var/lib`                         |
| `imagePullPolicy`        | The Kubernetes [imagePullPolicy][] value                                                                                                                                        | `IfNotPresent`                     |
| `imagePullSecrets`       | Configuration for [imagePullSecrets][] so that you can use a private registry for your image                                                                                    | `[]`                               |
| `imageTag`               | The Filebeat Docker image tag                                                                                                                                                   | `7.7.0-SNAPSHOT`                            |
| `image`                  | The Filebeat Docker image                                                                                                                                                       | `docker.elastic.co/beats/filebeat` |
| `labels`                 | Configurable [labels][] applied to all Filebeat pods                                                                                                                            | `{}`                               |
| `livenessProbe`          | Parameters to pass to liveness [probe][] checks for values such as timeouts and thresholds                                                                                      | see [values.yaml][]                |
| `managedServiceAccount`  | Whether the `serviceAccount` should be managed by this Helm chart. Set this to `false` in order to manage your own service account and related roles                            | `true`                             |
| `nameOverride`           | Overrides the chart name for resources. If not set the name will default to `.Chart.Name`                                                                                       | `""`                               |
| `nodeSelector`           | Configurable [nodeSelector][]                                                                                                                                                   | `{}`                               |
| `podAnnotations`         | Configurable [annotations][] applied to all Filebeat pods                                                                                                                       | `{}`                               |
| `podSecurityContext`     | Configurable [podSecurityContext][] for Filebeat pod execution environment                                                                                                      | see [values.yaml][]                |
| `priorityClassName`      | The name of the [PriorityClass][]. No default is supplied as the PriorityClass must be created first                                                                            | `""`                               |
| `readinessProbe`         | Parameters to pass to readiness [probe][] checks for values such as timeouts and thresholds                                                                                     | see [values.yaml][]                |
| `resources`              | Allows you to set the [resources][] for the `DaemonSet`                                                                                                                         | see [values.yaml][]                |
| `secretMounts`           | Allows you easily mount a secret as a file inside the `DaemonSet`. Useful for mounting certificates and other secrets. See [values.yaml][] for an example                       | `[]`                               |
| `serviceAccount`         | Custom [serviceAccount][] that Filebeat will use during execution. By default will use the service account created by this chart                                                | `""`                               |
| `terminationGracePeriod` | Termination period (in seconds) to wait before killing Filebeat pod process on pod shutdown                                                                                     | `30`                               |
| `tolerations`            | Configurable [tolerations][]                                                                                                                                                    | `[]`                               |
| `updateStrategy`         | The [updateStrategy][] for the `DaemonSet`. By default Kubernetes will kill and recreate pods on updates. Setting this to `OnDelete` will require that pods be deleted manually | `RollingUpdate`                    |


## Examples

In [examples][] you will find some example configurations. These examples are
used for the automated testing of this Helm chart.

### Default

* Deploy the [default Filebeat Helm chart][].
* Deploy Filebeat with the default values:

  ```
  cd examples/default
  make
  ```

* You can now setup a port forward for Filebeat to observe Filebeat
indices:

  ```
  kubectl port-forward svc/filebeat-master 9200
  curl localhost:9200/_cat/indices
  ```


## Contributing

Please check [CONTRIBUTING.md][] before any contribution or for any questions
about our development and testing process.


[BREAKING_CHANGES.md]: https://github.com/elastic/helm-charts/blob/master/BREAKING_CHANGES.md
[CHANGELOG.md]: https://github.com/elastic/helm-charts/blob/master/CHANGELOG.md
[CONTRIBUTING.md]: https://github.com/elastic/helm-charts/blob/master/CONTRIBUTING.md
[affinity]: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity
[annotations]: https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/
[default Filebeat Helm chart]: https://github.com/elastic/helm-charts/tree/7.7/filebeat/README.md#default
[environment variables]: https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/#using-environment-variables-inside-of-your-config
[examples]: https://github.com/elastic/helm-charts/tree/7.7/filebeat/examples
[filebeat docker image]: https://www.elastic.co/guide/en/beats/filebeat/current/running-on-docker.html
[helm]: https://helm.sh
[hostNetwork]: https://kubernetes.io/docs/concepts/policy/pod-security-policy/#host-namespaces
[hostPath]: https://kubernetes.io/docs/concepts/storage/volumes/#hostpath
[imagePullPolicy]: https://kubernetes.io/docs/concepts/containers/images/#updating-images
[imagePullSecrets]: https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#create-a-pod-that-uses-your-secret
[labels]: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
[parent readme]: https://github.com/elastic/helm-charts/tree/7.7/README.md
[nodeSelector]: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector
[podSecurityContext]: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
[priorityClass]: https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/#priorityclass
[probe]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/
[resources]: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
[serviceAccount]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
[tolerations]: https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/
[updateStrategy]: https://kubernetes.io/docs/tasks/manage-daemon/update-daemon-set/#daemonset-update-strategy
[values.yaml]: https://github.com/elastic/helm-charts/tree/7.7/filebeat/values.yaml
