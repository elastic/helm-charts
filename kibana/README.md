# Kibana Helm Chart

[![Build Status](https://img.shields.io/jenkins/s/https/devops-ci.elastic.co/job/elastic+helm-charts+main.svg)](https://devops-ci.elastic.co/job/elastic+helm-charts+main/) [![Artifact HUB](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/elastic)](https://artifacthub.io/packages/search?repo=elastic)

This Helm chart is a lightweight way to configure and run our official
[Kibana Docker image][].

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
  - [How to deploy this chart on a specific K8S distribution?](#how-to-deploy-this-chart-on-a-specific-k8s-distribution)
  - [How to use Kibana with security (authentication and TLS) enabled?](#how-to-use-kibana-with-security-authentication-and-tls-enabled)
  - [How to install plugins?](#how-to-install-plugins)
  - [How to import objects post-deployment?](#how-to-import-objects-post-deployment)
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

* Install it: `helm install kibana elastic/kibana`


### Install a development version using the main branch

* Clone the git repo: `git clone git@github.com:elastic/helm-charts.git`

* Install it: `helm install kibana ./helm-charts/kibana --set imageTag=8.5.1`

## Upgrading

Please always check [CHANGELOG.md][] and [BREAKING_CHANGES.md][] before
upgrading to a new chart version.


## Usage notes

* Automated testing of this chart is currently only run against GKE (Google
Kubernetes Engine).

* This repo includes several [examples][] of configurations that can be used
as a reference. They are also used in the automated testing of this chart.


## Configuration

| Parameter                                 | Description                                                                                                                                                                                    | Default                             |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| `affinity`                                | Configurable [affinity][]                                                                                                                                                                      | `{}`                                |
| `annotations`                             | Configurable [annotations][] on the deployment object                                                                                                                                          | `{}`                                |
| `automountToken`                          | Whether or not to automount the service account token in the Pod                                                                                                                               | `true`                              |
| `elasticsearchHosts`                      | The URLs used to connect to Elasticsearch                                                                                                                                                      | `https://elasticsearch-master:9200` |
| `elasticsearchCertificateSecret`          | The name of the K8S [secret][kubernetes secrets] that contains the Elasticsearch certificate                                                                                                   | `elasticsearch-master-certs`        |
| `elasticsearchCertificateAuthoritiesFile` | The name of the certificate file into the `elasticsearchCertificateSecret` K8S `secret`                                                                                                        | `ca.crt`                            |
| `elasticsearchCredentialSecret`           | The name of the K8S [secret][kubernetes secrets] that contains the Elasticsearch credentials                                                                                                   | `elasticsearch-master-credentials`  |
| `envFrom`                                 | Templatable string to be passed to the [environment from variables][] which will be appended to the `envFrom:` definition for the container                                                    | `[]`                                |
| `extraContainers`                         | Templatable string of additional containers to be passed to the `tpl` function                                                                                                                 | `[]`                                |
| `extraEnvs`                               | Extra [environment variables][] which will be appended to the `env:` definition for the container                                                                                              | see [values.yaml][]                 |
| `extraInitContainers`                     | Templatable string of additional containers to be passed to the `tpl` function                                                                                                                 | `[]`                                |
| `extraVolumeMounts`                       | Configuration for additional `volumeMounts`                                                                                                                                                    | `[]`                                |
| `extraVolumes`                            | Configuration for additional `volumes`                                                                                                                                                         | `[]`                                |
| `fullnameOverride`                        | Overrides the full name of the resources. If not set the name will default to " `.Release.Name` - `.Values.nameOverride orChart.Name` "                                                        | `""`                                |
| `healthCheckPath`                         | The path used for the readinessProbe to check that Kibana is ready. If you are setting `server.basePath` you will also need to update this to `/${basePath}/app/kibana`                        | `/app/kibana`                       |
| `hostAliases`                             | Configurable [hostAliases][]                                                                                                                                                                   | `[]`                                |
| `httpPort`                                | The http port that Kubernetes will use for the healthchecks and the service                                                                                                                    | `5601`                              |
| `imagePullPolicy`                         | The Kubernetes [imagePullPolicy][]value                                                                                                                                                        | `IfNotPresent`                      |
| `imagePullSecrets`                        | Configuration for [imagePullSecrets][] so that you can use a private registry for your image                                                                                                   | `[]`                                |
| `imageTag`                                | The Kibana Docker image tag                                                                                                                                                                    | `8.5.1`                             |
| `image`                                   | The Kibana Docker image                                                                                                                                                                        | `docker.elastic.co/kibana/kibana`   |
| `ingress`                                 | Configurable [ingress][] to expose the Kibana service.                                                                                                                                         | see [values.yaml][]                 |
| `kibanaConfig`                            | Allows you to add any config files in `/usr/share/kibana/config/` such as `kibana.yml` See [values.yaml][] for an example of the formatting                                                    | `{}`                                |
| `labels`                                  | Configurable [labels][] applied to all Kibana pods                                                                                                                                             | `{}`                                |
| `lifecycle`                               | Allows you to add [lifecycle hooks][]. See [values.yaml][] for an example of the formatting                                                                                                    | `{}`                                |
| `nameOverride`                            | Overrides the chart name for resources. If not set the name will default to `.Chart.Name`                                                                                                      | `""`                                |
| `nodeSelector`                            | Configurable [nodeSelector][] so that you can target specific nodes for your Kibana instances                                                                                                  | `{}`                                |
| `podAnnotations`                          | Configurable [annotations][] applied to all Kibana pods                                                                                                                                        | `{}`                                |
| `podSecurityContext`                      | Allows you to set the [securityContext][] for the pod                                                                                                                                          | see [values.yaml][]                 |
| `priorityClassName`                       | The name of the [PriorityClass][]. No default is supplied as the PriorityClass must be created first                                                                                           | `""`                                |
| `protocol`                                | The protocol that will be used for the readinessProbe. Change this to `https` if you have `server.ssl.enabled: true` set                                                                       | `http`                              |
| `readinessProbe`                          | Configuration for the readiness [probe][]                                                                                                                                                      | see [values.yaml][]                 |
| `replicas`                                | Kubernetes replica count for the Deployment (i.e. how many pods)                                                                                                                               | `1`                                 |
| `resources`                               | Allows you to set the [resources][] for the Deployment                                                                                                                                         | see [values.yaml][]                 |
| `secretMounts`                            | Allows you easily mount a secret as a file inside the Deployment. Useful for mounting certificates and other secrets. See [values.yaml][] for an example                                       | `[]`                                |
| `securityContext`                         | Allows you to set the [securityContext][] for the container                                                                                                                                    | see [values.yaml][]                 |
| `serverHost`                              | The [server.host][] Kibana setting. This is set explicitly so that the default always matches what comes with the Docker image                                                                 | `0.0.0.0`                           |
| `serviceAccount`                          | Allows you to overwrite the "default" [serviceAccount][] for the pod                                                                                                                           | `[]`                                |
| `service`                                 | Configurable [service][] to expose the Kibana service.                                                                                                                                         | see [values.yaml][]                 |
| `tolerations`                             | Configurable [tolerations][])                                                                                                                                                                  | `[]`                                |
| `updateStrategy`                          | Allows you to change the default [updateStrategy][] for the Deployment. A [standard upgrade][] of Kibana requires a full stop and start which is why the default strategy is set to `Recreate` | `type: Recreate`                    |

## FAQ

### How to deploy this chart on a specific K8S distribution?

This chart is highly tested with [GKE][], but some K8S distribution also
requires specific configurations.

We provide examples of configuration for the following K8S providers:

- [OpenShift][]

### How to use Kibana with security (authentication and TLS) enabled?

Starting with 8.x the [default Elasticsearch Helm chart][] is automatically
configured with security enabled (authentification and TLS).

As the Elasticsearch credentials and certificates are available in some
[Kubernetes secrets][] generated by the Elasticsearch chart, the Kibana chart is
configured to read these secrets to configure the secure connection to
Elasticsearch (The secrets names can be overrided in the chart
[values][values.yaml]).

Therefore, Kibana is automatically configured to required authentication. You
can connect to Kibana with the `elastic` user account that comes from
Elasticsearch. The password can be find in the `elasticsearchCredentialSecret`
(see the [chart notes][]).

:warning: Note that in production, the `elastic` user should only be used to
create new users.

This Helm chart can also use existing [Kubernetes secrets][] to set up TLS
certificates. These secrets should be created outside of this chart and accessed
using the [environment variables][] and volumes.

An example can be found in [examples/security][].

### How to install plugins?

The recommended way to install plugins into our Docker images is to create a
custom Docker image.

The Dockerfile would look something like this:

```
ARG kibana_version
FROM docker.elastic.co/kibana/kibana:${kibana_version}

RUN bin/kibana-plugin install <plugin_url>
```

And then updating the `image` in values to point to your custom image.

There are a couple of reasons we recommend this:

1. Tying the availability of Kibana to the download service to install plugins
is not a great idea or something that we recommend. Especially in Kubernetes
where it is normal and expected for a container to be moved to another host at
random times.
2. Mutating the state of a running Docker image (by installing plugins) goes
against the best practices of containers and immutable infrastructure.

### How to import objects post-deployment?

You can use `postStart` [lifecycle hooks][] to run code triggered after a
container is created.

Here is an example of `postStart` hook to import an index-pattern and a
dashboard:

```yaml
lifecycle:
  postStart:
    exec:
      command:
        - bash
        - -c
        - |
          #!/bin/bash
          # Import a dashboard
          KB_URL=http://localhost:5601
          while [[ "$(curl -s -o /dev/null -w '%{http_code}\n' -L $KB_URL)" != "200" ]]; do sleep 1; done
          curl -XPOST "$KB_URL/api/kibana/dashboards/import" -H "Content-Type: application/json" -H 'kbn-xsrf: true' -d'{"objects":[{"type":"index-pattern","id":"my-pattern","attributes":{"title":"my-pattern-*"}},{"type":"dashboard","id":"my-dashboard","attributes":{"title":"Look at my dashboard"}}]}'
```


## Contributing

Please check [CONTRIBUTING.md][] before any contribution or for any questions
about our development and testing process.

[affinity]: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity
[annotations]: https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/
[BREAKING_CHANGES.md]: https://github.com/elastic/helm-charts/blob/main/BREAKING_CHANGES.md
[CHANGELOG.md]: https://github.com/elastic/helm-charts/blob/main/CHANGELOG.md
[chart notes]: https://github.com/elastic/helm-charts/tree/main/kibana/templates/NOTES.txt
[CONTRIBUTING.md]: https://github.com/elastic/helm-charts/blob/main/CONTRIBUTING.md
[default elasticsearch helm chart]: https://github.com/elastic/helm-charts/tree/main/elasticsearch/README.md#default
[eck-charts]: https://github.com/elastic/cloud-on-k8s/tree/master/deploy
[elastic cloud on kubernetes]: https://github.com/elastic/cloud-on-k8s
[environment from variables]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/#configure-all-key-value-pairs-in-a-configmap-as-container-environment-variables
[environment variables]: https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/#using-environment-variables-inside-of-your-config
[examples]: https://github.com/elastic/helm-charts/tree/main/kibana/examples
[examples/security]: https://github.com/elastic/helm-charts/tree/main/kibana/examples/security
[gke]: https://cloud.google.com/kubernetes-engine
[helm]: https://helm.sh
[hostAliases]: https://kubernetes.io/docs/concepts/services-networking/add-entries-to-pod-etc-hosts-with-host-aliases/
[imagePullPolicy]: https://kubernetes.io/docs/concepts/containers/images/#updating-images
[imagePullSecrets]: https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#create-a-pod-that-uses-your-secret
[ingress]: https://kubernetes.io/docs/concepts/services-networking/ingress/
[kibana docker image]: https://www.elastic.co/guide/en/kibana/current/docker.html
[kubernetes secrets]: https://kubernetes.io/docs/concepts/configuration/secret/
[labels]: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
[lifecycle hooks]: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/
[nodeSelector]: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector
[openshift]: https://github.com/elastic/helm-charts/tree/main/kibana/examples/openshift
[priorityClass]: https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/#priorityclass
[probe]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/
[resources]: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
[securityContext]: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-security-context-for-a-pod
[server.host]: https://www.elastic.co/guide/en/kibana/current/settings.html
[service]: https://kubernetes.io/docs/concepts/services-networking/service/
[serviceAccount]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
[standard upgrade]: https://www.elastic.co/guide/en/kibana/current/upgrade-standard.html
[supported configurations]: https://github.com/elastic/helm-charts/tree/main/README.md#supported-configurations
[tolerations]: https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/
[updateStrategy]: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#updating-a-deployment
[values.yaml]: https://github.com/elastic/helm-charts/tree/main/kibana/values.yaml
