# Elasticsearch Helm Chart

This functionality is in alpha status and may be changed or removed completely in a future release. Elastic will take a best effort approach to fix any issues, but alpha features are not subject to the support SLA of official GA features.

This helm chart is a lightweight way to configure and run our official [Elasticsearch docker image](https://www.elastic.co/guide/en/kibana/current/docker.html)

## Requirements

* [Helm](https://helm.sh/) >= 2.8.0
* Kubernetes 1.8/1.9/1.10/1.11.
* Minimum cluster requirements include the following to run this chart with default settings. All of these settings are configurable.
  * Three Kubernetes nodes to respect the default "hard" affinity settings
  * 1GB of RAM for the JVM heap

## Usage notes and getting started
* This repo includes a number of [example](./examples) configurations which can be used as a reference. They are also used in the automated testing of this chart
* Automated testing of this chart is currently only run against GKE (Google Kubernetes Engine). If you are using a different Kubernetes provider you will likely need to adjust the `storageClassName` in the `volumeClaimTemplate`
* The default storage class for GKE is `standard` which by default will give you `pd-ssd` type persistent volumes. This is network attached storage and will not perform as well as local storage. If you are using Kubernetes version 1.10 or greater you can use [Local PersistentVolumes](https://cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd) for increased performance
* The chart deploys a statefulset and by default will do an automated rolling update of your cluster. It does this by waiting for the cluster health to become green after each instance is updated. If you prefer to update manually you can set [`updateStrategy: OnDelete`](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#on-delete)
* It is important to verify that the JVM heap size in `esJavaOpts` and to set the CPU/Memory `resources` to something suitable for your cluster
* To simplify chart and maintenance each set of node groups is deployed as a separate helm release. Take a look at the [multi](./examples/multi) example to get an idea for how this works. Without doing this it isn't possible to resize persistent volumes in a statefulset. By setting it up this way it makes it possible to add more nodes with a new storage size then drain the old ones. It also solves the problem of allowing the user to determine which node groups to update first when doing upgrades or changes.
* We have designed this chart to be very un-opinionated about how to configure Elasticsearch. It exposes ways to set environment variables and mount secrets inside of the container. Doing this makes it much easier for this chart to support multiple versions with minimal changes.

## Installing

* Add the elastic helm charts repo
  ```
  helm repo add elastic https://helm.elastic.co
  ```
* Install it
  ```
  helm install --name elasticsearch elastic/elasticsearch --version 6.6.2-alpha1
  ```


## Configuration

| Parameter                  | Description                                                                                                                                                                                                                                                                                                                | Default                                                                                                                   |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `clusterName`              | This will be used as the Elasticsearch [cluster.name](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster.name.html) and should be unique per cluster in the namespace                                                                                                                                 | `elasticsearch`                                                                                                           |
| `nodeGroup`                | This is the name that will be used for each group of nodes in the cluster. The name will be `clusterName-nodeGroup-X`                                                                                                                                                                                                      | `master`                                                                                                                  |
| `masterService`            | Optional. The service name used for [discovery.zen.ping.unicast.hosts](https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-discovery-zen.html#unicast) to connect to the masters. You only need to set this if your master `nodeGroup` is set to something other than `master`                         | ``                                                                                                                        |
| `roles`                    | A hash map with the [specific roles](https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-node.html) for the node group                                                                                                                                                                                 | `master: true`<br>`data: true`<br>`ingest: true`                                                                          |
| `replicas`                 | Kubernetes replica count for the statefulset (i.e. how many pods)                                                                                                                                                                                                                                                          | `3`                                                                                                                       |
| `minimumMasterNodes`       | The value for [discovery.zen.minimum_master_nodes](https://www.elastic.co/guide/en/elasticsearch/reference/current/discovery-settings.html#minimum_master_nodes). Should be set to `(replicas / 2) + 1`                                                                                                                    | `2`                                                                                                                       |
| `esMajorVersion`           | Used to set major version specific configuration. Will set `discovery.zen.minimum_master_nodes` by default and `cluster.initial_master_nodes` for versions >= 7                                                                                                                                                            | `6`                                                                                                                       |
| `esConfig`                 | Allows you to add any config files in `/usr/share/elasticsearch/config/` such as `elasticsearch.yml` and `log4j2.properties`. See [values.yaml](./values.yaml) for an example of the formatting.                                                                                                                           | `{}`                                                                                                                      |
| `extraEnvs`                | Extra [environment variables](https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/#using-environment-variables-inside-of-your-config) which will be appended to the `env:` definition for the container                                                                         | `{}`                                                                                                                      |
| `secretMounts`             | Allows you easily mount a secret as a file inside the statefulset. Useful for mounting certificates and other secrets. See [values.yaml](./values.yaml) for an example                                                                                                                                                     | `{}`                                                                                                                      |
| `image`                    | The Elasticsearch docker image                                                                                                                                                                                                                                                                                             | `docker.elastic.co/elasticsearch/elasticsearch`                                                                           |
| `imageTag`                 | The Elasticsearch docker image tag                                                                                                                                                                                                                                                                                         | `6.6.2`                                                                                                                   |
| `imagePullPolicy`          | The Kubernetes [imagePullPolicy](https://kubernetes.io/docs/concepts/containers/images/#updating-images) value                                                                                                                                                                                                             | `IfNotPresent`                                                                                                            |
| `podAnnotations`           | Configurable [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) applied to all Elasticsearch pods                                                                                                                                                                               | `{}`                                                                                                                      |
| `esJavaOpts`               | [Java options](https://www.elastic.co/guide/en/elasticsearch/reference/current/jvm-options.html) for Elasticsearch. This is where you should configure the [jvm heap size](https://www.elastic.co/guide/en/elasticsearch/reference/current/heap-size.html)                                                                 | `-Xmx1g -Xms1g`                                                                                                           |
| `resources`                | Allows you to set the [resources](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/) for the statefulset                                                                                                                                                                               | `requests.cpu: 100m`<br>`requests.memory: 2Gi`<br>`limits.cpu: 1000m`<br>`limits.memory: 2Gi`                             |
| `initResources`            | Allows you to set the [resources](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/) for the initContainer in the statefulset                                                                                                                                                          | {}                                                                                                                        |
| `networkHost`              | Value for the [network.host Elasticsearch setting](https://www.elastic.co/guide/en/elasticsearch/reference/current/network.host.html)                                                                                                                                                                                      | `0.0.0.0`                                                                                                                 |
| `volumeClaimTemplate`      | Configuration for the [volumeClaimTemplate for statefulsets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#stable-storage). You will want to adjust the storage (default `30Gi`) and the `storageClassName` if you are using a different storage class                                            | `accessModes: [ "ReadWriteOnce" ]`<br>`storageClassName: standard`<br>`resources.requests.storage: 30Gi`                  |
| `antiAffinityTopologyKey`  | The [anti-affinity topology key](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity). By default this will prevent multiple Elasticsearch nodes from running on the same Kubernetes node                                                                                        | `kubernetes.io/hostname`                                                                                                  |
| `antiAffinity`             | Setting this to hard enforces the [anti-affinity rules](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity). If it is set to soft it will be done "best effort". Other values will be ignored.                                                                                  | `hard`                                                                                                                    |
| `nodeAffinity`             | Value for the [node affinity settings](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#node-affinity-beta-feature)                                                                                                                                                                                      | `{}`                                                                                                                      |
| `podManagementPolicy`      | By default Kubernetes [deploys statefulsets serially](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#pod-management-policies). This deploys them in parallel so that they can discover eachother                                                                                                   | `Parallel`                                                                                                                |
| `protocol`                 | The protocol that will be used for the readinessProbe. Change this to `https` if you have `xpack.security.http.ssl.enabled` set                                                                                                                                                                                            | `http`                                                                                                                    |
| `httpPort`                 | The http port that Kubernetes will use for the healthchecks and the service. If you change this you will also need to set [http.port](https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-http.html#_settings_2) in `extraEnvs`                                                                        | `9200`                                                                                                                    |
| `transportPort`            | The transport port that Kubernetes will use for the service. If you change this you will also need to set [transport port configuration](https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-transport.html#_tcp_transport) in `extraEnvs`                                                             | `9300`                                                                                                                    |
| `updateStrategy`           | The [updateStrategy](https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/#updating-statefulsets) for the statefulset. By default Kubernetes will wait for the cluster to be green after upgrading each pod. Setting this to `OnDelete` will allow you to manually delete each pod during upgrades | `RollingUpdate`                                                                                                           |
| `maxUnavailable`           | The [maxUnavailable](https://kubernetes.io/docs/tasks/run-application/configure-pdb/#specifying-a-poddisruptionbudget) value for the pod disruption budget. By default this will prevent Kubernetes from having more than 1 unhealthy pod in the node group                                                                | `1`                                                                                                                       |
| `fsGroup`                  | The Group ID (GID) for [securityContext.fsGroup](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) so that the Elasticsearch user can read from the persistent volume                                                                                                                            | `1000`                                                                                                                    |
| `terminationGracePeriod`   | The [terminationGracePeriod](https://kubernetes.io/docs/concepts/workloads/pods/pod/#termination-of-pods) in seconds used when trying to stop the pod                                                                                                                                                                      | `120`                                                                                                                     |
| `sysctlVmMaxMapCount`      | Sets the [sysctl vm.max_map_count](https://www.elastic.co/guide/en/elasticsearch/reference/current/vm-max-map-count.html#vm-max-map-count) needed for Elasticsearch                                                                                                                                                        | `262144`                                                                                                                  |
| `readinessProbe`           | Configuration fields for the [readinessProbe](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/)                                                                                                                                                                               | `failureThreshold: 3`<br>`initialDelaySeconds: 10`<br>`periodSeconds: 10`<br>`successThreshold: 3`<br>`timeoutSeconds: 5` |
| `clusterHealthCheckParams` | The [Elasticsearch cluster health status params](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-health.html#request-params) that will be used by readinessProbe command                                                                                                                           | `wait_for_status=green&timeout=1s`                                                                                        |
| `imagePullSecrets`         | Configuration for [imagePullSecrets](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#create-a-pod-that-uses-your-secret) so that you can use a private registry for your image                                                                                                       | `[]`                                                                                                                      |
| `nodeSelector`             | Configurable [nodeSelector](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector) so that you can target specific nodes for your Elasticsearch cluster                                                                                                                                          | `{}`                                                                                                                      |
| `tolerations`              | Configurable [tolerations](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/)                                                                                                                                                                                                                        | `[]`                                                                                                                      |
| `ingress`                  | Configurable [ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) to expose the Elasticsearch service. See [`values.yaml`](./values.yaml) for an example                                                                                                                                            | `enabled: false`                                                                                                          |

## Try it out

In [examples/](./examples) you will find some example configurations. These examples are used for the automated testing of this helm chart

### Default

To deploy a cluster with all default values and run the integration tests

```
cd examples/default
make
```

### Multi

A cluster with dedicated node types

```
cd examples/multi
make
```

### Security

A cluster with X-Pack security enabled

* Generate SSL certificates following the [official docs]( https://www.elastic.co/guide/en/elasticsearch/reference/6.3/configuring-tls.html#node-certificates)
* Make sure you have a copy of your [license](https://www.elastic.co/subscriptions) handy.
* Create Kubernetes secrets for authentication credentials, X-Pack license and certificates
  ```
  kubectl create secret generic elastic-credentials  --from-literal=password=changeme --from-literal=username=elastic
  kubectl create secret generic elastic-license --from-file=license.json
  kubectl create secret generic elastic-certificates --from-file=elastic-certificates.p12
  ```
* Deploy!
  ```
  cd examples/security
  make
  ```
* Attach into one of the containers
  ```
  kubectl exec -ti $(kubectl get pods -l release=helm-es-security -o name | awk -F'/' '{ print $NF }' | head -n 1) bash
  ```

* Install the X-Pack license
  ```
  curl -XPUT 'http://localhost:9200/_xpack/license' -H "Content-Type: application/json" -d @/usr/share/elasticsearch/config/license/license.json
  ```
* Test that authentication is now enabled
  ```
  curl 'http://localhost:9200/' # This one will fail
  curl -u elastic:changeme 'http://localhost:9200/'
  ```
* Install some test data to play around with
  ```
  wget https://download.elastic.co/demos/kibana/gettingstarted/logs.jsonl.gz && gunzip logs.jsonl.gz && curl -u elastic:changeme -H 'Content-Type: application/x-ndjson' -XPOST 'localhost:9200/_bulk?pretty' --data-binary @logs.jsonl
  ```

### FAQ

#### How to install plugins?

The [recommended](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#_c_customized_image) way to install plugins into our docker images is to create a custom docker image.

The Dockerfile would look something like:

```
ARG elasticsearch_version
FROM docker.elastic.co/elasticsearch/elasticsearch:${elasticsearch_version}

RUN bin/elasticsearch-plugin install --batch repository-gcs
```

And then updating the `image` in values to point to your custom image.

There are a couple reasons we recommend this.

1. Tying the availability of Elasticsearch to the download service to install plugins is not a great idea or something that we recommend. Especially in Kubernetes where it is normal and expected for a container to be moved to another host at random times.
2. Mutating the state of a running docker image (by installing plugins) goes against best practices of containers and immutable infrastructure.

#### How to use the keystore?

1. Create a Kubernetes secret containing the [keystore](https://www.elastic.co/guide/en/elasticsearch/reference/current/secure-settings.html)
    ```
    $ kubectl create secret generic elasticsearch-keystore --from-file=./elasticsearch.keystore
    ```
2. Mount it into the container via `secretMounts`
    ```
    secretMounts:
    - name: elasticsearch-keystore
      secretName: elasticsearch-keystore
      path: /usr/share/elasticsearch/config/elasticsearch.keystore
      subPath: elasticsearch.keystore
    ```


### Local development environments

This chart is designed to run on production scale Kubernetes clusters with multiple nodes, lots of memory and persistent storage. For that reason it can be a bit tricky to run them against local Kubernetes environments such as minikube. Below are some examples of how to get this working locally.

#### Minikube

This chart also works successfully on [minikube](https://kubernetes.io/docs/setup/minikube/) in addition to typical hosted Kubernetes environments.
An example `values.yaml` file for minikube is provided under `examples/`.

In order to properly support the required persistent volume claims for the Elasticsearch `StatefulSet`, the `default-storageclass` and `storage-provisioner` minikube addons must be enabled.

```
minikube addons enable default-storageclass
minikube addons enable storage-provisioner
cd examples/minikube
make
```

Note that if `helm` or `kubectl` timeouts occur, you may consider creating a minikube VM with more CPU cores or memory allocated.


#### Docker for Mac - Kubernetes

It is also possible to run this chart with the built in Kubernetes cluster that comes with [docker-for-mac](https://docs.docker.com/docker-for-mac/kubernetes/).

```
cd examples/docker-for-mac
make
```

## Clustering and Node Discovery

This chart facilitates Elasticsearch node discovery and services by creating two `Service` definitions in Kubernetes, one with the name `$clusterName-$nodeGroup` and another named `$clusterName-$nodeGroup-headless`.
Only `Ready` pods are a part of the `$clusterName-$nodeGroup` service, while all pods (`Ready` or not) are a part of `$clusterName-$nodeGroup-headless`.

If your group of master nodes has the default `nodeGroup: master` then you can just add new groups of nodes with a different `nodeGroup` and they will automatically discover the correct master. If your master nodes have a different `nodeGroup` name then you will need to set `masterService` to `$clusterName-$masterNodeGroup`.

The chart value for `masterService` is used to populate `discovery.zen.ping.unicast.hosts`, which Elasticsearch nodes will use to contact master nodes and form a cluster.
Therefore, to add a group of nodes to an existing cluster, setting `masterService` to the desired `Service` name of the related cluster is sufficient.

For an example of deploying both a group master nodes and data nodes using multiple releases of this chart, see the accompanying values files in `examples/multi`.

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
