## Unreleased - XXXX/XX/XX


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
