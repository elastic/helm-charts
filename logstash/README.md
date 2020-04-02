# Logstash Helm Chart

This functionality is in beta and is subject to change. The design and code is less mature than official GA features and is being provided as-is with no warranties. Beta features are not subject to the support SLA of official GA features.

This helm chart is a lightweight way to configure and run our official [Logstash docker image](https://www.elastic.co/guide/en/logstash/current/docker.html)

## Requirements

* [Helm](https://helm.sh/) >=2.8.0 and <3.0.0 (see parent [README](https://github.com/elastic/helm-charts/tree/master/README.md) for more details)
* Kubernetes >=1.8

## Usage notes and getting started

* This repo includes a number of [example](https://github.com/elastic/helm-charts/tree/master/logstash/examples) configurations which can be used as a reference. They are also used in the automated testing of this chart
* Automated testing of this chart is currently only run against GKE (Google Kubernetes Engine).
* The chart deploys a statefulset and by default will do an automated rolling update of your cluster. It does this by waiting for the cluster health to become green after each instance is updated. If you prefer to update manually you can set [`updateStrategy: OnDelete`](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#on-delete)
* It is important to verify that the JVM heap size in `logstashJavaOpts` and to set the CPU/Memory `resources` to something suitable for your cluster
* We have designed this chart to be very un-opinionated about how to configure Logstash. It exposes ways to set environment variables and mount secrets inside of the container. Doing this makes it much easier for this chart to support multiple versions with minimal changes.
* `logstash.yml` configuration files can be set either by a ConfigMap using `logstashConfig` in `values.yml` or by environment variables using `extraEnvs` in `values.yml`, however Logstash Docker image can't mix both methods as defining settings with environment variables causes `logstash.yml` to be modified in place while using ConfigMap bind-mount the same file (more details in this [Note](https://www.elastic.co/guide/en/logstash/6.7/docker-config.html#docker-env-config)).

## Installing

### Using Helm repository

* Add the elastic helm charts repo
  ```
  helm repo add elastic https://helm.elastic.co
  ```
* Install it
  ```
  helm install --name logstash elastic/logstash

### Using master branch

* Clone the git repo
  ```
  git clone git@github.com:elastic/helm-charts.git
  ```
* Install it
  ```
  helm install --name logstash ./helm-charts/logstash
  ```

## Compatibility

This chart is tested with the latest supported versions. The currently tested versions are:

| 6.x   | 7.x   |
| ----- | ----- |
| 6.8.8 | 7.6.2 |

Examples of installing older major versions can be found in the [examples](https://github.com/elastic/helm-charts/tree/master/logstash/examples) directory.

While only the latest releases are tested, it is possible to easily install old or new releases by overriding the `imageTag`. To install version `7.6.2` of Logstash it would look like this:

```
helm install --name logstash elastic/logstash --set imageTag=7.6.2
```

## Configuration

| Parameter                     | Description                                                                                                                                                                                                                                                                                                                | Default                                                                                                                    |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `antiAffinity`                | Setting this to hard enforces the [anti-affinity rules](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity). If it is set to soft it will be done "best effort". Other values will be ignored.                                                                                  | `hard`                                                                                                                     |
| `antiAffinityTopologyKey`     | The [anti-affinity topology key](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity). By default this will prevent multiple Logstash nodes from running on the same Kubernetes node                                                                                             | `kubernetes.io/hostname`                                                                                                   |
| `extraContainers`             | Templatable string of additional containers to be passed to the `tpl` function                                                                                                                                                                                                                                             | `""`                                                                                                                       |
| `extraEnvs`                   | Extra [environment variables](https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/#using-environment-variables-inside-of-your-config) which will be appended to the `env:` definition for the container                                                                         | `[]`                                                                                                                       |
| `extraInitContainers`         | Templatable string of additional init containers to be passed to the `tpl` function                                                                                                                                                                                                                                        | `""`                                                                                                                       |
| `extraVolumes`                | Templatable string of additional volumes to be passed to the `tpl` function                                                                                                                                                                                                                                                | `""`                                                                                                                       |
| `extraVolumeMounts`           | Templatable string of additional volumeMounts to be passed to the `tpl` function                                                                                                                                                                                                                                           | `""`                                                                                                                       |
| `image`                       | The Logstash docker image                                                                                                                                                                                                                                                                                                  | `docker.elastic.co/logstash/logstash`                                                                                      |
| `imagePullPolicy`             | The Kubernetes [imagePullPolicy](https://kubernetes.io/docs/concepts/containers/images/#updating-images) value                                                                                                                                                                                                             | `IfNotPresent`                                                                                                             |
| `imagePullSecrets`            | Configuration for [imagePullSecrets](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#create-a-pod-that-uses-your-secret) so that you can use a private registry for your image                                                                                                       | `[]`                                                                                                                       |
| `imageTag`                    | The Logstash docker image tag                                                                                                                                                                                                                                                                                              | `7.6.2`                                                                                                                    |
| `httpPort`                    | The http port that Kubernetes will use for the healthchecks and the service.                                                                                                                                                                                                                                               | `9600`                                                                                                                     |
| `extraPorts`                    | An array of extra ports to open on the pod                                                                                                                                                                                                                                                | `[]`                                                                                                                     |
| `labels`                      | Configurable [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) applied to all Logstash pods                                                                                                                                                                                              | `{}`                                                                                                                       |
| `lifecycle`                   | Allows you to add lifecycle configuration. See [values.yaml](https://github.com/elastic/helm-charts/tree/master/logstash/values.yaml) for an example of the formatting.                                                                                                                                                    | `{}`                                                                                                                       |
| `livenessProbe`               | Configuration fields for the [livenessProbe](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/)                                                                                                                                                                                | `failureThreshold: 3`<br>`initialDelaySeconds: 300`<br>`periodSeconds: 10`<br>`successThreshold: 3`<br>`timeoutSeconds: 5` |
| `logstashConfig`              | Allows you to add any config files in `/usr/share/logstash/config/` such as `logstash.yml` and `log4j2.properties`. See [values.yaml](https://github.com/elastic/helm-charts/tree/master/logstash/values.yaml) for an example of the formatting.                                                                           | `{}`                                                                                                                       |
| `logstashJavaOpts`            | Java options for Logstash. This is where you should configure the jvm heap size                                                                                                                                                                                                                                            | `-Xmx1g -Xms1g`                                                                                                            |
| `logstashPipeline`            | Allows you to add any pipeline files in `/usr/share/logstash/pipeline/`.                                                                                                                                                                                                                                                   | `{}`                                                                                                                       |
| `maxUnavailable`              | The [maxUnavailable](https://kubernetes.io/docs/tasks/run-application/configure-pdb/#specifying-a-poddisruptionbudget) value for the pod disruption budget. By default this will prevent Kubernetes from having more than 1 unhealthy pod in the node group                                                                | `1`                                                                                                                        |
| `nodeAffinity`                | Value for the [node affinity settings](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#node-affinity-beta-feature)                                                                                                                                                                                      | `{}`                                                                                                                       |
| `nodeSelector`                | Configurable [nodeSelector](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector) so that you can target specific nodes for your Logstash cluster                                                                                                                                               | `{}`                                                                                                                       |
| `persistence.annotations`     | Additional persistence annotations for the `volumeClaimTemplate`                                                                                                                                                                                                                                                           | `{}`                                                                                                                       |
| `persistence.enabled`         | Enables a persistent volume for Logstash data                                                                                                                                                                                                                                                                              | `false`                                                                                                                    |
| `podAnnotations`              | Configurable [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) applied to all Logstash pods                                                                                                                                                                                    | `{}`                                                                                                                       |
| `podManagementPolicy`         | By default Kubernetes [deploys statefulsets serially](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#pod-management-policies). This deploys them in parallel so that they can discover each other                                                                                                  | `Parallel`                                                                                                                 |
| `podSecurityContext`          | Allows you to set the [securityContext](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-security-context-for-a-pod) for the pod                                                                                                                                                         | `fsGroup: 1000`<br>`runAsUser: 1000`                                                                                       |
| `podSecurityPolicy`           | Configuration for create a pod security policy with minimal permissions to run this Helm chart with `create: true`. Also can be used to reference an external pod security policy with `name: "externalPodSecurityPolicy"`                                                                                                 | `create: false`<br>`name: ""`                                                                                              |
| `priorityClassName`           | The [name of the PriorityClass](https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/#priorityclass). No default is supplied as the PriorityClass must be created first.                                                                                                                              | `""`                                                                                                                       |
| `readinessProbe`              | Configuration fields for the [readinessProbe](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/)                                                                                                                                                                               | `failureThreshold: 3`<br>`initialDelaySeconds: 60`<br>`periodSeconds: 10`<br>`successThreshold: 3`<br>`timeoutSeconds: 5`  |
| `replicas`                    | Kubernetes replica count for the statefulset (i.e. how many pods)                                                                                                                                                                                                                                                          | `1`                                                                                                                        |
| `resources`                   | Allows you to set the [resources](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/) for the statefulset                                                                                                                                                                               | `requests.cpu: 100m`<br>`requests.memory: 1536Mi`<br>`limits.cpu: 1000m`<br>`limits.memory: 1536Mi`                        |
| `schedulerName`               | Name of the [alternate scheduler](https://kubernetes.io/docs/tasks/administer-cluster/configure-multiple-schedulers/#specify-schedulers-for-pods)                                                                                                                                                                          | `""`                                                                                                                       |
| `secretMounts`                | Allows you easily mount a secret as a file inside the statefulset. Useful for mounting certificates and other secrets. See [values.yaml](https://github.com/elastic/helm-charts/tree/master/logstash/values.yaml) for an example                                                                                           | `[]`                                                                                                                       |
| `securityContext`             | Allows you to set the [securityContext](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-security-context-for-a-container) for the container                                                                                                                                             | `capabilities.drop:[ALL]`<br>`runAsNonRoot: true`<br>`runAsUser: 1000`                                                     |
| `terminationGracePeriod`      | The [terminationGracePeriod](https://kubernetes.io/docs/concepts/workloads/pods/pod/#termination-of-pods) in seconds used when trying to stop the pod                                                                                                                                                                      | `120`                                                                                                                      |
| `tolerations`                 | Configurable [tolerations](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/)                                                                                                                                                                                                                        | `[]`                                                                                                                       |
| `updateStrategy`              | The [updateStrategy](https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/#updating-statefulsets) for the statefulset. By default Kubernetes will wait for the cluster to be green after upgrading each pod. Setting this to `OnDelete` will allow you to manually delete each pod during upgrades | `RollingUpdate`                                                                                                            |
| `volumeClaimTemplate`         | Configuration for the [volumeClaimTemplate for statefulsets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#stable-storage). You will want to adjust the storage (default `30Gi`) and the `storageClassName` if you are using a different storage class                                            | `accessModes: [ "ReadWriteOnce" ]`<br>`resources.requests.storage: 1Gi`                                                    |
| `rbac`                        | Configuration for creating a role, role binding and service account as part of this helm chart with `create: true`. Also can be used to reference an external service account with `serviceAccountName: "externalServiceAccountName"`.                                                                                     | `create: false`<br>`serviceAccountName: ""`                                                                                |
| `fullnameOverride`            | Overrides the full name of the resources. If not set the name will default to "`.Release.Name`-`.Values.nameOverride or .Chart.Name`"                                                                                                                                                                                      | `""`                                                                                                                       |

## Try it out

In [examples/](https://github.com/elastic/helm-charts/tree/master/logstash/examples) you will find some example configurations. These examples are used for the automated testing of this helm chart

### Default

To deploy a cluster with all default values and run the integration tests

```
cd examples/default
make
```

### FAQ

#### How to install plugins?

The [recommended](https://www.elastic.co/guide/en/logstash/current/docker-config.html#_custom_images) way to install plugins into our docker images is to create a custom docker image.

The Dockerfile would look something like:

```
ARG logstash_version
FROM docker.elastic.co/logstash/logstash:${logstash_version}

RUN bin/logstash-plugin install logstash-output-kafka
```

And then updating the `image` in values to point to your custom image.

There are a couple reasons we recommend this.

1. Tying the availability of Logstash to the download service to install plugins is not a great idea or something that we recommend. Especially in Kubernetes where it is normal and expected for a container to be moved to another host at random times.
2. Mutating the state of a running docker image (by installing plugins) goes against best practices of containers and immutable infrastructure.

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

Integration tests are run using [goss](https://github.com/aelsabbahy/goss/blob/master/docs/manual.md) which is a serverspec like tool written in golang. See [goss.yaml](https://github.com/elastic/helm-charts/tree/master/logstash/examples/default/test/goss.yaml) for an example of what the tests look like.

To run the goss tests against the default example:

```
cd examples/default
make goss
```
