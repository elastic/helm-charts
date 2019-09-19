# Kibana Helm Chart

This functionality is in beta and is subject to change. The design and code is less mature than official GA features and is being provided as-is with no warranties. Beta features are not subject to the support SLA of official GA features.

This helm chart is a lightweight way to configure and run our official [Kibana docker image](https://www.elastic.co/guide/en/kibana/current/docker.html)

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
  helm install --name kibana elastic/kibana
  ```

## Compatibility

This chart is tested with the latest supported versions. The currently tested versions are:

| 6.x   | 7.x   |
| ----- | ----- |
| 6.8.3 | 7.3.2 |

Examples of installing older major versions can be found in the [examples](./examples) directory.

While only the latest releases are tested, it is possible to easily install old or new releases by overriding the `imageTag`. To install version `7.3.2` of Kibana it would look like this:

```
helm install --name kibana elastic/kibana --set imageTag=7.3.2
```

## Configuration

| Parameter                 | Description                                                                                                                                                                                                                                                                                                                                                    | Default                                                                                                                   |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `elasticsearchHosts`      | The URLs used to connect to Elasticsearch.                                                                                                                                                                                                                                                                                                                     | `http://elasticsearch-master:9200`                                                                                        |
| `elasticsearchURL`        | The URL used to connect to Elasticsearch. Deprecated, needs to be used for Kibana versions < 6.6                                                                                                                                                                                                                                                               |                                                                                                                           |
| `replicas`                | Kubernetes replica count for the deployment (i.e. how many pods)                                                                                                                                                                                                                                                                                               | `1`                                                                                                                       |
| `extraEnvs`               | Extra [environment variables](https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/#using-environment-variables-inside-of-your-config) which will be appended to the `env:` definition for the container                                                                                                             | `[]`                                                                                                                      |
| `secretMounts`            | Allows you easily mount a secret as a file inside the deployment. Useful for mounting certificates and other secrets. See [values.yaml](./values.yaml) for an example                                                                                                                                                                                          | `[]`                                                                                                                      |
| `image`                   | The Kibana docker image                                                                                                                                                                                                                                                                                                                                        | `docker.elastic.co/kibana/kibana`                                                                                         |
| `imageTag`                | The Kibana docker image tag                                                                                                                                                                                                                                                                                                                                    | `7.3.2`                                                                                                                   |
| `imagePullPolicy`         | The Kubernetes [imagePullPolicy](https://kubernetes.io/docs/concepts/containers/images/#updating-images) value                                                                                                                                                                                                                                                 | `IfNotPresent`                                                                                                            |
| `podAnnotations`          | Configurable [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) applied to all Kibana pods                                                                                                                                                                                                                          | `{}`                                                                                                                      |
| `resources`               | Allows you to set the [resources](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/) for the statefulset                                                                                                                                                                                                                   | `requests.cpu: 100m`<br>`requests.memory: 500Mi`<br>`limits.cpu: 1000m`<br>`limits.memory: 2Gi`                             |
| `protocol`                | The protocol that will be used for the readinessProbe. Change this to `https` if you have `server.ssl.enabled: true` set                                                                                                                                                                                                                                       | `http`                                                                                                                    |
| `serverHost`              | The [`server.host`](https://www.elastic.co/guide/en/kibana/current/settings.html) Kibana setting. This is set explicitly so that the default always matches what comes with the docker image.                                                                                                                                                                  | `0.0.0.0`                                                                                                                 |
| `healthCheckPath`         | The path used for the readinessProbe to check that Kibana is ready. If you are setting `server.basePath` you will also need to update this to `/${basePath}/app/kibana`                                                                                                                                                                                        | `/app/kibana`                                                                                                             |
| `kibanaConfig`            | Allows you to add any config files in `/usr/share/kibana/config/` such as `kibana.yml`. See [values.yaml](./values.yaml) for an example of the formatting.                                                                                                                                                                                                     | `{}`                                                                                                                      |
| `podSecurityContext`      | Allows you to set the [securityContext](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-security-context-for-a-pod) for the pod                                                                                                                                                                                             | `fsGroup: 1000`                                                                                                           |
| `securityContext`         | Allows you to set the [securityContext](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-security-context-for-a-container) for the container                                                                                                                                                                                 | `capabilities.drop:[ALL]`<br>`runAsNonRoot: true`<br>`runAsUser: 1000`                                                    |
| `serviceAccount`          | Allows you to overwrite the "default" [serviceAccount](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) for the pod                                                                                                                                                                                                        | `[]`                                                                                                                      |
| `priorityClassName`       | The [name of the PriorityClass](https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/#priorityclass). No default is supplied as the PriorityClass must be created first.                                                                                                                                                                  | `""`                                                                                                                      |
| `antiAffinityTopologyKey` | The [anti-affinity topology key](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity). By default this will prevent multiple Kibana instances from running on the same Kubernetes node                                                                                                                               | `kubernetes.io/hostname`                                                                                                  |
| `antiAffinity`            | Setting this to hard enforces the [anti-affinity rules](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity). If it is set to soft it will be done "best effort"                                                                                                                                                     | `hard`                                                                                                                    |
| `httpPort`                | The http port that Kubernetes will use for the healthchecks and the service.                                                                                                                                                                                                                                                                                   | `5601`                                                                                                                    |
| `maxUnavailable`          | The [maxUnavailable](https://kubernetes.io/docs/tasks/run-application/configure-pdb/#specifying-a-poddisruptionbudget) value for the pod disruption budget. By default this will prevent Kubernetes from having more than 1 unhealthy pod                                                                                                                      | `1`                                                                                                                       |
| `updateStrategy`          | Allows you to change the default update [strategy](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#updating-a-deployment) for the deployment. A [standard upgrade](https://www.elastic.co/guide/en/kibana/current/upgrade-standard.html) of Kibana requires a full stop and start which is why the default strategy is set to `Recreate` | `Recreate`                                                                                                                |
| `readinessProbe`          | Configuration for the [readinessProbe](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/)                                                                                                                                                                                                                          | `failureThreshold: 3`<br>`initialDelaySeconds: 10`<br>`periodSeconds: 10`<br>`successThreshold: 3`<br>`timeoutSeconds: 5` |
| `imagePullSecrets`        | Configuration for [imagePullSecrets](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#create-a-pod-that-uses-your-secret) so that you can use a private registry for your image                                                                                                                                           | `[]`                                                                                                                      |
| `nodeSelector`            | Configurable [nodeSelector](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector) so that you can target specific nodes for your Kibana instances                                                                                                                                                                                   | `{}`                                                                                                                      |
| `tolerations`             | Configurable [tolerations](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/)                                                                                                                                                                                                                                                            | `[]`                                                                                                                      |
| `ingress`                 | Configurable [ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) to expose the Kibana service. See [`values.yaml`](./values.yaml) for an example                                                                                                                                                                                       | `enabled: false`                                                                                                          |
| `service`                 | Configurable [service](https://kubernetes.io/docs/concepts/services-networking/service/) to expose the Kibana service. See [`values.yaml`](./values.yaml) for an example                                                                                                                                                                                       | `type: ClusterIP`<br>`port: 5601`<br>`nodePort:`<br>`annotations: {}`                                                     |
| `labels`                  | Configurable [label](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) applied to all Kibana pods                                                                                                                                                                                                                                     | `{}`                                                                                                                      |

## Examples

In [examples/](./examples) you will find some example configurations. These examples are used for the automated testing of this helm chart

### Default

* Deploy the [default Elasticsearch helm chart](../elasticsearch/README.md#default)
* Deploy Kibana with the default values
  ```
  cd examples/default
  make
  ```
* You can now setup a port forward and access Kibana at http://localhost:5601
  ```
  kubectl port-forward deployment/helm-kibana-default-kibana 5601
  ```

### Security

* Deploy a [security enabled Elasticsearch cluster](../elasticsearch/README.md#security)
* Deploy Kibana with the security example
  ```
  cd examples/security
  make
  ```
* Setup a port forward and access Kibana at https://localhost:5601
  ```
  # Setup the port forward
  kubectl port-forward deployment/helm-kibana-security-kibana 5601

  # Run this in a seperate terminal
  # Get the auto generated password
  password=$(kubectl get secret elastic-credentials -o jsonpath='{.data.password}' | base64 --decode)
  echo $password

  # Test Kibana is working with curl or access it with your browser at https://localhost:5601
  # The example certificate is self signed so you may see a warning about the certificate
  curl -I -k -u elastic:$password https://localhost:5601/app/kibana
  ```

## Testing

This chart uses [pytest](https://docs.pytest.org/en/latest/) to test the templating logic. The dependencies for testing can be installed from the [`requirements.txt`](../requirements.txt) in the parent directory.

```
pip install -r ../requirements.txt
make test
```


You can also use `helm template` to look at the YAML being generated

```
make template
```

It is possible to run all of the tests and linting inside of a docker container

```
make test
```
