# Changelog

---
## 7.2.1-0 - 2019/07/01

* [#195](https://github.com/elastic/helm-charts/pull/195) - @cclauss - Initial steps started to move all python2 code to python3
* [#205](https://github.com/elastic/helm-charts/pull/205) - @Crazybus - Fixup and improve security example documentation


### Elasticsearch

* [#171](https://github.com/elastic/helm-charts/pull/171) - @naseemkullah - Run Elasticsearch as a non-root user
* [#197](https://github.com/elastic/helm-charts/pull/197) - @tetianakravchenko - Add option to provide custom start/stop hooks
* [#206](https://github.com/elastic/helm-charts/pull/206) - @Crazybus - Automatically detect esMajorVersion for default images
* [#203](https://github.com/elastic/helm-charts/pull/203) - @Crazybus - Add testing for security context
* [#220](https://github.com/elastic/helm-charts/pull/220) - @JorisAndrade -  Add option to disable sysctlInitContainer

### Kibana

* [#204](https://github.com/elastic/helm-charts/pull/204) - @Crazybus - Make imagePullPolicy actually do something
* [#210](https://github.com/elastic/helm-charts/pull/210) - @cliedeman - Add Kibana pod annotations
* [#217](https://github.com/elastic/helm-charts/pull/217) - @Crazybus - Update healthCheckPath to mention basePath usage

### Filebeat

* [#214](https://github.com/elastic/helm-charts/pull/214) - @dugouchet - Add additional labels

### Metricbeat

* [#127](https://github.com/elastic/helm-charts/pull/127) - @Crazybus - Add metricbeat chart
* [#128](https://github.com/elastic/helm-charts/pull/128) - @Crazybus - Add ci jobs for metricbeat

---
## 7.2.0 - 2019/07/01

* 7.2.0 as the default stack version
* Updated the beta status messaging and added proper descriptions to each chart [#158](https://github.com/elastic/helm-charts/pull/158)
* Add GKE 1.13 to automated testing suite [#169](https://github.com/elastic/helm-charts/pull/169) and [#181](https://github.com/elastic/helm-charts/pull/181)

### Elasticsearch

* [#123](https://github.com/elastic/helm-charts/pull/123) - @kimxogus - Make the service configurable
* [#141](https://github.com/elastic/helm-charts/pull/141) - @satchpx - Add capability to specify alternate scheduler
* [#161](https://github.com/elastic/helm-charts/pull/161) - @Crazybus - Add configurable nodePort to the service spec
* [#170](https://github.com/elastic/helm-charts/pull/170) - @Crazybus - Update security example docs to match reality
* [#182](https://github.com/elastic/helm-charts/pull/182) - @hxquangnhat - Fix secretName field for secretMounts
* [#186](https://github.com/elastic/helm-charts/pull/186) - @Crazybus - Fix pvc annotations with multiple fields
* [#189](https://github.com/elastic/helm-charts/pull/189) - @gnatpat - Add resources to sidecar container


### Kibana

* [#160](https://github.com/elastic/helm-charts/pull/160) - @Crazybus - Add configurable nodePort to the service spec
* [#168](https://github.com/elastic/helm-charts/pull/168) - @Crazybus - Always set server.host to the docker default
* [#172](https://github.com/elastic/helm-charts/pull/172) - @naseemkullah - Run Kibana as the non-root kibana user (1000)
* [#182](https://github.com/elastic/helm-charts/pull/182) - @hxquangnhat - Fix secretName field for secretMounts
* [#184](https://github.com/elastic/helm-charts/pull/184) - @diegofernandes - Fix wildcard support for ingress

### Filebeat

* [#182](https://github.com/elastic/helm-charts/pull/182) - @hxquangnhat - Fix secretName field for secretMounts
* [#188](https://github.com/elastic/helm-charts/pull/188) - @cclauss - Fix octal literal to work in both Python 2 and Python 3

---
## 7.1.1 - 2019/06/07

* 7.1.1 as the default stack version
* Helm 2.14.0 as the tested version. Helm 2.14.0 has some extra validation built in which caused an issue with an [invalid field in the filebeat chart](https://github.com/elastic/helm-charts/issues/136).

### Elasticsearch

* [#146](https://github.com/elastic/helm-charts/pull/146) - @Crazybus - Add instructions for how to enable snapshots

### Kibana

* [#151](https://github.com/elastic/helm-charts/pull/151) - @natebwangsut - Added an option to add annotations(s) to service resource

### Filebeat

* [#140](https://github.com/elastic/helm-charts/pull/140) - @Crazybus - Remove fsGroup from container level security context

---
## 7.1.0 - 2019/05/21

* 7.1.0 as the default stack version
* Promotion from alpha to beta status
* Filebeat chart added

### Elasticsearch

* [#119](https://github.com/elastic/helm-charts/pull/119) - @kimxogus - Wait for new master election before stopping the pod to prevent master status being temporarily lost during rolling upgrades #63
* [#109](https://github.com/elastic/helm-charts/pull/109) - @lancespeelmon - Add support for k8s priorityclass

### Kibana

* [#109](https://github.com/elastic/helm-charts/pull/109) - @lancespeelmon - Add support for k8s priorityclass
* [#134](https://github.com/elastic/helm-charts/pull/134) - @Crazybus - Explicitly set the targetPort to the defined http port

### Filebeat

* [#117](https://github.com/elastic/helm-charts/pull/117) - @tylerjl - Add initial filebeat chart
* [#122](https://github.com/elastic/helm-charts/pull/122) - @Crazybus - Add ci jobs for filebeat
* [#121](https://github.com/elastic/helm-charts/pull/121) - @Crazybus - Add integration tests and other tweaks
* [#129](https://github.com/elastic/helm-charts/pull/129) - @tylerjl - Add usage notes for filebeat

---
## 7.0.1-alpha1 - 2019/05/01

* 7.0.1 as the default stack version
* [Contributing guide](https://github.com/elastic/helm-charts/blob/master/CONTRIBUTING.md), [release process](https://github.com/elastic/helm-charts/blob/master/helpers/release.md), [changelog](https://github.com/elastic/helm-charts/blob/master/CHANGELOG.md) and [issue templates](https://github.com/elastic/helm-charts/tree/master/.github/ISSUE_TEMPLATE) added in [#111](https://github.com/elastic/helm-charts/pull/111)
* Automated testing for Kubernetes 1.10 dropped because it is no longer available in GKE
* Helm client version bumped to 2.13.1

### Elasticsearch

* [#100](https://github.com/elastic/helm-charts/pull/100) - @kuisathaverat - Remove deprecated zen ping unicast hosts setting 
* [#114](https://github.com/elastic/helm-charts/pull/114) - @Crazybus - Make persistent volumes optional
* [#115](https://github.com/elastic/helm-charts/pull/115) - @Crazybus - Added an integration test for upgrading from the previous release and testing rolling upgrades


### Kibana

* [#107](https://github.com/elastic/helm-charts/pull/107) - @Crazybus - Make the health check path configurable to support webroots and other customizations. 

---
## 7.0.0-alpha1 - 2019/04/17

* [#96](https://github.com/elastic/helm-charts/pull/96) - @Crazybus - 7.0.0 as the default stack version

### Elasticsearch

* [#94](https://github.com/elastic/helm-charts/pull/94) - @kimxogus - Remove hardcoded storageClassName

### Notes

If you were using the default Elasticsearch version from the previous release (6.6.2-alpha1) you will first need to upgrade to Elasticsearch 6.7.1 before being able to upgrade to 7.0.0. You can do this by adding this to your values file:

```
esMajorVersion: 6
imageTag: 6.7.1
```

If you are upgrading an existing cluster that did not override the default `storageClassName` you will now need to specify the `storageClassName`. This only affects existing clusters and was changed in https://github.com/elastic/helm-charts/pull/94. The advantage of this is that now the helm chart will just use the default storageClassName rather than needing to override it for any providers where it is not called `standard`. 

```
volumeClaimTemplate:
  storageClassName: "standard"
```
