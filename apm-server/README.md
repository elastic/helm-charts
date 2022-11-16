# APM Server Helm Chart

[![Build Status](https://img.shields.io/jenkins/s/https/devops-ci.elastic.co/job/elastic+helm-charts+main.svg)](https://devops-ci.elastic.co/job/elastic+helm-charts+main/) [![Artifact HUB](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/elastic)](https://artifacthub.io/packages/search?repo=elastic)

This Helm chart is a lightweight way to configure and run our official
[APM Server Docker image][].

> **Warning**
> When it comes to running the Elastic on Kubernetes infrastructure, we
> recommend [Elastic Cloud on Kubernetes][] (ECK) as the best way to run and manage
> the Elastic Stack.
>
> ECK offers many operational benefits for both our basic-tier and our
> enterprise-tier customers, such as spinning up cluster nodes that were lost on
> failed infrastructure, seamless upgrades, rolling cluster changes, and much
> much more.
>
> With the release of the Elastic Stack Helm charts for Elastic version 8.5.1,
> we are handing over the ongoing maintenance of our Elastic Stack Helm charts
> to the community and contributors. This repository will finally be archived
> after 6 months time. Elastic Stacks deployed on Kubernetes through Helm charts
> will still be fully supported under EOL limitations.
>
> Since we want to provide an even better experience for our customers by
> running the Elastic Stack on Kubernetes, we will continue maintaining the
> Helm charts applicable to ECK Custom Resources. These charts can be found in
> the [ECK repository][eck-charts].
>
> Helm charts will currently be maintained for ECK Enterprise-tier customers,
> however, we encourage the community to engage with the existing Helm charts
> for the Elastic Stack and continue supporting their ongoing maintenance.
>
> See <https://github.com/elastic/helm-charts/issues/1731> for more details.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Requirements](#requirements)
- [Installing](#installing)
  - [Install a released version using the Helm repository](#install-a-released-version-using-the-helm-repository)
  - [Install a development version using the main branch](#install-a-development-version-using-the-main-branch)
- [Upgrading](#upgrading)
- [Usage notes](#usage-notes)
- [Configuration](#configuration)
- [FAQ](#faq)
  - [How to use APM Server with Elasticsearch with security (authentication and TLS) enabled?](#how-to-use-apm-server-with-elasticsearch-with-security-authentication-and-tls-enabled)
- [Contributing](#contributing)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!-- Use this to update TOC: -->
<!-- docker run --entrypoint doctoc --rm -it -v $(pwd):/usr/src jorgeandrada/doctoc README.md --github --no-title -->


## Requirements

See [supported configurations][] for more details.


## Installing

### Install a released version using the Helm repository

* Add the Elastic Helm charts repo:
`helm repo add elastic https://helm.elastic.co`

* Install it `helm install apm-server elastic/apm-server`


### Install a development version using the main branch

* Clone the git repo: `git clone git@github.com:elastic/helm-charts.git`

* Install it: `helm install apm-server ./helm-charts/apm-server --set imageTag=8.5.1`


## Upgrading

Please always check [CHANGELOG.md][] and [BREAKING_CHANGES.md][] before
upgrading to a new chart version.


## Usage notes

* The default APM Server configuration file for this chart is configured to use
an Elasticsearch endpoint as configured by the rest of these Helm charts. This
can easily be overridden in the config value `apmConfig.apm-server.yml`.

* Automated testing of this chart is currently only run against GKE (Google
Kubernetes Engine).

* This repo includes several [examples][] of configurations that can be used as a
reference. They are also used in the automated testing of this chart.


## Configuration

| Parameter                   | Description                                                                                                                                                | Default                            |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| `affinity`                  | Configurable [affinity][]                                                                                                                                  | `{}`                               |
| `apmConfig`                 | Allows you to add any config files in `/usr/share/apm-server/config` such as `apm-server.yml`                                                              | see [values.yaml][]                |
| `autoscaling`               | Enable the [horizontal pod autoscaler][]                                                                                                                   | see [values.yaml][]                |
| `envFrom`                   | Templatable string to be passed to the [environment from variables][] which will be appended to the `envFrom:` definition for the container                | `[]`                               |
| `extraContainers`           | Templatable string of additional containers to be passed to the `tpl` function                                                                             | `""`                               |
| `extraEnvs`                 | Extra [environment variables][] which will be appended to the `env:` definition for the container                                                          | see [values.yaml][]                |
| `extraInitContainers`       | Templatable string of additional containers to be passed to the `tpl` function                                                                             | `""`                               |
| `extraVolumeMounts`         | List of additional `volumeMounts`                                                                                                                          | `[]`                               |
| `extraVolumes`              | List of additional `volumes`                                                                                                                               | `[]`                               |
| `fullnameOverride`          | Overrides the full name of the resources. If not set the name will default to `.Release.Name` - `.Values.nameOverride` or `.Chart.Name`                    | `""`                               |
| `hostAliases`               | Configurable [hostAliases][]                                                                                                                               | `[]`                               |
| `imagePullPolicy`           | The Kubernetes [imagePullPolicy][] value                                                                                                                   | `IfNotPresent`                     |
| `imagePullSecrets`          | Configuration for [imagePullSecrets][] so that you can use a private registry for your image                                                               | `[]`                               |
| `imageTag`                  | The APM Server Docker image tag                                                                                                                            | `8.5.1`                            |
| `image`                     | The APM Server Docker image                                                                                                                                | `docker.elastic.co/apm/apm-server` |
| `ingress`                   | Configurable [ingress][] to expose the APM Server service                                                                                                  | see [values.yaml][]                |
| `labels`                    | Configurable [labels][] applied to all APM server pods                                                                                                     | `{}`                               |
| `lifecycle`                 | Configurable [lifecycle hooks][]                                                                                                                           | `false`                            |
| `livenessProbe`             | Parameters to pass to liveness [probe][] checks for values such as timeouts and thresholds                                                                 | see [values.yaml][]                |
| `managedServiceAccount`     | Whether the `serviceAccount` should be managed by this Helm chart. Set this to `false` in order to manage your own service account and related roles       | `true`                             |
| `nameOverride`              | Overrides the chart name for resources. If not set the name will default to `.Chart.Name`                                                                  | `""`                               |
| `nodeSelector`              | Configurable [nodeSelector][]                                                                                                                              | `{}`                               |
| `podAnnotations`            | Configurable [annotations][] applied to all APM Server pods                                                                                                | `{}`                               |
| `podSecurityContext`        | Configurable [podSecurityContext][] for APM Server pod execution environment                                                                               | see [values.yaml][]                |
| `priorityClassName`         | The name of the [PriorityClass][]. No default is supplied as the `PriorityClass` must be created first                                                     | `""`                               |
| `readinessProbe`            | Parameters to pass to readiness [probe][] checks for values such as timeouts and thresholds                                                                | see [values.yaml][]                |
| `replicas`                  | Number of APM servers to run                                                                                                                               | `1`                                |
| `resources`                 | Allows you to set the [resources][] for the `Deployment`                                                                                                   | see [values.yaml][]                |
| `secretMounts`              | Allows you easily mount a secret as a file inside the `Deployment`. Useful for mounting certificates and other secrets. See [values.yaml][] for an example | `[]`                               |
| `serviceAccount`            | Custom [serviceAccount][] that APM Server will use during execution. By default will use the `serviceAccount` created by this chart                        | `""`                               |
| `serviceAccountAnnotations` | Annotations to be added to the ServiceAccount that is created by this chart.                                                                               | `{}`                               |
| `service`                   | Configurable [service][] to expose the APM Server service. See [values.yaml][] for an example                                                              | see [values.yaml][]                |
| `terminationGracePeriod`    | Termination period (in seconds) to wait before killing APM Server pod process on pod shutdown                                                              | `30`                               |
| `tolerations`               | Configurable [tolerations][]                                                                                                                               | `[]`                               |
| `updateStrategy`            | Allows you to change the default [updateStrategy][] for the deployment                                                                                     | see [values.yaml][]                |


## FAQ

### How to use APM Server with Elasticsearch with security (authentication and TLS) enabled?

This Helm chart can use existing [Kubernetes secrets][] to setup
credentials or certificates for examples. These secrets should be created
outside of this chart and accessed using [environment variables][] and volumes.

An example can be found in [examples/security][].


## Contributing

Please check [CONTRIBUTING.md][] before any contribution or for any questions
about our development and testing process.

[affinity]: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity
[annotations]: https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/
[apm server docker image]: https://www.elastic.co/guide/en/apm/server/current/running-on-docker.html
[BREAKING_CHANGES.md]: https://github.com/elastic/helm-charts/blob/main/BREAKING_CHANGES.md
[CHANGELOG.md]: https://github.com/elastic/helm-charts/blob/main/CHANGELOG.md
[CONTRIBUTING.md]: https://github.com/elastic/helm-charts/blob/main/CONTRIBUTING.md
[eck-charts]: https://github.com/elastic/cloud-on-k8s/tree/master/deploy
[elastic cloud on kubernetes]: https://github.com/elastic/cloud-on-k8s
[environment from variables]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/#configure-all-key-value-pairs-in-a-configmap-as-container-environment-variables
[environment variables]: https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/#using-environment-variables-inside-of-your-config
[examples]: https://github.com/elastic/helm-charts/tree/main/apm-server/examples
[examples/security]: https://github.com/elastic/helm-charts/tree/main/apm-server/examples/security
[horizontal pod autoscaler]: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/
[hostAliases]: https://kubernetes.io/docs/concepts/services-networking/add-entries-to-pod-etc-hosts-with-host-aliases/
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
[supported configurations]: https://github.com/elastic/helm-charts/tree/main/README.md#supported-configurations
[tolerations]: https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/
[updateStrategy]: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#updating-a-deployment
[values.yaml]: https://github.com/elastic/helm-charts/tree/main/apm-server/values.yaml
