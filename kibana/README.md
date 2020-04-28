# Kibana Helm Chart
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Requirements](#requirements)
- [Installing](#installing)
  - [Using Helm repository](#using-helm-repository)
  - [Using the 7.7 branch](#using-the-77-branch)
- [Upgrading](#upgrading)
- [Configuration](#configuration)
  - [Deprecated](#deprecated)
- [Examples](#examples)
  - [Default](#default)
  - [Security](#security)
- [FAQ](#faq)
  - [How to install plugins?](#how-to-install-plugins)
- [Contributing](#contributing)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!-- Use this to update TOC: -->
<!-- docker run --rm -it -v $(pwd):/usr/src jorgeandrada/doctoc --github -->


This functionality is in beta and is subject to change. The design and code is
less mature than official GA features and is being provided as-is with no
warranties. Beta features are not subject to the support SLA of official GA
features.

This Helm chart is a lightweight way to configure and run our official
[Kibana Docker image][].


## Requirements

* [Helm][] >=2.8.0 and <3.0.0 (see [parent README][] for more details)
* Kubernetes >=1.9


## Installing

This chart is tested with the latest 7.7.0-SNAPSHOT versions.

### Using Helm repository

* Add the Elastic Helm charts repo:
`helm repo add elastic https://helm.elastic.co`

* Install the latest 7.7 release:
`helm install --name kibana elastic/kibana --version=7.7.0`

### Using the 7.7 branch

* Clone the git repo and checkout the right branch:

  ```shell
  git clone git@github.com:elastic/helm-charts.git
  cd helm-charts
  git checkout -b 7.7 origin/7.7
  ````

* Install the latest 7.7.0-SNAPSHOT:
`helm install --name kibana ./helm-charts/kibana`


## Upgrading

Please always check [CHANGELOG.md][] and [BREAKING_CHANGES.md][] before
upgrading to a new chart version.


## Configuration

| Parameter             | Description                                                                                                                                                                                    | Default                            |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| `affinity`            | Configurable [affinity][]                                                                                                                                                                      | `{}`                               |
| `elasticsearchHosts`  | The URLs used to connect to Elasticsearch                                                                                                                                                      | `http://elasticsearch-master:9200` |
| `envFrom`             | Templatable string to be passed to the [environment from variables][] which will be appended to the `envFrom:` definition for the container                                                    | `[]`                               |
| `extraContainers`     | Templatable string of additional containers to be passed to the `tpl` function                                                                                                                 | `""`                               |
| `extraEnvs`           | Extra [environment variables][] which will be appended to the `env:` definition for the container                                                                                              | see [values.yaml][]                |
| `extraInitContainers` | Templatable string of additional containers to be passed to the `tpl` function                                                                                                                 | `""`                               |
| `fullnameOverride`    | Overrides the full name of the resources. If not set the name will default to " `.Release.Name` - `.Values.nameOverride orChart.Name` "                                                        | `""`                               |
| `healthCheckPath`     | The path used for the readinessProbe to check that Kibana is ready. If you are setting `server.basePath` you will also need to update this to `/${basePath}/app/kibana`                        | `/app/kibana`                      |
| `httpPort`            | The http port that Kubernetes will use for the healthchecks and the service                                                                                                                    | `5601`                             |
| `imagePullPolicy`     | The Kubernetes [imagePullPolicy][]value                                                                                                                                                        | `IfNotPresent`                     |
| `imagePullSecrets`    | Configuration for [imagePullSecrets][] so that you can use a private registry for your image                                                                                                   | `[]`                               |
| `imageTag`            | The Kibana Docker image tag                                                                                                                                                                    | `7.7.0-SNAPSHOT`                            |
| `image`               | The Kibana Docker image                                                                                                                                                                        | `docker.elastic.co/kibana/kibana`  |
| `ingress`             | Configurable [ingress][] to expose the Kibana service.                                                                                                                                         | see [values.yaml][]                |
| `kibanaConfig`        | Allows you to add any config files in `/usr/share/kibana/config/` such as `kibana.yml` See [values.yaml][] for an example of the formatting                                                    | `{}`                               |
| `labels`              | Configurable [labels][] applied to all Kibana pods                                                                                                                                             | `{}`                               |
| `lifecycle`           | Allows you to add lifecycle configuration. See [values.yaml][] for an example of the formatting                                                                                                | `{}`                               |
| `nameOverride`        | Overrides the chart name for resources. If not set the name will default to `.Chart.Name`                                                                                                      | `""`                               |
| `nodeSelector`        | Configurable [nodeSelector][] so that you can target specific nodes for your Kibana instances                                                                                                  | `{}`                               |
| `podAnnotations`      | Configurable [annotations][] applied to all Kibana pods                                                                                                                                        | `{}`                               |
| `podSecurityContext`  | Allows you to set the [securityContext][] for the pod                                                                                                                                          | see [values.yaml][]                |
| `priorityClassName`   | The name of the [PriorityClass][]. No default is supplied as the PriorityClass must be created first                                                                                           | `""`                               |
| `protocol`            | The protocol that will be used for the readinessProbe. Change this to `https` if you have `server.ssl.enabled: true` set                                                                       | `http`                             |
| `readinessProbe`      | Configuration for the readiness [probe][]                                                                                                                                                      | see [values.yaml][]                |
| `replicas`            | Kubernetes replica count for the Deployment (i.e. how many pods)                                                                                                                               | `1`                                |
| `resources`           | Allows you to set the [resources][] for the Deployment                                                                                                                                         | see [values.yaml][]                |
| `secretMounts`        | Allows you easily mount a secret as a file inside the Deployment. Useful for mounting certificates and other secrets. See [values.yaml][] for an example                                       | `[]`                               |
| `securityContext`     | Allows you to set the [securityContext][] for the container                                                                                                                                    | see [values.yaml][]                |
| `serverHost`          | The [server.host][] Kibana setting. This is set explicitly so that the default always matches what comes with the Docker image                                                                 | `0.0.0.0`                          |
| `serviceAccount`      | Allows you to overwrite the "default" [serviceAccount][] for the pod                                                                                                                           | `[]`                               |
| `service`             | Configurable [service][] to expose the Kibana service.                                                                                                                                         | see [values.yaml][]                |
| `tolerations`         | Configurable [tolerations][])                                                                                                                                                                  | `[]`                               |
| `updateStrategy`      | Allows you to change the default [updateStrategy][] for the Deployment. A [standard upgrade][] of Kibana requires a full stop and start which is why the default strategy is set to `Recreate` | `type: Recreate`                   |

### Deprecated

| Parameter          | Description                                                                          | Default |
|--------------------|--------------------------------------------------------------------------------------|---------|
| `elasticsearchURL` | The URL used to connect to Elasticsearch. needs to be used for Kibana versions < 6.6 | `""`    |


## Examples

In [examples][] you will find some example configurations. These examples are
used for the automated testing of this Helm chart.

### Default

* Deploy the [default Elasticsearch Helm chart][].
* Deploy Kibana with the default values:

  ```
  cd examples/default
  make
  ```

* You can now setup a port forward and access Kibana at http://localhost:5601:

  ```
  kubectl port-forward deployment/helm-kibana-default-kibana 5601
  ```

### Security

* Deploy a [security enabled Elasticsearch cluster][].
* Deploy Kibana with the security example:

  ```
  cd examples/security
  make
  ```

* Setup a port forward and access Kibana at https://localhost:5601:

  ```
  # Setup the port forward
  kubectl port-forward deployment/helm-kibana-security-kibana 5601

  # Run this in a seperate terminal
  # Get the auto generated password
  password=$(kubectl get secret elastic-credentials -o jsonpath='{.data.password}' | base64 --decode)
  echo password

  # Test Kibana is working with curl or access it with your browser at https://localhost:5601
  # The example certificate is self signed so you may see a warning about the certificate
  curl -I -k -u elastic:$password https://localhost:5601/app/kibana
  ```


## FAQ

### How to install plugins?

The recommended way to install plugins into our Docker images is to create a
custom Docker image.

The Dockerfile would look something like:

```
ARG kibana_version
FROM docker.elastic.co/kibana/kibana:${kibana_version}

RUN bin/kibana-plugin install <plugin_url>
```

And then updating the `image` in values to point to your custom image.

There are a couple reasons we recommend this:

1. Tying the availability of Kibana to the download service to install plugins
is not a great idea or something that we recommend. Especially in Kubernetes
where it is normal and expected for a container to be moved to another host at
random times.
2. Mutating the state of a running Docker image (by installing plugins) goes
against best practices of containers and immutable infrastructure.


## Contributing

Please check [CONTRIBUTING.md][] before any contribution or for any questions
about our development and testing process.


[BREAKING_CHANGES.md]: https://github.com/elastic/helm-charts/blob/master/BREAKING_CHANGES.md
[CHANGELOG.md]: https://github.com/elastic/helm-charts/blob/master/CHANGELOG.md
[CONTRIBUTING.md]: https://github.com/elastic/helm-charts/blob/master/CONTRIBUTING.md
[annotations]: https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/
[default elasticsearch helm chart]: https://github.com/elastic/helm-charts/tree/7.7/elasticsearch/README.md#default
[environment variables]: https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/#using-environment-variables-inside-of-your-config
[kibana docker image]: https://www.elastic.co/guide/en/kibana/current/docker.html
[examples]: https://github.com/elastic/helm-charts/tree/7.7/kibana/examples
[helm]: https://helm.sh
[imagePullPolicy]: https://kubernetes.io/docs/concepts/containers/images/#updating-images
[imagePullSecrets]: https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#create-a-pod-that-uses-your-secret
[ingress]: https://kubernetes.io/docs/concepts/services-networking/ingress/
[labels]: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
[nodeSelector]: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector
[parent readme]: https://github.com/elastic/helm-charts/tree/7.7/README.md
[priorityClass]: https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/#priorityclass
[probe]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/
[resources]: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
[security enabled elasticsearch cluster]: https://github.com/elastic/helm-charts/tree/7.7/elasticsearch/README.md#security
[securityContext]: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-security-context-for-a-pod
[server.host]: https://www.elastic.co/guide/en/kibana/current/settings.html
[service]: https://kubernetes.io/docs/concepts/services-networking/service/
[serviceAccount]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
[standard upgrade]: https://www.elastic.co/guide/en/kibana/current/upgrade-standard.html
[tolerations]: https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/
[updateStrategy]: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#updating-a-deployment
[values.yaml]: https://github.com/elastic/helm-charts/tree/7.7/kibana/values.yaml
