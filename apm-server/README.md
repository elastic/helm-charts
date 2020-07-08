# APM Server Helm Chart

This Helm chart is a lightweight way to configure and run our official
[APM Server Docker image][].

**Warning**: This functionality is in alpha and is subject to change.
The design and code is less mature than official GA features and is being
provided as-is with no warranties. Alpha features are not subject to the support
SLA of official GA features (see [supported configurations][] for more details).

**Warning**: This branch is used for development, please use [7.8.0][] release
for released version.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Requirements](#requirements)
- [Installing](#installing)
  - [Install released version using Helm repository](#install-released-version-using-helm-repository)
  - [Install development version using master branch](#install-development-version-using-master-branch)
- [Upgrading](#upgrading)
- [Usage notes](#usage-notes)
- [Configuration](#configuration)
- [FAQ](#faq)
  - [How to use APM Server with Elasticsearch with security (authentication and TLS) enabled?](#how-to-use-apm-server-with-elasticsearch-with-security-authentication-and-tls-enabled)
  - [How to install OSS version of APM Server?](#how-to-install-oss-version-of-apm-server)
- [Contributing](#contributing)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!-- Use this to update TOC: -->
<!-- docker run --rm -it -v $(pwd):/usr/src jorgeandrada/doctoc --github -->


## Requirements

* Kubernetes >= 1.9
* [Helm][] >= 2.8.0

See [supported configurations][] for more details.


## Installing

### Install released version using Helm repository

* Add the Elastic Helm charts repo:
`helm repo add elastic https://helm.elastic.co`

* Install it: `helm install --name apm-server elastic/apm-server`

### Install development version using master branch

* Clone the git repo: `git clone git@github.com:elastic/helm-charts.git`

* Install it: `helm install --name apm-server ./helm-charts/apm-server  --set imageTag=8.0.0-SNAPSHOT`


## Upgrading

Please always check [CHANGELOG.md][] and [BREAKING_CHANGES.md][] before
upgrading to a new chart version.


## Usage notes

* The default APM Server configuration file for this chart is configured to use
an Elasticsearch endpoint as configured by the rest of these Helm charts. This
can easily be overridden in the config value `apmConfig.apm-server.yml`.

* Automated testing of this chart is currently only run against GKE (Google
Kubernetes Engine).

* This repo includes a number of [examples][] configurations which can be used
as a reference. They are also used in the automated testing of this chart.


## Configuration

| Parameter                | Description                                                                                                                                                | Default                            |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| `affinity`               | Configurable [affinity][]                                                                                                                                  | `{}`                               |
| `apmConfig`              | Allows you to add any config files in `/usr/share/apm-server/config` such as `apm-server.yml`                                                              | see [values.yaml][]                |
| `autoscaling`            | Enable the [horizontal pod autoscaler][]                                                                                                                   | `enabled: false`                   |
| `envFrom`                | Templatable string to be passed to the [environment from variables][] which will be appended to the `envFrom:` definition for the container                | `[]`                               |
| `extraContainers`        | Templatable string of additional containers to be passed to the `tpl` function                                                                             | `""`                               |
| `extraEnvs`              | Extra [environment variables][] which will be appended to the `env:` definition for the container                                                          | `[]`                               |
| `extraInitContainers`    | Templatable string of additional containers to be passed to the `tpl` function                                                                             | `""`                               |
| `extraVolumeMounts`      | List of additional `volumeMounts`                                                                                                                          | `[]`                               |
| `extraVolumes`           | List of additional `volumes`                                                                                                                               | `[]`                               |
| `fullnameOverride`       | Overrides the full name of the resources. If not set the name will default to `.Release.Name` - `.Values.nameOverride` or `.Chart.Name`                    | `""`                               |
| `imagePullPolicy`        | The Kubernetes [imagePullPolicy][] value                                                                                                                   | `IfNotPresent`                     |
| `imagePullSecrets`       | Configuration for [imagePullSecrets][] so that you can use a private registry for your image                                                               | `[]`                               |
| `imageTag`               | The APM Server Docker image tag                                                                                                                            | `8.0.0-SNAPSHOT`                            |
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
| `serviceAccountAnnotations` | Annotations to be added to the ServiceAccount that is created by this chart.                                                                            | `{}`
| `service`                | Configurable [service][] to expose the APM Server service. See [values.yaml][] for an example                                                              | see [values.yaml][]                |
| `terminationGracePeriod` | Termination period (in seconds) to wait before killing APM Server pod process on pod shutdown                                                              | `30`                               |
| `tolerations`            | Configurable [tolerations][]                                                                                                                               | `[]`                               |
| `updateStrategy`         | Allows you to change the default [updateStrategy][] for the deployment                                                                                     | see [values.yaml][]                |


## FAQ

### How to use APM Server with Elasticsearch with security (authentication and TLS) enabled?

This Helm chart can use existing [Kubernetes secrets][] to setup
credentials or certificates for examples. These secrets should be created
outside of this chart and accessed using [environment variables][] and volumes.

An example can be found in [examples/security][].

### How to install OSS version of APM Server?

Deploying OSS version of Elasticsearch can be done by setting `image` value to
[APM Server OSS Docker image][]

An example of APM Server deployment using OSS version can be found in
[examples/oss][].


## Contributing

Please check [CONTRIBUTING.md][] before any contribution or for any questions
about our development and testing process.


[7.8.0]: https://github.com/elastic/helm-charts/blob/7.8.0/apm-server/README.md
[BREAKING_CHANGES.md]: https://github.com/elastic/helm-charts/blob/master/BREAKING_CHANGES.md
[CHANGELOG.md]: https://github.com/elastic/helm-charts/blob/master/CHANGELOG.md
[CONTRIBUTING.md]: https://github.com/elastic/helm-charts/blob/master/CONTRIBUTING.md
[affinity]: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity
[annotations]: https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/
[apm server docker image]: https://www.elastic.co/guide/en/apm/server/current/running-on-docker.html
[apm server oss docker image]: https://www.docker.elastic.co/#apm-server-7-7-0-oss
[default elasticsearch helm chart]: https://github.com/elastic/helm-charts/tree/master/elasticsearch/README.md#default
[environment variables]: https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/#using-environment-variables-inside-of-your-config
[environment from variables]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/#configure-all-key-value-pairs-in-a-configmap-as-container-environment-variables
[examples]: https://github.com/elastic/helm-charts/tree/master/apm-server/examples
[examples/oss]: https://github.com/elastic/helm-charts/tree/master/apm-server/examples/oss
[examples/security]: https://github.com/elastic/helm-charts/tree/master/apm-server/examples/security
[helm]: https://helm.sh
[horizontal pod autoscaler]: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/
[imagePullPolicy]: https://kubernetes.io/docs/concepts/containers/images/#updating-images
[imagePullSecrets]: https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#create-a-pod-that-uses-your-secret
[ingress]: https://kubernetes.io/docs/concepts/services-networking/ingress/
[kubernetes secrets]: https://kubernetes.io/docs/concepts/configuration/secret/
[labels]: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
[lifecycle hooks]: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/
[nodeSelector]: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector
[podSecurityContext]: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
[priorityClass]: https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/#priorityclass
[probe]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/
[resources]: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
[service]: https://kubernetes.io/docs/concepts/services-networking/service/
[serviceAccount]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
[supported configurations]: https://github.com/elastic/helm-charts/tree/master/README.md#supported-configurations
[tolerations]: https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/
[updateStrategy]: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#updating-a-deployment
[values.yaml]: https://github.com/elastic/helm-charts/tree/master/apm-server/values.yaml
