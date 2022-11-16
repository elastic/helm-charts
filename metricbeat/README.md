# Metricbeat Helm Chart

[![Build Status](https://img.shields.io/jenkins/s/https/devops-ci.elastic.co/job/elastic+helm-charts+main.svg)](https://devops-ci.elastic.co/job/elastic+helm-charts+main/) [![Artifact HUB](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/elastic)](https://artifacthub.io/packages/search?repo=elastic)

This Helm chart is a lightweight way to configure and run our official
[Metricbeat Docker image][].

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
  - [Install development version using main branch](#install-development-version-using-main-branch)
- [Upgrading](#upgrading)
- [Usage notes](#usage-notes)
- [Configuration](#configuration)
- [FAQ](#faq)
  - [How to use Metricbeat with Elasticsearch with security (authentication and TLS) enabled?](#how-to-use-metricbeat-with-elasticsearch-with-security-authentication-and-tls-enabled)
  - [How to install OSS version of Metricbeat?](#how-to-install-oss-version-of-metricbeat)
  - [How to use Kubelet read-only port instead of secure port?](#how-to-use-kubelet-read-only-port-instead-of-secure-port)
  - [Why is Metricbeat host.name field set to Kubernetes pod name?](#why-is-metricbeat-hostname-field-set-to-kubernetes-pod-name)
  - [How do I get multiple beats agents working with hostNetworking enabled?](#how-do-i-get-multiple-beats-agents-working-with-hostnetworking-enabled)
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

* Add the Prometheus community Helm charts repo (required for kube-state-metrics chart dependency):
`helm repo add prometheus-community https://prometheus-community.github.io/helm-charts`

* Install it: `helm install metricbeat elastic/metricbeat`

### Install development version using main branch

* Clone the git repo: `git clone git@github.com:elastic/helm-charts.git`

* Add the Prometheus community Helm charts repo (required for kube-state-metrics chart dependency):
`helm repo add prometheus-community https://prometheus-community.github.io/helm-charts`

* Install it: `helm install metricbeat ./helm-charts/metricbeat --set imageTag=8.5.1`


## Upgrading

Please always check [CHANGELOG.md][] and [BREAKING_CHANGES.md][] before
upgrading to a new chart version.


## Usage notes

* The default Metricbeat configuration file for this chart is configured to use
an Elasticsearch endpoint. Without any additional changes, Metricbeat will send
documents to the service URL that the Elasticsearch Helm chart sets up by
default. The Elasticsearch credentials are also retrieved from
`elasticsearch-master-credentials` Secret from Elasticsearch chart by default.
You may either set the `ELASTICSEARCH_HOSTS`, `ELASTICSEARCH_USER` and
`ELASTICSEARCH_PASSWORD` environment variables in `extraEnvs` to override this
or modify the default `metricbeatConfig` to change this behavior.
* This chart disables the [HostNetwork][] setting by default for compatibility
reasons with the majority of kubernetes providers and scenarios. Some kubernetes
providers may not allow enabling `hostNetwork` and deploying multiple Metricbeat
pods on the same node isn't possible with `hostNetwork` However Metricbeat does
recommend activating it. If your kubernetes provider is compatible with
`hostNetwork` and you don't need to run multiple Metricbeat DaemonSets, you can
activate it by setting `hostNetworking: true` in [values.yaml][].
* This repo includes several [examples][] of configurations that can be used
as a reference. They are also used in the automated testing of this chart.


## Configuration

| Parameter                      | Description                                                                                                                                                                  | Default                              |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| `clusterRoleRules`             | Configurable [cluster role rules][] that Metricbeat uses to access Kubernetes resources                                                                                      | see [values.yaml][]                  |
| `daemonset.annotations`        | Configurable [annotations][] for Metricbeat daemonset                                                                                                                        | `{}`                                 |
| `daemonset.labels`             | Configurable [labels][] applied to all Metricbeat DaemonSet pods                                                                                                             | `{}`                                 |
| `daemonset.affinity`           | Configurable [affinity][] for Metricbeat daemonset                                                                                                                           | `{}`                                 |
| `daemonset.enabled`            | If true, enable daemonset                                                                                                                                                    | `true`                               |
| `daemonset.envFrom`            | Templatable string of `envFrom` to be passed to the  [environment from variables][] which will be appended to Metricbeat container for DaemonSet                             | `[]`                                 |
| `daemonset.extraEnvs`          | Extra [environment variables][] which will be appended to Metricbeat container for DaemonSet                                                                                 | see [values.yaml][]                  |
| `daemonset.extraVolumeMounts`  | Templatable string of additional `volumeMounts` to be passed to the `tpl` function or DaemonSet                                                                              | `[]`                                 |
| `daemonset.extraVolumes`       | Templatable string of additional `volumes` to be passed to the `tpl` function or DaemonSet                                                                                   | `[]`                                 |
| `daemonset.hostAliases`        | Configurable [hostAliases][] for Metricbeat DaemonSet                                                                                                                        | `[]`                                 |
| `daemonset.hostNetworking`     | Enable Metricbeat DaemonSet to use `hostNetwork`                                                                                                                             | `false`                              |
| `daemonset.metricbeatConfig`   | Allows you to add any config files in `/usr/share/metricbeat` such as `metricbeat.yml` for Metricbeat DaemonSet                                                              | see [values.yaml][]                  |
| `daemonset.nodeSelector`       | Configurable [nodeSelector][] for Metricbeat DaemonSet                                                                                                                       | `{}`                                 |
| `daemonset.resources`          | Allows you to set the [resources][] for Metricbeat DaemonSet                                                                                                                 | see [values.yaml][]                  |
| `daemonset.secretMounts`       | Allows you easily mount a secret as a file inside the DaemonSet. Useful for mounting certificates and other secrets. See [values.yaml][] for an example                      | `[]`                                 |
| `daemonset.securityContext`    | Configurable [securityContext][] for Metricbeat DaemonSet pod execution environment                                                                                          | see [values.yaml][]                  |
| `daemonset.tolerations`        | Configurable [tolerations][] for Metricbeat DaemonSet                                                                                                                        | `[]`                                 |
| `deployment.annotations`       | Configurable [annotations][] for Metricbeat Deployment                                                                                                                       | `{}`                                 |
| `deployment.labels`            | Configurable [labels][] applied to all Metricbeat Deployment pods                                                                                                            | `{}`                                 |
| `deployment.affinity`          | Configurable [affinity][] for Metricbeat Deployment                                                                                                                          | `{}`                                 |
| `deployment.enabled`           | If true, enable deployment                                                                                                                                                   | `true`                               |
| `deployment.envFrom`           | Templatable string of `envFrom` to be passed to the  [environment from variables][] which will be appended to Metricbeat container for Deployment                            | `[]`                                 |
| `deployment.extraEnvs`         | Extra [environment variables][] which will be appended to Metricbeat container for Deployment                                                                                | see [values.yaml][]                  |
| `deployment.extraVolumeMounts` | Templatable string of additional `volumeMounts` to be passed to the `tpl` function or DaemonSet                                                                              | `[]`                                 |
| `deployment.extraVolumes`      | Templatable string of additional `volumes` to be passed to the `tpl` function or Deployment                                                                                  | `[]`                                 |
| `deployment.hostAliases`       | Configurable [hostAliases][] for Metricbeat Deployment                                                                                                                       | `[]`                                 |
| `deployment.metricbeatConfig`  | Allows you to add any config files in `/usr/share/metricbeat` such as `metricbeat.yml` for Metricbeat Deployment                                                             | see [values.yaml][]                  |
| `deployment.nodeSelector`      | Configurable [nodeSelector][] for Metricbeat Deployment                                                                                                                      | `{}`                                 |
| `deployment.resources`         | Allows you to set the [resources][] for Metricbeat Deployment                                                                                                                | see [values.yaml][]                  |
| `deployment.secretMounts`      | Allows you easily mount a secret as a file inside the Deployment Useful for mounting certificates and other secrets. See [values.yaml][] for an example                      | `[]`                                 |
| `deployment.securityContext`   | Configurable [securityContext][] for Metricbeat Deployment pod execution environment                                                                                         | see [values.yaml][]                  |
| `deployment.tolerations`       | Configurable [tolerations][] for Metricbeat Deployment                                                                                                                       | `[]`                                 |
| `extraContainers`              | Templatable string of additional containers to be passed to the `tpl` function                                                                                               | `""`                                 |
| `extraInitContainers`          | Templatable string of additional containers to be passed to the `tpl` function                                                                                               | `""`                                 |
| `fullnameOverride`             | Overrides the full name of the resources. If not set the name will default to " `.Release.Name` - `.Values.nameOverride or .Chart.Name` "                                    | `""`                                 |
| `hostPathRoot`                 | Fully-qualified [hostPath][] that will be used to persist Metricbeat registry data                                                                                           | `/var/lib`                           |
| `imagePullPolicy`              | The Kubernetes [imagePullPolicy][] value                                                                                                                                     | `IfNotPresent`                       |
| `imagePullSecrets`             | Configuration for [imagePullSecrets][] so that you can use a private registry for your image                                                                                 | `[]`                                 |
| `imageTag`                     | The Metricbeat Docker image tag                                                                                                                                              | `8.5.1`                              |
| `image`                        | The Metricbeat Docker image                                                                                                                                                  | `docker.elastic.co/beats/metricbeat` |
| `kube_state_metrics.enabled`   | Install [kube-state-metrics][] chart as a dependency                                                                                                                         | `true`                               |
| `kube_state_metrics.host`      | Define kube-state-metrics endpoint for an existing deployment. Works only if `kube_state_metrics.enabled: false`                                                             | `""`                                 |
| `livenessProbe`                | Parameters to pass to liveness [probe][] checks for values such as timeouts and thresholds                                                                                   | see [values.yaml][]                  |
| `managedServiceAccount`        | Whether the `serviceAccount` should be managed by this helm chart. Set this to `false` in order to manage your own service account and related roles                         | `true`                               |
| `nameOverride`                 | Overrides the chart name for resources. If not set the name will default to `.Chart.Name`                                                                                    | `""`                                 |
| `podAnnotations`               | Configurable [annotations][] applied to all Metricbeat pods                                                                                                                  | `{}`                                 |
| `priorityClassName`            | The name of the [PriorityClass][]. No default is supplied as the PriorityClass must be created first                                                                         | `""`                                 |
| `readinessProbe`               | Parameters to pass to readiness [probe][] checks for values such as timeouts and thresholds                                                                                  | see [values.yaml][]                  |
| `replicas`                     | The replica count for the Metricbeat deployment talking to kube-state-metrics                                                                                                | `1`                                  |
| `secrets`                      | Allows creating a secret from variables or a file. To add secrets from file, add suffix `.filepath` to the key of the secret key. The value will be encoded to base64.       | See [values.yaml][]                  |
| `serviceAccount`               | Custom [serviceAccount][] that Metricbeat will use during execution. By default will use the service account created by this chart                                           | `""`                                 |
| `serviceAccountAnnotations`    | Annotations to be added to the ServiceAccount that is created by this chart.                                                                                                 | `{}`                                 |
| `terminationGracePeriod`       | Termination period (in seconds) to wait before killing Metricbeat pod process on pod shutdown                                                                                | `30`                                 |
| `updateStrategy`               | The [updateStrategy][] for the DaemonSet By default Kubernetes will kill and recreate pods on updates. Setting this to `OnDelete` will require that pods be deleted manually | `RollingUpdate`                      |


## FAQ

### How to use Metricbeat with Elasticsearch with security (authentication and TLS) enabled?

This Helm chart can use existing [Kubernetes secrets][] to setup
credentials or certificates for examples. These secrets should be created
outside of this chart and accessed using [environment variables][] and volumes.

An example can be found in [examples/security][].

### How to install OSS version of Metricbeat?

Deploying OSS version of Metricbeat can be done by setting `image` value to
[Metricbeat OSS Docker image][]

An example of Metricbeat deployment using OSS version can be found in
[examples/oss][].

### How to use Kubelet read-only port instead of secure port?

Default Metricbeat configuration has been switched to Kubelet secure port
(10250/TCP) instead of read-only port (10255/TCP) in [#471][] because read-only
port usage is now discouraged and not enabled by default in most Kubernetes
configurations.

However, if you need to use read-only port, you can replace
`hosts: ["https://${NODE_NAME}:10250"]` by `hosts: ["${NODE_NAME}:10255"]` and
comment `bearer_token_file` and `ssl.verification_mode` in
`daemonset.metricbeatConfig` in [values.yaml][].

### Why is Metricbeat host.name field set to Kubernetes pod name?

The default Metricbeat configuration is using Metricbeat pod name for
`agent.hostname` and `host.name` fields. The `hostname` of the Kubernetes nodes
can be find in `kubernetes.node.name` field. If you would like to have
`agent.hostname` and `host.name` fields set to the hostname of the nodes, you'll
need to set `daemonset.hostNetworking` value to true.

Note that enabling [hostNetwork][] make Metricbeat pod use the host network
namespace which gives it access to the host loopback device, services listening
on localhost, could be used to snoop on network activity of other pods on the
same node.

### How do I get multiple beats agents working with hostNetworking enabled?

The default http port for multiple beats agents may be on the same port, for
example, Filebeats and Metricbeats both default to 5066. When `hostNetworking`
is enabled this will cause collisions when standing up the http server. The work
around for this is to set `http.port` in the config file for one of the beats agent
to use a different port.


## Contributing

Please check [CONTRIBUTING.md][] before any contribution or for any questions
about our development and testing process.

[#471]: https://github.com/elastic/helm-charts/pull/471
[affinity]: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity
[annotations]: https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/
[BREAKING_CHANGES.md]: https://github.com/elastic/helm-charts/blob/main/BREAKING_CHANGES.md
[CHANGELOG.md]: https://github.com/elastic/helm-charts/blob/main/CHANGELOG.md
[cluster role rules]: https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-and-clusterrole
[CONTRIBUTING.md]: https://github.com/elastic/helm-charts/blob/main/CONTRIBUTING.md
[eck-charts]: https://github.com/elastic/cloud-on-k8s/tree/master/deploy
[elastic cloud on kubernetes]: https://github.com/elastic/cloud-on-k8s
[environment from variables]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/#configure-all-key-value-pairs-in-a-configmap-as-container-environment-variables
[environment variables]: https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/#using-environment-variables-inside-of-your-config
[examples]: https://github.com/elastic/helm-charts/tree/main/metricbeat/examples
[examples/oss]: https://github.com/elastic/helm-charts/tree/main/metricbeat/examples/oss
[examples/security]: https://github.com/elastic/helm-charts/tree/main/metricbeat/examples/security
[hostAliases]: https://kubernetes.io/docs/concepts/services-networking/add-entries-to-pod-etc-hosts-with-host-aliases/
[hostNetwork]: https://kubernetes.io/docs/concepts/policy/pod-security-policy/#host-namespaces
[hostPath]: https://kubernetes.io/docs/concepts/storage/volumes/#hostpath
[imagePullPolicy]: https://kubernetes.io/docs/concepts/containers/images/#updating-images
[imagePullSecrets]: https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#create-a-pod-that-uses-your-secret
[kube-state-metrics]: https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-state-metrics
[kubernetes secrets]: https://kubernetes.io/docs/concepts/configuration/secret/
[labels]: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
[metricbeat docker image]: https://www.elastic.co/guide/en/beats/metricbeat/current/running-on-docker.html
[metricbeat oss docker image]: https://www.docker.elastic.co/r/beats/metricbeat-oss
[nodeSelector]: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector
[priorityClass]: https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/#priorityclass
[probe]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes
[resources]: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
[securityContext]: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
[serviceAccount]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
[supported configurations]: https://github.com/elastic/helm-charts/tree/main/README.md#supported-configurations
[tolerations]: https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/
[updateStrategy]: https://kubernetes.io/docs/tasks/manage-daemon/update-daemon-set/#daemonset-update-strategy
[values.yaml]: https://github.com/elastic/helm-charts/tree/main/metricbeat/values.yaml
