## Unreleased - XXXX/XX/XX

### Metricbeat (WIP)

* [#128](https://github.com/elastic/helm-charts/pull/128) - @Crazybus - Add ci jobs for metricbeat
* [#127](https://github.com/elastic/helm-charts/pull/127) - @Crazybus - WIP add metricbeat chart

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
