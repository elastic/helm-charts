# Changelog

## 8.5.1

* 8.5.1 as default version
* See the [Breaking changes](./BREAKING_CHANGES.md) for a detailed list of changes.
* Thanks for everyone that contributed to this release, especially [@framsouza](https://github.com/framsouza), [@jmlrt](https://github.com/jmlrt),[@ebuildy](https://github.com/ebuildy), [@pjaak](https://github.com/pjaak), [@azasypkin](https://github.com/azasypkin),[@jbudz](https://github.com/jbudz),[@jkakavas](https://github.com/jkakavas), [@mark-vieira](https://github.com/mark-vieira), [@mgreau](https://github.com/mgreau), [@nkammah](https://github.com/nkammah), [@pugnascotia](https://github.com/pugnascotia), [@rjernst](https://github.com/rjernst), and everyone else who wasn't mentionned here...


## 7.17.3

* 7.17.3 as default version.


| PR                                                        | Author                             | Title                                    |
|-----------------------------------------------------------|------------------------------------|------------------------------------------|
| [#1632](https://github.com/elastic/helm-charts/pull/1632) | [@jmlrt](https://github.com/jmlrt) | [meta] update upgrade tests base version |
| [#1622](https://github.com/elastic/helm-charts/pull/1622) | [@jmlrt](https://github.com/jmlrt) | [metricbeat] fix upgrade test            |


## 7.17.1

* 7.17.1 as default version.


| PR                                                        | Author                                       | Title                                                                   |
|-----------------------------------------------------------|----------------------------------------------|-------------------------------------------------------------------------|
| [#1604](https://github.com/elastic/helm-charts/pull/1604) | [@jmlrt](https://github.com/jmlrt)           | [meta] update docker images                                             |
| [#1603](https://github.com/elastic/helm-charts/pull/1603) | [@jmlrt](https://github.com/jmlrt)           | [metricbeat] add missing rolebinding and cluster role rules             |
| [#1602](https://github.com/elastic/helm-charts/pull/1602) | [@jmlrt](https://github.com/jmlrt)           | [filebeat] add missing rolebinding and cluster role rules               |
| [#1593](https://github.com/elastic/helm-charts/pull/1593) | [@jmlrt](https://github.com/jmlrt)           | [meta] add support for k8s 1.22                                         |
| [#1582](https://github.com/elastic/helm-charts/pull/1582) | [@jmlrt](https://github.com/jmlrt)           | [kibana] fix extra values default values                                |
| [#1581](https://github.com/elastic/helm-charts/pull/1581) | [@jmlrt](https://github.com/jmlrt)           | [logstash] fix ServiceAccount inconsistencies                           |
| [#1580](https://github.com/elastic/helm-charts/pull/1580) | [@jmlrt](https://github.com/jmlrt)           | [elasticsearch] fix ServiceAccount inconsistencies                      |
| [#1570](https://github.com/elastic/helm-charts/pull/1570) | [@jmlrt](https://github.com/jmlrt)           | [logstash] add externalTrafficPolicy support                            |
| [#1569](https://github.com/elastic/helm-charts/pull/1569) | [@jmlrt](https://github.com/jmlrt)           | [logstash] add flexible ingress                                         |
| [#1563](https://github.com/elastic/helm-charts/pull/1563) | [@jmlrt](https://github.com/jmlrt)           | [meta] bump Helm version to 3.8.0                                       |
| [#1538](https://github.com/elastic/helm-charts/pull/1538) | [@chetanv-oi](https://github.com/chetanv-oi) | [elasticsearch] move the yaml separator inside the condition            |
| [#1530](https://github.com/elastic/helm-charts/pull/1530) | [@jmlrt](https://github.com/jmlrt)           | [kibana] use bash for readiness script                                  |
| [#1527](https://github.com/elastic/helm-charts/pull/1527) | [@ebuildy](https://github.com/ebuildy)       | [apm-server] add pod labels                                             |
| [#1524](https://github.com/elastic/helm-charts/pull/1524) | [@beatkind](https://github.com/beatkind)     | [metricbeat] bump kube-state-metrics to version 4.7.0                   |
| [#1521](https://github.com/elastic/helm-charts/pull/1521) | [@ebuildy](https://github.com/ebuildy)       | [apm-server] fix podLabels                                              |
| [#1494](https://github.com/elastic/helm-charts/pull/1494) | [@ebuildy](https://github.com/ebuildy)       | [elasticsearch] add keystore container securityContext                  |
| [#1450](https://github.com/elastic/helm-charts/pull/1450) | [@dmarcs](https://github.com/dmarcs)         | [logstash] allow array values for extra                                 |
| [#1422](https://github.com/elastic/helm-charts/pull/1422) | [@framsouza](https://github.com/framsouza)   | [metricbeat] adding custerRole permissions for leader election          |
| [#1420](https://github.com/elastic/helm-charts/pull/1420) | [@framsouza](https://github.com/framsouza)   | [elasticsearch] [logstash] add support to PodDisruptionBudget policy/v1 |
| [#1417](https://github.com/elastic/helm-charts/pull/1417) | [@framsouza](https://github.com/framsouza)   | [kibana] add annotations at deployment level                            |


## 7.16.3

* 7.16.3 as default version.


| PR                                                        | Author                                               | Title                                                     |
|-----------------------------------------------------------|------------------------------------------------------|-----------------------------------------------------------|
| [#1533](https://github.com/elastic/helm-charts/pull/1533) | [@ebuildy](https://github.com/ebuildy)               | [tests] fix yaml load warning (#1522)                     |
| [#1517](https://github.com/elastic/helm-charts/pull/1517) | [@elasticmachine](https://github.com/elasticmachine) | Bump version to 7.16.3-SNAPSHOT                           |
| [#1502](https://github.com/elastic/helm-charts/pull/1502) | [@ebuildy](https://github.com/ebuildy)               | [elasticsearch] #1495 Configure JVM options files (#1496) |


## 7.16.2

* 7.16.2 as default version.

| PR                                                        | Author                                               | Title                                                    |
|-----------------------------------------------------------|------------------------------------------------------|----------------------------------------------------------|
| [#1507](https://github.com/elastic/helm-charts/pull/1507) | [@jmlrt](https://github.com/jmlrt)                   | [elasticsearch] remove usage of ELASTIC_USERNAME (#1506) |
| [#1499](https://github.com/elastic/helm-charts/pull/1499) | [@elasticmachine](https://github.com/elasticmachine) | Bump version to 7.16.2-SNAPSHOT                          |


## 6.8.22

* 6.8.22 as default version.

| PR                                                        | Author                                               | Title                                                    |
|-----------------------------------------------------------|------------------------------------------------------|----------------------------------------------------------|
| [#1508](https://github.com/elastic/helm-charts/pull/1508) | [@jmlrt](https://github.com/jmlrt)                   | [elasticsearch] remove usage of ELASTIC_USERNAME (#1506) |
| [#1498](https://github.com/elastic/helm-charts/pull/1498) | [@elasticmachine](https://github.com/elasticmachine) | Bump version to 6.8.22-SNAPSHOT                          |


## 7.16.1

* 7.16.1 as default version.

| PR                                                        | Author                                         | Title                                                                  |
|-----------------------------------------------------------|------------------------------------------------|------------------------------------------------------------------------|
| [#1382](https://github.com/elastic/helm-charts/pull/1382) | [@piglovesyou](https://github.com/piglovesyou) | [elasticsearch] fix typo                                               |
| [#1386](https://github.com/elastic/helm-charts/pull/1386) | [@jmlrt](https://github.com/jmlrt)             | [meta] fail make test on error                                         |
| [#1409](https://github.com/elastic/helm-charts/pull/1409) | [@framsouza](https://github.com/framsouza)     | [all] add support to ingress networking.k8s.io/v1 & ingressClassName   |
| [#1410](https://github.com/elastic/helm-charts/pull/1410) | [@jmlrt](https://github.com/jmlrt)             | [meta] add support for K8S 1.21 and remove 1.18                        |
| [#1458](https://github.com/elastic/helm-charts/pull/1458) | [@jmlrt](https://github.com/jmlrt)             | [elasticsearch] use bash for readiness script                          |
| [#1460](https://github.com/elastic/helm-charts/pull/1460) | [@jmlrt](https://github.com/jmlrt)             | [meta] download goss outside of pods                                   |
| [#1464](https://github.com/elastic/helm-charts/pull/1464) | [@jmlrt](https://github.com/jmlrt)             | [elasticsearch] use bash for keystore init container                   |
| [#1466](https://github.com/elastic/helm-charts/pull/1466) | [@jmlrt](https://github.com/jmlrt)             | [elasticsearch] fix a typo in 4e31e0cf3d025f9ce877ac52d218f49d72e26447 |
| [#1469](https://github.com/elastic/helm-charts/pull/1469) | [@jmlrt](https://github.com/jmlrt)             | [metricbeat] remove es metricset search query for oss example          |
| [#1474](https://github.com/elastic/helm-charts/pull/1474) | [@framsouza](https://github.com/framsouza)     | [elasticsearch] disabling deprecation logs to be indexed               |
| [#1475](https://github.com/elastic/helm-charts/pull/1475) | [@jmlrt](https://github.com/jmlrt)             | [meta] initiate 7.16 branch                                            |
| [#1476](https://github.com/elastic/helm-charts/pull/1476) | [@jmlrt](https://github.com/jmlrt)             | [meta] update backport config for 7.16 branch                          |
| [#1480](https://github.com/elastic/helm-charts/pull/1480) | [@jmlrt](https://github.com/jmlrt)             | [elasticsearch] fix a lines order in example values                    |


## 6.8.21

* 6.8.21 as default version.

| PR                                                        | Author                                               | Title                                                           |
|-----------------------------------------------------------|------------------------------------------------------|-----------------------------------------------------------------|
| [#1410](https://github.com/elastic/helm-charts/pull/1410) | [@jmlrt](https://github.com/jmlrt)                   | [meta] add support for K8S 1.21 and remove 1.18                 |
| [#1300](https://github.com/elastic/helm-charts/pull/1300) | [@jonkerj](https://github.com/jonkerj)               | [elasticsearch]: optionally disable SA token automount          |
| [#1382](https://github.com/elastic/helm-charts/pull/1382) | [@piglovesyou](https://github.com/piglovesyou)       | Fix typo                                                        |
| [#1386](https://github.com/elastic/helm-charts/pull/1386) | [@jmlrt](https://github.com/jmlrt)                   | [meta] fail make test on error                                  |
| [#1319](https://github.com/elastic/helm-charts/pull/1319) | [@cclausss](https://github.com/cclausss)             | Fix typos discovered by codespell                               |
| [#1105](https://github.com/elastic/helm-charts/pull/1105) | [@moritazi](https://github.com/moritazi)             | [elasticsearch] Add namespace to helm test command in NOTES.txt |
| [#1362](https://github.com/elastic/helm-charts/pull/1362) | [@jmlrt](https://github.com/jmlrt)                   | [meta] remove contributing file from 6.8 branch                 |
| [#1321](https://github.com/elastic/helm-charts/pull/1321) | [@elasticmachine](https://github.com/elasticmachine) | Bump version to 6.8.19-SNAPSHOT                                 |
| [#1294](https://github.com/elastic/helm-charts/pull/1294) | [@jmlrt](https://github.com/jmlrt)                   | [meta] add tests for k8s 1.20                                   |
| [#1232](https://github.com/elastic/helm-charts/pull/1232) | [@jmlrt](https://github.com/jmlrt)                   | [meta] add helm 3.6.2 support                                   |
| [#1116](https://github.com/elastic/helm-charts/pull/1116) | [@nflaig](https://github.com/nflaig)                 | [elasticsearch] add value to disable tests                      |
| [#1115](https://github.com/elastic/helm-charts/pull/1115) | [@nflaig](https://github.com/nflaig)                 | [elasticsearch] add value to disable service                    |
| [#1337](https://github.com/elastic/helm-charts/pull/1337) | [@jmlrt](https://github.com/jmlrt)                   | [meta] remove support matrix + nit doc changes                  |


## 7.15.0

* 7.15.0 as default version.


| PR                                                        | Author                                   | Title                                                           |
|-----------------------------------------------------------|------------------------------------------|-----------------------------------------------------------------|
| [#1294](https://github.com/elastic/helm-charts/pull/1294) | [@jmlrt](https://github.com/jmlrt)       | [meta] add tests for k8s 1.20                                   |
| [#1232](https://github.com/elastic/helm-charts/pull/1232) | [@jmlrt](https://github.com/jmlrt)       | [meta] add helm 3.6.2 support                                   |
| [#1116](https://github.com/elastic/helm-charts/pull/1116) | [@nflaig](https://github.com/nflaig)     | [elasticsearch] add value to disable tests                      |
| [#1115](https://github.com/elastic/helm-charts/pull/1115) | [@nflaig](https://github.com/nflaig)     | [elasticsearch] add value to disable service                    |
| [#1105](https://github.com/elastic/helm-charts/pull/1105) | [@moritazy](https://github.com/moritazy) | [elasticsearch] Add namespace to helm test command in NOTES.txt |
| [#1361](https://github.com/elastic/helm-charts/pull/1361) | [@jmlrt](https://github.com/jmlrt)       | [meta] remove contributing file from 7.15 branch                |
| [#1357](https://github.com/elastic/helm-charts/pull/1357) | [@ygel](https://github.com/ygel)         | [meta] Initiate 7.15 branch                                     |
| [#1337](https://github.com/elastic/helm-charts/pull/1337) | [@jmlrt](https://github.com/jmlrt)       | [meta] remove support matrix + nit doc changes                  |
| [#1316](https://github.com/elastic/helm-charts/pull/1316) | [@jmlrt](https://github.com/jmlrt)       | [meta] bump 7.x branch to 7.15.0-SNAPSHOT                       |


## 7.14.0

* 7.14.0 as default version.


## 6.8.18

* 6.8.18 as default version.


| PR                                                        | Author                                               | Title                                       |
|-----------------------------------------------------------|------------------------------------------------------|---------------------------------------------|
| [#1269](https://github.com/elastic/helm-charts/pull/1269) | [@jmlrt](https://github.com/jmlrt)                   | [6.8] [meta] add tests for k8s 1.19 (#1231) |
| [#1306](https://github.com/elastic/helm-charts/pull/1306) | [@jmlrt](https://github.com/jmlrt)                   | [meta] update support matrix (#1305)        |
| [#1292](https://github.com/elastic/helm-charts/pull/1292) | [@elasticmachine](https://github.com/elasticmachine) | Bump version to 6.8.18-SNAPSHOT             |


## 7.13.4

* 7.13.4 as default version.


| PR                                                        | Author                                               | Title                           |
|-----------------------------------------------------------|------------------------------------------------------|---------------------------------|
| [#1293](https://github.com/elastic/helm-charts/pull/1293) | [@elasticmachine](https://github.com/elasticmachine) | Bump version to 7.13.4-SNAPSHOT |


## 7.13.3

* 7.13.3 as default version.


| PR                                                        | Author                                               | Title                                                                    |
|-----------------------------------------------------------|------------------------------------------------------|--------------------------------------------------------------------------|
| [#1288](https://github.com/elastic/helm-charts/pull/1288) | [@jmlrt](https://github.com/jmlrt)                   | [meta] remove gke 1.17 tests (#1286)                                     |
| [#1279](https://github.com/elastic/helm-charts/pull/1279) | [@DilasserT](https://github.com/DilasserT)           | [kibana] adding extra volumes and extra volume mounts (#557) (#1264)     |
| [#1276](https://github.com/elastic/helm-charts/pull/1276) | [@ebuildy](https://github.com/ebuildy)               | [logstash] feat: add podAffinity settings (#1257)                        |
| [#1273](https://github.com/elastic/helm-charts/pull/1273) | [@tomhobson](https://github.com/tomhobson)           | [elasticsearch] Added health pod name override for compatibility (#1058) |
| [#1270](https://github.com/elastic/helm-charts/pull/1270) | [@jmlrt](https://github.com/jmlrt)                   | [meta] add tests for k8s 1.19 (#1231)                                    |
| [#1252](https://github.com/elastic/helm-charts/pull/1252) | [@elasticmachine](https://github.com/elasticmachine) | Bump version to 7.13.3-SNAPSHOT                                          |


## 6.8.17

* 6.8.17 as default version.


| PR                                                        | Author                                               | Title                                                                    |
|-----------------------------------------------------------|------------------------------------------------------|--------------------------------------------------------------------------|
| [#1278](https://github.com/elastic/helm-charts/pull/1278) | [@DilasserT](https://github.com/DilasserT)           | [kibana] adding extra volumes and extra volume mounts (#557) (#1264)     |
| [#1275](https://github.com/elastic/helm-charts/pull/1275) | [@ebuildy](https://github.com/ebuildy)               | [logstash] feat: add podAffinity settings (#1257)                        |
| [#1272](https://github.com/elastic/helm-charts/pull/1272) | [@tomhobson](https://github.com/tomhobson)           | [elasticsearch] Added health pod name override for compatibility (#1058) |
| [#1216](https://github.com/elastic/helm-charts/pull/1216) | [@jmlrt](https://github.com/jmlrt)                   | [elasticsearch] fix statefulset to rollout in upgrade test (#1189)       |
| [#1227](https://github.com/elastic/helm-charts/pull/1227) | [@elasticmachine](https://github.com/elasticmachine) | Bump version to 6.8.17-SNAPSHOT                                          |
| [#1210](https://github.com/elastic/helm-charts/pull/1210) | [@jmlrt](https://github.com/jmlrt)                   | [elasticsearch] only configure ES_JAVA_OPTS when value is set (#1089)    |
| [#1207](https://github.com/elastic/helm-charts/pull/1207) | [@jmlrt](https://github.com/jmlrt)                   | [elasticsearch] fix network policies http additional rules (#1111)       |


## 7.13.2

* 7.13.2 as default version.


| PR                                                        | Author                                               | Title                                                              |
|-----------------------------------------------------------|------------------------------------------------------|--------------------------------------------------------------------|
| [#1220](https://github.com/elastic/helm-charts/pull/1220) | [@jmlrt](https://github.com/jmlrt)                   | [elasticsearch] remove unused sidecarResources value (#1185)       |
| [#1217](https://github.com/elastic/helm-charts/pull/1217) | [@jmlrt](https://github.com/jmlrt)                   | [elasticsearch] fix statefulset to rollout in upgrade test (#1189) |
| [#1214](https://github.com/elastic/helm-charts/pull/1214) | [@jmlrt](https://github.com/jmlrt)                   | [elasticsearch] remove masterTerminationFix (#1183)                |
| [#1238](https://github.com/elastic/helm-charts/pull/1238) | [@elasticmachine](https://github.com/elasticmachine) | Bump version to 7.13.2-SNAPSHOT                                    |


## 7.13.1

* 7.13.1 as default version.


| PR                                                        | Author                                               | Title                                                                 |
|-----------------------------------------------------------|------------------------------------------------------|-----------------------------------------------------------------------|
| [#1211](https://github.com/elastic/helm-charts/pull/1211) | [@jmlrt](https://github.com/jmlrt)                   | [elasticsearch] only configure ES_JAVA_OPTS when value is set (#1089) |
| [#1208](https://github.com/elastic/helm-charts/pull/1208) | [@jmlrt](https://github.com/jmlrt)                   | [elasticsearch] fix network policies http additional rules (#1111)    |
| [#1228](https://github.com/elastic/helm-charts/pull/1228) | [@elasticmachine](https://github.com/elasticmachine) | Bump version to 7.13.1-SNAPSHOT                                       |


## 7.13.0

* 7.13.0 as default version.


| PR                                                        | Author                               | Title                                                        |
|-----------------------------------------------------------|--------------------------------------|--------------------------------------------------------------|
| [#1205](https://github.com/elastic/helm-charts/pull/1205) | [@jmlrt](https://github.com/jmlrt)   | [meta] update backport config for 7.13 branch (#1198)        |
| [#1197](https://github.com/elastic/helm-charts/pull/1197) | [@jmlrt](https://github.com/jmlrt)   | [meta] Initiate 7.13 branch                                  |
| [#1194](https://github.com/elastic/helm-charts/pull/1194) | [@jmlrt](https://github.com/jmlrt)   | [meta] remove gke 1.16 tests (#1184)                         |
| [#1175](https://github.com/elastic/helm-charts/pull/1175) | [@nittyy](https://github.com/nittyy) | [7.x][logstash] Add option loadBalancerIP to service (#1099) |


## 6.8.16

* 6.8.16 as default version.


| PR                                                        | Author                                                         | Title                                                                |
|-----------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------------|
| [#1192](https://github.com/elastic/helm-charts/pull/1192) | [@jmlrt](https://github.com/jmlrt)                             | [meta] remove gke 1.16 tests (#1184)                                 |
| [#1176](https://github.com/elastic/helm-charts/pull/1176) | [@nittyy](https://github.com/nittyy)                           | [6.8][logstash] Add option loadBalancerIP to service (#1099)         |
| [#1172](https://github.com/elastic/helm-charts/pull/1172) | [@dependabot](https://github.com/dependabot)                   | [6.8] Bump py from 1.8.0 to 1.10.0 (#1155)                           |
| [#1169](https://github.com/elastic/helm-charts/pull/1169) | [@dependabot](https://github.com/dependabot)                   | [6.8] Bump py from 1.8.0 to 1.10.0 in /helpers/helm-tester (#1154)   |
| [#1160](https://github.com/elastic/helm-charts/pull/1160) | [@jmlrt](https://github.com/jmlrt)                             | [6.8] [meta] add helm 3.5.3 support (#1128)                          |
| [#1166](https://github.com/elastic/helm-charts/pull/1166) | [@karolinepauls](https://github.com/karolinepauls)             | [6.8] [elasticsearch] Mark esMajorVersion as deprecated (#1109)      |
| [#1163](https://github.com/elastic/helm-charts/pull/1163) | [@jmlrt](https://github.com/jmlrt)                             | [6.8] [meta] update backport config for 7.12 branch (#1112)          |
| [#1157](https://github.com/elastic/helm-charts/pull/1157) | [@AndreasChristianson](https://github.com/AndreasChristianson) | [6.8] [elasticsearch] heap size is no longer defaulted to 1g (#1135) |
| [#1145](https://github.com/elastic/helm-charts/pull/1145) | [@jmlrt](https://github.com/jmlrt)                             | [6.8] [meta] update PyYAML dependencies (#1140)                      |
| [#1142](https://github.com/elastic/helm-charts/pull/1142) | [@jmlrt](https://github.com/jmlrt)                             | [6.8] [meta] add tests for k8s 1.18 and remove 1.15 (#1141)          |


## 7.12.1

* 7.12.1 as default version.


| PR                                                        | Author                                                         | Title                                                                 |
|-----------------------------------------------------------|----------------------------------------------------------------|-----------------------------------------------------------------------|
| [#1173](https://github.com/elastic/helm-charts/pull/1173) | [@dependabot](https://github.com/dependabot)                   | [7.12] Bump py from 1.8.0 to 1.10.0 (#1155)                           |
| [#1170](https://github.com/elastic/helm-charts/pull/1170) | [@dependabot](https://github.com/dependabot)                   | [7.12] Bump py from 1.8.0 to 1.10.0 in /helpers/helm-tester (#1154)   |
| [#1161](https://github.com/elastic/helm-charts/pull/1161) | [@jmlrt](https://github.com/jmlrt)                             | [7.12] [meta] add helm 3.5.3 support (#1128)                          |
| [#1167](https://github.com/elastic/helm-charts/pull/1167) | [@karolinepauls](https://github.com/karolinepauls)             | [7.12] [elasticsearch] Mark esMajorVersion as deprecated (#1109)      |
| [#1164](https://github.com/elastic/helm-charts/pull/1164) | [@jmlrt](https://github.com/jmlrt)                             | [7.12] [meta] update backport config for 7.12 branch (#1112)          |
| [#1158](https://github.com/elastic/helm-charts/pull/1158) | [@AndreasChristianson](https://github.com/AndreasChristianson) | [7.12] [elasticsearch] heap size is no longer defaulted to 1g (#1135) |
| [#1146](https://github.com/elastic/helm-charts/pull/1146) | [@jmlrt](https://github.com/jmlrt)                             | [7.12] [meta] update PyYAML dependencies (#1140)                      |
| [#1143](https://github.com/elastic/helm-charts/pull/1143) | [@jmlrt](https://github.com/jmlrt)                             | [7.12] [meta] add tests for k8s 1.18 and remove 1.15 (#1141)          |
| [#1125](https://github.com/elastic/helm-charts/pull/1125) | [@elasticmachine](https://github.com/elasticmachine)           | Bump 7.12 branch to 7.12.1-SNAPSHOT                                   |


## 7.12.0

* 7.12.0 as default version.


| PR                                                        | Author                                 | Title                                                            |
|-----------------------------------------------------------|----------------------------------------|------------------------------------------------------------------|
| [#1093](https://github.com/elastic/helm-charts/pull/1093) | [@ebuildy](https://github.com/ebuildy) | [7.x] [apm-server] Add  option loadBalancerIP to service (#1075) |


## 6.8.15

* 6.8.15 as default version.


| PR                                                        | Author                                                   | Title                                                            |
|-----------------------------------------------------------|----------------------------------------------------------|------------------------------------------------------------------|
| [#1092](https://github.com/elastic/helm-charts/pull/1092) | [@ebuildy](https://github.com/ebuildy)                   | [6.8] [apm-server] Add  option loadBalancerIP to service (#1075) |
| [#1080](https://github.com/elastic/helm-charts/pull/1080) | [@jmlrt](https://github.com/jmlrt)                       | [6.8] [meta] bump helm support to 3.5.2 (#1065)                  |
| [#952](https://github.com/elastic/helm-charts/pull/952)   | [@jmlrt](https://github.com/jmlrt)                       | [6.8] [meta] enable filebeat and metricbeat upgrade test         |
| [#1077](https://github.com/elastic/helm-charts/pull/1077) | [@tuananhnguyen-ct](https://github.com/tuananhnguyen-ct) | [6.8] [logstash] Add support to use pattern files (#883)         |
| [#1068](https://github.com/elastic/helm-charts/pull/1068) | [@elasticmachine](https://github.com/elasticmachine)     | Bump 6.8 branch to 6.8.15-SNAPSHOT                               |


## 7.11.2

* 7.11.2 as default version.


| PR                                                        | Author                                                   | Title                                                     |
|-----------------------------------------------------------|----------------------------------------------------------|-----------------------------------------------------------|
| [#1081](https://github.com/elastic/helm-charts/pull/1081) | [@jmlrt](https://github.com/jmlrt)                       | [7.11] [meta] bump helm support to 3.5.2 (#1065)          |
| [#1078](https://github.com/elastic/helm-charts/pull/1078) | [@tuananhnguyen-ct](https://github.com/tuananhnguyen-ct) | [7.11] [logstash] Add support to use pattern files (#883) |
| [#1072](https://github.com/elastic/helm-charts/pull/1072) | [@elasticmachine](https://github.com/elasticmachine)     | Bump 7.11 branch to 7.11.2-SNAPSHOT                       |


## 7.11.1

* 7.11.1 as default version.


| PR                                                        | Author                                                   | Title                                                                                                                        |
|-----------------------------------------------------------|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [#1053](https://github.com/elastic/helm-charts/pull/1053) | [@jmlrt](https://github.com/jmlrt)                       | [elasticsearch][kibana] remove oss examples (#1046)                                                                          |
| [#1040](https://github.com/elastic/helm-charts/pull/1040) | [@daniel-hutao](https://github.com/daniel-hutao)         | [elasticsearch] Fix security.yaml is 404                                                                                     |
| [#1039](https://github.com/elastic/helm-charts/pull/1039) | [@yousafsyed](https://github.com/yousafsyed)             | [metricbeat] Fixing the repository of kube-state-metrics for metricbeats                                                     |
| [#809](https://github.com/elastic/helm-charts/pull/809)   | [@clemcvlcs](https://github.com/clemcvlcs)               | [filebeat] Variable maxUnavailable updateStrategy                                                                            |
| [#1033](https://github.com/elastic/helm-charts/pull/1033) | [@jmlrt](https://github.com/jmlrt)                       | [meta] Add build status and artifact hub badges                                                                              |
| [#1028](https://github.com/elastic/helm-charts/pull/1028) | [@artificial-aidan](https://github.com/artificial-aidan) | [kibana] Fix post-lifecycle hook example                                                                                     |
| [#1025](https://github.com/elastic/helm-charts/pull/1025) | [@jmlrt](https://github.com/jmlrt)                       | [meta] Bump helm version to 3.5.0                                                                                            |
| [#1018](https://github.com/elastic/helm-charts/pull/1018) | [@jmlrt](https://github.com/jmlrt)                       | [meta] Fix transient errors with stable repository                                                                           |
| [#1022](https://github.com/elastic/helm-charts/pull/1022) | [@jmlrt](https://github.com/jmlrt)                       | [meta] Small fixes for 7.11 branch                                                                                           |
| [#1017](https://github.com/elastic/helm-charts/pull/1017) | [@jmlrt](https://github.com/jmlrt)                       | [meta] NIT Update backport config and small doc fixes                                                                        |
| [#1012](https://github.com/elastic/helm-charts/pull/1012) | [@jmlrt](https://github.com/jmlrt)                       | [elasticsearch] Fix secrets in config example                                                                                |
| [#996](https://github.com/elastic/helm-charts/pull/996)   | [@jmlrt](https://github.com/jmlrt)                       | [apm-server] Run as non root user                                                                                            |
| [#1000](https://github.com/elastic/helm-charts/pull/1000) | [@jmlrt](https://github.com/jmlrt)                       | [logstash] Disable privileged container in psp                                                                               |
| [#498](https://github.com/elastic/helm-charts/pull/498)   | [@desaintmartin](https://github.com/desaintmartin)       | [elasticsearch] Add support for NetworkPolicy.                                                                               |
| [#994](https://github.com/elastic/helm-charts/pull/994)   | [@kevinsmithwrs](https://github.com/kevinsmithwrs)       | [elasticsearch][kibana] Add flexible ingress                                                                                 |
| [#1011](https://github.com/elastic/helm-charts/pull/1011) | [@kwsorensen](https://github.com/kwsorensen)             | [filebeat][metricbeat] Update documentation on port collisions for multiple beats agents with hostNetworking enabled. (#997) |
| [#1007](https://github.com/elastic/helm-charts/pull/1007) | [@njgibbon](https://github.com/njgibbon)                 | [filebeat] Configurable ClusterRole (#978)                                                                                   |
| [#1005](https://github.com/elastic/helm-charts/pull/1005) | [@operatorequals](https://github.com/operatorequals)     | [filebeat] Deployment support feature (#964)                                                                                 |
| [#985](https://github.com/elastic/helm-charts/pull/985)   | [@jmlrt](https://github.com/jmlrt)                       | [all] Add hostaliases (#970)                                                                                                 |
| [#982](https://github.com/elastic/helm-charts/pull/982)   | [@unki](https://github.com/unki)                         | [elasticsearch] Add emptyDir to podSecurityPolicy as allowed volume-type (#975)                                              |
| [#974](https://github.com/elastic/helm-charts/pull/974)   | [@jmlrt](https://github.com/jmlrt)                       | [meta] Add config for backport (#971)                                                                                        |
| [#959](https://github.com/elastic/helm-charts/pull/959)   | [@ebuildy](https://github.com/ebuildy)                   | [kibana] Add service.httpPortName config in chart (#843)                                                                     |
| [#956](https://github.com/elastic/helm-charts/pull/956)   | [@david92rl](https://github.com/david92rl)               | [apm-server] Add missing fields to HPA (#782)                                                                                |
| [#951](https://github.com/elastic/helm-charts/pull/951)   | [@jmlrt](https://github.com/jmlrt)                       | [meta] Enable metricbeat upgrade test (#940)                                                                                 |
| [#946](https://github.com/elastic/helm-charts/pull/946)   | [@micborens](https://github.com/micborens)               | [logstash] Add rbac custom annotations (#764)                                                                                |
| [#943](https://github.com/elastic/helm-charts/pull/943)   | [@cloudziu](https://github.com/cloudziu)                 | [elasticsearch] Statefulset empty initContainers fix (#795)                                                                  |
| [#938](https://github.com/elastic/helm-charts/pull/938)   | [@jmlrt](https://github.com/jmlrt)                       | [meta] Stabilize CI tests (#935)                                                                                             |
| [#928](https://github.com/elastic/helm-charts/pull/928)   | [@jmlrt](https://github.com/jmlrt)                       | [meta] Remove version from dev install section title                                                                         |
| [#923](https://github.com/elastic/helm-charts/pull/923)   | [@jmlrt](https://github.com/jmlrt)                       | [meta] Remove support for k8s <1.14 & helm <2.17.0 (#916)                                                                    |
| [#920](https://github.com/elastic/helm-charts/pull/920)   | [@jmlrt](https://github.com/jmlrt)                       | [meta] Upgrade test (#907)                                                                                                   |


## 6.8.14

* 6.8.14 as default version.


| PR                                                        | Author                                                   | Title                                                                                                                        |
|-----------------------------------------------------------|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [#1040](https://github.com/elastic/helm-charts/pull/1040) | [@daniel-hutao](https://github.com/daniel-hutao)         | [elasticsearch] Fix security.yaml is 404                                                                                     |
| [#1039](https://github.com/elastic/helm-charts/pull/1039) | [@yousafsyed](https://github.com/yousafsyed)             | [metricbeat] Fixing the repository of kube-state-metrics for metricbeats                                                     |
| [#809](https://github.com/elastic/helm-charts/pull/809)   | [@clemcvlcs](https://github.com/clemcvlcs)               | [filebeat] Variable maxUnavailable updateStrategy                                                                            |
| [#1033](https://github.com/elastic/helm-charts/pull/1033) | [@jmlrt](https://github.com/jmlrt)                       | [meta] Add build status and artifact hub badges                                                                              |
| [#1028](https://github.com/elastic/helm-charts/pull/1028) | [@artificial-aidan](https://github.com/artificial-aidan) | [kibana] Fix post-lifecycle hook example                                                                                     |
| [#1025](https://github.com/elastic/helm-charts/pull/1025) | [@jmlrt](https://github.com/jmlrt)                       | [meta] Bump helm version to 3.5.0                                                                                            |
| [#1018](https://github.com/elastic/helm-charts/pull/1018) | [@jmlrt](https://github.com/jmlrt)                       | [meta] Fix transient errors with stable repository                                                                           |
| [#1017](https://github.com/elastic/helm-charts/pull/1017) | [@jmlrt](https://github.com/jmlrt)                       | [meta] NIT Update backport config and small doc fixes                                                                        |
| [#1012](https://github.com/elastic/helm-charts/pull/1012) | [@jmlrt](https://github.com/jmlrt)                       | [elasticsearch] Fix secrets in config example                                                                                |
| [#996](https://github.com/elastic/helm-charts/pull/996)   | [@jmlrt](https://github.com/jmlrt)                       | [apm-server] Run as non root user                                                                                            |
| [#1000](https://github.com/elastic/helm-charts/pull/1000) | [@jmlrt](https://github.com/jmlrt)                       | [logstash] Disable privileged container in psp                                                                               |
| [#498](https://github.com/elastic/helm-charts/pull/498)   | [@desaintmartin](https://github.com/desaintmartin)       | [elasticsearch] Add support for NetworkPolicy.                                                                               |
| [#994](https://github.com/elastic/helm-charts/pull/994)   | [@kevinsmithwrs](https://github.com/kevinsmithwrs)       | [elasticsearch][kibana] Add flexible ingress                                                                                 |
| [#1009](https://github.com/elastic/helm-charts/pull/1009) | [@kwsorensen](https://github.com/kwsorensen)             | [filebeat][metricbeat] Update documentation on port collisions for multiple beats agents with hostNetworking enabled. (#997) |
| [#1006](https://github.com/elastic/helm-charts/pull/1006) | [@njgibbon](https://github.com/njgibbon)                 | [filebeat] Configurable ClusterRole (#978)                                                                                   |
| [#1004](https://github.com/elastic/helm-charts/pull/1004) | [@operatorequals](https://github.com/operatorequals)     | [filebeat] Deployment support feature (#964)                                                                                 |
| [#983](https://github.com/elastic/helm-charts/pull/983)   | [@jmlrt](https://github.com/jmlrt)                       | [all] Add hostaliases (#970)                                                                                                 |
| [#980](https://github.com/elastic/helm-charts/pull/980)   | [@unki](https://github.com/unki)                         | [elasticsearch] Add emptyDir to podSecurityPolicy as allowed volume-type (#975)                                              |
| [#972](https://github.com/elastic/helm-charts/pull/972)   | [@jmlrt](https://github.com/jmlrt)                       | [meta] Add config for backport (#971)                                                                                        |
| [#957](https://github.com/elastic/helm-charts/pull/957)   | [@ebuildy](https://github.com/ebuildy)                   | [kibana] Add service.httpPortName config in chart (#843)                                                                     |
| [#954](https://github.com/elastic/helm-charts/pull/954)   | [@david92rl](https://github.com/david92rl)               | [apm-server] Add missing fields to HPA (#782)                                                                                |
| [#944](https://github.com/elastic/helm-charts/pull/944)   | [@micborens](https://github.com/micborens)               | [logstash] Add rbac custom annotations (#764)                                                                                |
| [#941](https://github.com/elastic/helm-charts/pull/941)   | [@cloudziu](https://github.com/cloudziu)                 | [elasticsearch] Statefulset empty initContainers fix (#795)                                                                  |
| [#936](https://github.com/elastic/helm-charts/pull/936)   | [@jmlrt](https://github.com/jmlrt)                       | [meta] Stabilize CI tests (#935)                                                                                             |
| [#921](https://github.com/elastic/helm-charts/pull/921)   | [@jmlrt](https://github.com/jmlrt)                       | [meta] Remove support for k8s <1.14 & helm <2.17.0 (#916)                                                                    |
| [#918](https://github.com/elastic/helm-charts/pull/918)   | [@jmlrt](https://github.com/jmlrt)                       | [meta] Upgrade test (#907)                                                                                                   |
| [#897](https://github.com/elastic/helm-charts/pull/897)   | [@cospeedster](https://github.com/cospeedster)           | [elasticsearch] Fix spelling                                                                                                 |
| [#911](https://github.com/elastic/helm-charts/pull/911)   | [@jmlrt](https://github.com/jmlrt)                       | [elasticsearch] Update test hook annotations                                                                                 |
| [#910](https://github.com/elastic/helm-charts/pull/910)   | [@jmlrt](https://github.com/jmlrt)                       | [meta] Add link to eck chart doc                                                                                             |
| [#904](https://github.com/elastic/helm-charts/pull/904)   | [@jmlrt](https://github.com/jmlrt)                       | [meta] Helm 3 (#516)                                                                                                         |
| [#891](https://github.com/elastic/helm-charts/pull/891)   | [@jmlrt](https://github.com/jmlrt)                       | [meta] Increase helm timeout                                                                                                 |
| [#890](https://github.com/elastic/helm-charts/pull/890)   | [@jmlrt](https://github.com/jmlrt)                       | [meta] Update rbac.authorization.k8s.io api                                                                                  |
| [#888](https://github.com/elastic/helm-charts/pull/888)   | [@nkammah](https://github.com/nkammah)                   | [meta] Add warning comment placeholder (6.8 branch)                                                                          |
| [#882](https://github.com/elastic/helm-charts/pull/882)   | [@jmlrt](https://github.com/jmlrt)                       | [metricbeat] Use relocated stable repo for kube-state-metrics                                                                |
| [#880](https://github.com/elastic/helm-charts/pull/880)   | [@jmlrt](https://github.com/jmlrt)                       | [meta] Add support for helm 2.17.0 and k8s 1.17                                                                              |
| [#878](https://github.com/elastic/helm-charts/pull/878)   | [@jmlrt](https://github.com/jmlrt)                       | [elasticsearch] Remove roles unavailable on 6.8                                                                              |
| [#854](https://github.com/elastic/helm-charts/pull/854)   | [@jmlrt](https://github.com/jmlrt)                       | [elasticsearch] Add coordinator node to multi test                                                                           |


## 7.10.2

* 7.10.2 as default version.


| PR                                                        | Author                                               | Title                                                                                                                        |
|-----------------------------------------------------------|------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [#1017](https://github.com/elastic/helm-charts/pull/1017) | [@jmlrt](https://github.com/jmlrt)                   | NIT Update backport config and small doc fixes                                                                               |
| [#1010](https://github.com/elastic/helm-charts/pull/1010) | [@kwsorensen](https://github.com/kwsorensen)         | [filebeat][metricbeat] Update documentation on port collisions for multiple beats agents with hostNetworking enabled. (#997) |
| [#984](https://github.com/elastic/helm-charts/pull/984)   | [@jmlrt](https://github.com/jmlrt)                   | [7.10] [all] add hostaliases (#970)                                                                                          |
| [#981](https://github.com/elastic/helm-charts/pull/981)   | [@unki](https://github.com/unki)                     | [7.10] elasticsearch: add emptyDir to podSecurityPolicy as allowed volume-type (#975)                                        |
| [#987](https://github.com/elastic/helm-charts/pull/987)   | [@jmlrt](https://github.com/jmlrt)                   | [7.10] [meta] bump helm to 3.4.2 (#977)                                                                                      |
| [#968](https://github.com/elastic/helm-charts/pull/968)   | [@elasticmachine](https://github.com/elasticmachine) | Bump version to 7.10.2-SNAPSHOT                                                                                              |
| [#973](https://github.com/elastic/helm-charts/pull/973)   | [@jmlrt](https://github.com/jmlrt)                   | [7.10] [meta] add config for backport (#971)                                                                                 |


## 7.10.1

* 7.10.1 as default version.


| PR                                                      | Author                                               | Title                                                           |
|---------------------------------------------------------|------------------------------------------------------|-----------------------------------------------------------------|
| [#958](https://github.com/elastic/helm-charts/pull/958) | [@ebuildy](https://github.com/ebuildy)               | [7.10] [kibana] add service.httpPortName config in chart (#843) |
| [#955](https://github.com/elastic/helm-charts/pull/955) | [@david92rl](https://github.com/david92rl)           | [7.10] [apm-server] Add missing fields to HPA (#782)            |
| [#950](https://github.com/elastic/helm-charts/pull/950) | [@jmlrt](https://github.com/jmlrt)                   | [7.10] [meta] enable metricbeat upgrade test (#940)             |
| [#945](https://github.com/elastic/helm-charts/pull/945) | [@micborens](https://github.com/micborens)           | [7.10] [logstash] add rbac custom annotations (#764)            |
| [#942](https://github.com/elastic/helm-charts/pull/942) | [@cloudziu](https://github.com/cloudziu)             | [7.10] ES Statefulset empty initContainers fix (#795)           |
| [#932](https://github.com/elastic/helm-charts/pull/932) | [@elasticmachine](https://github.com/elasticmachine) | Bump 7.10 branch to 7.10.1-SNAPSHOT                             |
| [#937](https://github.com/elastic/helm-charts/pull/937) | [@jmlrt](https://github.com/jmlrt)                   | [7.10] [meta] stabilize CI tests (#935)                         |


## 7.10.0

* 7.10.0 as default version.


| PR                                                      | Author                                         | Title                                                            |
|---------------------------------------------------------|------------------------------------------------|------------------------------------------------------------------|
| [#927](https://github.com/elastic/helm-charts/pull/927) | [@jmlrt](https://github.com/jmlrt)             | [meta] Remove version from dev install section title             |
| [#922](https://github.com/elastic/helm-charts/pull/922) | [@jmlrt](https://github.com/jmlrt)             | [meta] Remove support for k8s <1.14 & helm <2.17.0 (#916) [7.10] |
| [#919](https://github.com/elastic/helm-charts/pull/919) | [@jmlrt](https://github.com/jmlrt)             | [meta] Upgrade test (#907) [7.10]                                |
| [#914](https://github.com/elastic/helm-charts/pull/914) | [@jmlrt](https://github.com/jmlrt)             | [meta] Initiate 7.10 branch                                      |
| [#897](https://github.com/elastic/helm-charts/pull/897) | [@cospeedster](https://github.com/cospeedster) | [elasticsearch] Fix spelling                                     |
| [#911](https://github.com/elastic/helm-charts/pull/911) | [@jmlrt](https://github.com/jmlrt)             | [elasticsearch] Update test hook annotations                     |
| [#910](https://github.com/elastic/helm-charts/pull/910) | [@jmlrt](https://github.com/jmlrt)             | [meta] Add link to eck chart doc                                 |
| [#902](https://github.com/elastic/helm-charts/pull/902) | [@jmlrt](https://github.com/jmlrt)             | [meta] Helm 3 (#516)                                             |
| [#891](https://github.com/elastic/helm-charts/pull/891) | [@jmlrt](https://github.com/jmlrt)             | [meta] Increase helm timeout                                     |
| [#890](https://github.com/elastic/helm-charts/pull/890) | [@jmlrt](https://github.com/jmlrt)             | [meta] Update rbac.authorization.k8s.io api                      |
| [#887](https://github.com/elastic/helm-charts/pull/887) | [@nkammah](https://github.com/nkammah)         | [meta] Add warning comment placeholder (7.x branch)              |
| [#882](https://github.com/elastic/helm-charts/pull/882) | [@jmlrt](https://github.com/jmlrt)             | [metricbeat] Use relocated stable repo for kube-state-metrics    |
| [#880](https://github.com/elastic/helm-charts/pull/880) | [@jmlrt](https://github.com/jmlrt)             | [meta] Add support for helm 2.17.0 and k8s 1.17                  |
| [#854](https://github.com/elastic/helm-charts/pull/854) | [@jmlrt](https://github.com/jmlrt)             | [elasticsearch] Add coordinator node to multi test               |
| [#860](https://github.com/elastic/helm-charts/pull/860) | [@nkammah](https://github.com/nkammah)         | [meta] Simplify doc in 7.x branch                                |


## 7.9.3

* 7.9.3 as default version.

| PR                                                      | Author                                   | Title                                                            |
|---------------------------------------------------------|------------------------------------------|------------------------------------------------------------------|
| [#859](https://github.com/elastic/helm-charts/pull/859) | [@nkammah](https://github.com/nkammah)   | [all] Simplify doc in 7.9 branch                                 |
| [#767](https://github.com/elastic/helm-charts/pull/767) | [@ebuildy](https://github.com/ebuildy)   | [Metricbeat] Dont generate config if not enabled                 |
| [#793](https://github.com/elastic/helm-charts/pull/793) | [@jnbelo](https://github.com/jnbelo)     | fixup! Added ingress support to the logstash chart               |
| [#793](https://github.com/elastic/helm-charts/pull/793) | [@jnbelo](https://github.com/jnbelo)     | Added ingress support to the logstash chart                      |
| [#839](https://github.com/elastic/helm-charts/pull/839) | [@jmlrt](https://github.com/jmlrt)       | [logstash] use only httpPort in headless service                 |
| [#659](https://github.com/elastic/helm-charts/pull/659) | [@orong-pp](https://github.com/orong-pp) | [filebeat] introduce dnsConfig values for the containers         |
| [#820](https://github.com/elastic/helm-charts/pull/820) | [@v1r7u](https://github.com/v1r7u)       | [metricbeat] support deployment/daemonset specific metrics       |
| [#831](https://github.com/elastic/helm-charts/pull/831) | [@nkammah](https://github.com/nkammah)   | 7.9.3 snapshot                                                   |
| [#717](https://github.com/elastic/helm-charts/pull/717) | [@qqshfox](https://github.com/qqshfox)   | support tpl in logstashConfig, logstashPipeline and kibanaConfig |
| [#818](https://github.com/elastic/helm-charts/pull/818) | [@jmlrt](https://github.com/jmlrt)       | [elasticsearch][kibana] disable nss dentry cache                 |

## 6.8.13

* 6.8.13 as default version.

| PR                                                      | Author                                                 | Title                                                            |
|---------------------------------------------------------|--------------------------------------------------------|------------------------------------------------------------------|
| [#858](https://github.com/elastic/helm-charts/pull/858) | [@nkammah](https://github.com/nkammah)                 | [all] Simplify doc in 6.8 branch                                 |
| [#767](https://github.com/elastic/helm-charts/pull/767) | [@ebuildy](https://github.com/ebuildy)                 | [Metricbeat] Dont generate config if not enabled                 |
| [#793](https://github.com/elastic/helm-charts/pull/793) | [@jnbelo](https://github.com/jnbelo)                   | Added ingress support to the logstash chart                      |
| [#839](https://github.com/elastic/helm-charts/pull/839) | [@jmlrt](https://github.com/jmlrt)                     | [logstash] use only httpPort in headless service                 |
| [#659](https://github.com/elastic/helm-charts/pull/659) | [@orong-pp](https://github.com/orong-pp)               | [filebeat] introduce dnsConfig values for the containers         |
| [#820](https://github.com/elastic/helm-charts/pull/820) | [@v1r7u](https://github.com/v1r7u)                     | [metricbeat] support deployment/daemonset specific metrics       |
| [#717](https://github.com/elastic/helm-charts/pull/717) | [@qqshfox](https://github.com/qqshfox)                 | support tpl in logstashConfig, logstashPipeline and kibanaConfig |
| [#818](https://github.com/elastic/helm-charts/pull/818) | [@jmlrt](https://github.com/jmlrt)                     | [elasticsearch][kibana] disable nss dentry cache                 |
| [#816](https://github.com/elastic/helm-charts/pull/816) | [@jmlrt](https://github.com/jmlrt)                     | [helm] bump helm version to 2.16.12                              |
| [#811](https://github.com/elastic/helm-charts/pull/811) | [@jmlrt](https://github.com/jmlrt)                     | [elasticsearch] fix secrets names in examples                    |
| [#729](https://github.com/elastic/helm-charts/pull/729) | [@floretan](https://github.com/floretan)               | Include pre-releases in the semver range.                        |
| [#810](https://github.com/elastic/helm-charts/pull/810) | [@luanguimaraesla](https://github.com/luanguimaraesla) | [elasticsearch] add loadBalancer externalTrafficPolicy option    |
| [#778](https://github.com/elastic/helm-charts/pull/778) | [@erihanse](https://github.com/erihanse)               | [metricbeat] Support secrets                                     |
| [#786](https://github.com/elastic/helm-charts/pull/786) | [@caiconkhicon](https://github.com/caiconkhicon)       | Fix serviceAccount for APM server                                |
| [#770](https://github.com/elastic/helm-charts/pull/770) | [@vliubko](https://github.com/vliubko)                 | [metricbeat] Add missing labels for deployment                   |
| [#776](https://github.com/elastic/helm-charts/pull/776) | [@itssimon](https://github.com/itssimon)               | [logstash] Fix headless service ports spec                       |
| [#763](https://github.com/elastic/helm-charts/pull/763) | [@ebuildy](https://github.com/ebuildy)                 | Remove duplicate "initialDelaySeconds" field                     |
| [#752](https://github.com/elastic/helm-charts/pull/752) | [@AhmedSamirAhmed](https://github.com/AhmedSamirAhmed) | Missing deletion of "elastic-certificate-crt"                    |
| [#744](https://github.com/elastic/helm-charts/pull/744) | [@SlavaSubotskiy](https://github.com/SlavaSubotskiy)   | Fix typo in FAQ                                                  |
| [#797](https://github.com/elastic/helm-charts/pull/797) | [@jmlrt](https://github.com/jmlrt)                     | [helm] bump helm version to 2.16.10                              |
| [#798](https://github.com/elastic/helm-charts/pull/798) | [@jmlrt](https://github.com/jmlrt)                     | [meta] drop gke 1.14 tests                                       |
| [#790](https://github.com/elastic/helm-charts/pull/790) | [@ygel](https://github.com/ygel)                       | Bump version to 6.8.13-SNAPSHOT                                  |

## 7.9.2 - 2020/09/24
* 7.9.2 as the default stack version
* Bump Helm version to 2.16.12 ([@jmlrt](https://github.com/jmlrt))

### Elasticsearch

| PR                                                      | Author                                                 | Title                                         |
|---------------------------------------------------------|--------------------------------------------------------|-----------------------------------------------|
| [#729](https://github.com/elastic/helm-charts/pull/729) | [@floretan](https://github.com/floretan)               | Include pre-releases in the semver range.     |
| [#810](https://github.com/elastic/helm-charts/pull/810) | [@luanguimaraesla](https://github.com/luanguimaraesla) | Add loadBalancer externalTrafficPolicy option |
| [#778](https://github.com/elastic/helm-charts/pull/811) | [@jmlrt ](https://github.com/jmlrt)                    | Fix secrets names in examples                 |

### Metricbeat

| PR                                                      | Author                                  | Title           |
|---------------------------------------------------------|-----------------------------------------|-----------------|
| [#778](https://github.com/elastic/helm-charts/pull/778) | [erihanse](https://github.com/erihanse) | Support secrets |


## 7.9.1 - 2020/09/03
* 7.9.1 as the default stack version
* Helm 2.16.10 support in [#797](https://github.com/elastic/helm-charts/pull/797) [@jmlrt](https://github.com/jmlrt)
* Drop GKE 1.14 tests in [#798](https://github.com/elastic/helm-charts/pull/798) [@jmlrt](https://github.com/jmlrt)

### APM Server

| PR                                                      | Author                                           | Title                                        |
|---------------------------------------------------------|--------------------------------------------------|----------------------------------------------|
| [#763](https://github.com/elastic/helm-charts/pull/763) | [@ebuildy](https://github.com/ebuildy)           | Remove duplicate `initialDelaySeconds` field |
| [#786](https://github.com/elastic/helm-charts/pull/786) | [@caiconkhicon](https://github.com/caiconkhicon) | Fix `serviceAccount`                         |

### Elasticsearch

| PR                                                      | Author                                                 | Title                                                             |
|---------------------------------------------------------|--------------------------------------------------------|-------------------------------------------------------------------|
| [#752](https://github.com/elastic/helm-charts/pull/752) | [@AhmedSamirAhmed](https://github.com/AhmedSamirAhmed) | Remove `elastic-certificate-crt` in security example clean target |

### Logstash

| PR                                                      | Author                                  | Title                           |
|---------------------------------------------------------|-----------------------------------------|---------------------------------|
| [#776](https://github.com/elastic/helm-charts/pull/776) | [itssimon](https://github.com/itssimon) | Fix headless service ports spec |

### Metricbeat

| PR                                                      | Author                                | Title                             |
|---------------------------------------------------------|---------------------------------------|-----------------------------------|
| [#770](https://github.com/elastic/helm-charts/pull/770) | [vliubko](https://github.com/vliubko) | Add missing labels for deployment |


## 7.9.0 - 2020/08/18
* 7.9.0 as the default stack version
* Add Helm 3 support in beta ([@jmlrt](https://github.com/jmlrt))
* Some improvements in CI tests jobs ([@jmlrt](https://github.com/jmlrt))



## 6.8.12 - 2020/08/18

* 6.8.12 as the default stack version
* See [7.9.0 CHANGELOG](#790---20200818) for other changes


## 7.8.1 - 2020/07/28

* 7.8.1 as the default stack version
* Some documentation fixes and improvements ([@ArthurFritz](https://github.com/ArthurFritz), [@fatmcgav](https://github.com/fatmcgav) and [AhmedSamirAhmed](https://github.com/AhmedSamirAhmed))
* Some improvements in CI tests jobs ([@jmlrt](https://github.com/jmlrt)) and [@fatmcgav](https://github.com/fatmcgav))

### APM Server

| PR                                                      | Author                                             | Title                          |
|---------------------------------------------------------|----------------------------------------------------|--------------------------------|
| [#686](https://github.com/elastic/helm-charts/pull/686) | [@jim-barber-he](https://github.com/jim-barber-he) | Add ServiceAccount annotations |

### Elasticsearch

| PR                                                      | Author                                             | Title                                                                            |
|---------------------------------------------------------|----------------------------------------------------|----------------------------------------------------------------------------------|
| [#655](https://github.com/elastic/helm-charts/pull/655) | [@mephinet](https://github.com/mephinet)           | `podSecurityContext.runAsUser` needs to be nulled as well for Openshift          |
| [#686](https://github.com/elastic/helm-charts/pull/686) | [@jim-barber-he](https://github.com/jim-barber-he) | Add ServiceAccount annotations                                                   |
| [#665](https://github.com/elastic/helm-charts/pull/665) | [@desaintmartin](https://github.com/desaintmartin) | Set PVC labels through setting all StatefulSet labels to its volumeClaimTemplate |
| [#670](https://github.com/elastic/helm-charts/pull/670) | [@xario](https://github.com/xario)                 | Update `elasticsearch.endpoints` to use `elasticsearch.uname`                    |
| [#727](https://github.com/elastic/helm-charts/pull/727) | [@fhaase2](https://github.com/fhaase2)             | Update test image pull policy                                                    |

### Filebeat

| PR                                                      | Author                                             | Title                                      |
|---------------------------------------------------------|----------------------------------------------------|--------------------------------------------|
| [#686](https://github.com/elastic/helm-charts/pull/686) | [@jim-barber-he](https://github.com/jim-barber-he) | Add ServiceAccount annotations             |
| [#704](https://github.com/elastic/helm-charts/pull/704) | [@bmilescu](https://github.com/bmilescu)           | Add permission to list nodes               |
| [#699](https://github.com/elastic/helm-charts/pull/699) | [@jmlrt](https://github.com/jmlrt)                 | Document probe workaround for Kafka output |

### Kibana

| PR                                                      | Author                                               | Title                              |
|---------------------------------------------------------|------------------------------------------------------|------------------------------------|
| [#726](https://github.com/elastic/helm-charts/pull/726) | [@debojitkakoti ](https://github.com/debojitkakoti ) | Add loadbalancerIP to Service spec |


### Logstash

| PR                                                      | Author                                             | Title                                     |
|---------------------------------------------------------|----------------------------------------------------|-------------------------------------------|
| [#686](https://github.com/elastic/helm-charts/pull/686) | [@jim-barber-he](https://github.com/jim-barber-he) | Add ServiceAccount annotations            |
| [#695](https://github.com/elastic/helm-charts/pull/695) | [@jmlrt](https://github.com/jmlrt)                 | Add headless service for StatefulSet      |
| [#712](https://github.com/elastic/helm-charts/pull/712) | [@kksudo](https://github.com/kksudo)               | Support creating secrets                  |
| [#723](https://github.com/elastic/helm-charts/pull/723) | [@kksudo](https://github.com/kksudo)               | Restart pod when the secrets have changed |

### Metricbeat

| PR                                                      | Author                                               | Title                                           |
|---------------------------------------------------------|------------------------------------------------------|-------------------------------------------------|
| [#686](https://github.com/elastic/helm-charts/pull/686) | [@jim-barber-he](https://github.com/jim-barber-he)   | Add ServiceAccount annotations support          |
| [#713](https://github.com/elastic/helm-charts/pull/713) | [@kernkonzentrat](https://github.com/kernkonzentrat) | Add DaemonSet and Deployment annotation support |
| [#716](https://github.com/elastic/helm-charts/pull/716) | [@erihanse](https://github.com/erihanse)             | Make DaemonSet and Deployment optional          |
| [#387](https://github.com/elastic/helm-charts/pull/387) | [@SergK](https://github.com/SergK)                   | Make kube-state-metrics optional                |


## 6.8.11 - 2020/07/28

* 6.8.11 as the default stack version
* See [7.8.1 CHANGELOG](#781---20200728) for other changes


## 7.8.0 - 2020/06/18

* 7.8.0 as the default stack version
* Helm 2.16.9 support in [#667](https://github.com/elastic/helm-charts/pull/667) [@jmlrt](https://github.com/jmlrt)


### APM Server

| PR                                                      | Author                             | Title                    |
|---------------------------------------------------------|------------------------------------|--------------------------|
| [#664](https://github.com/elastic/helm-charts/pull/664) | [@jmlrt](https://github.com/jmlrt) | Increase memory limit    |
| [#671](https://github.com/elastic/helm-charts/pull/671) | [@jmlrt](https://github.com/jmlrt) | Allow customizing probes |


### Elasticsearch

| PR                                                      | Author                                            | Title                                                    |
|---------------------------------------------------------|---------------------------------------------------|----------------------------------------------------------|
| [#437](https://github.com/elastic/helm-charts/pull/437) | [desaintmartin](https://github.com/desaintmartin) | Remove `heritage` from selector                          |
| [#542](https://github.com/elastic/helm-charts/pull/542) | [@floretan](https://github.com/floretan)          | Disable service links to prevent very long startup times |
| [#671](https://github.com/elastic/helm-charts/pull/671) | [@jmlrt](https://github.com/jmlrt)                | Update kind example for version >= 0.7.0                 |


### Logstash

| PR                                                      | Author                             | Title                |
|---------------------------------------------------------|------------------------------------|----------------------|
| [#392](https://github.com/elastic/helm-charts/pull/392) | [@jmlrt](https://github.com/jmlrt) | Add security example |


## 7.7.1 - 2020/06/03

* 7.7.1 as the default stack version
* K8S 1.16 support in [#635](https://github.com/elastic/helm-charts/pull/635) [@jmlrt](https://github.com/jmlrt)


### Elasticsearch

| PR                                                      | Author                                      | Title                                           |
|---------------------------------------------------------|---------------------------------------------|-------------------------------------------------|
| [#596](https://github.com/elastic/helm-charts/pull/596) | [domgoodwin](https://github.com/domgoodwin) | Elasticsearch secret mount mode                 |
| [#638](https://github.com/elastic/helm-charts/pull/638) | [@fatmcgav](https://github.com/fatmcgav)    | Fix issue with `readinessProbe` causing outages |
| [#639](https://github.com/elastic/helm-charts/pull/639) | [@coolbaluk](https://github.com/coolbaluk)  | Fix values links in `examples/multi/README.md`  |

### Kibana

| PR                                                      | Author                                         | Title                                                                      |
|---------------------------------------------------------|------------------------------------------------|----------------------------------------------------------------------------|
| [#555](https://github.com/elastic/helm-charts/pull/555) | [@ramrodo](https://github.com/ramrodo)         | Add extensible label support on Kibana                                     |
| [#637](https://github.com/elastic/helm-charts/pull/637) | [@maxkochubey](https://github.com/maxkochubey) | String/YAML conditions for `.Values.{extraContainers,extraInitContainers}` |

### Metricbeat

| PR                                                      | Author                                 | Title                                                                            |
|---------------------------------------------------------|----------------------------------------|----------------------------------------------------------------------------------|
| [#622](https://github.com/elastic/helm-charts/pull/622) | [@jmlrt](https://github.com/jmlrt)     | Fix deployment upgrade by removing chart label from `.spec.selector.matchLabels` |
| [#624](https://github.com/elastic/helm-charts/pull/624) | [@jmlrt](https://github.com/jmlrt)     | Use deprecated `kube-state-metrics-metricbeat.yml` when existing                 |
| [#634](https://github.com/elastic/helm-charts/pull/634) | [@MaxRink](https://github.com/MaxRink) | Fix `configChecksum` not being set                                               |

## 6.8.10 - 2020/06/03

* 6.8.10 as the default stack version
* See [7.7.1 CHANGELOG](#771---20200603) for other changes

## 7.7.0 - 2020/05/13

* 7.7.0 as the default stack version
* Elasticsearch chart is moving to GA
* Kibana chart is moving to GA
* Filebeat chart is moving to GA
* Metricbeat chart is moving to GA
* Using [new branching model](https://github.com/elastic/helm-charts/blob/main/CONTRIBUTING.md#branching) in [#541](https://github.com/elastic/helm-charts/pull/541) [@mgreau](https://github.com/mgreau)
* Helm 2.16.7 support in [#607](https://github.com/elastic/helm-charts/pull/607) [@jmlrt](https://github.com/jmlrt)
* Docs improvements in [#593](https://github.com/elastic/helm-charts/pull/593) and [#598](https://github.com/elastic/helm-charts/pull/598) [@jmlrt](https://github.com/jmlrt)
* Tests with SNAPSHOT Docker images in [#581](https://github.com/elastic/helm-charts/pull/581) [@mgreau](https://github.com/mgreau)
* Version bumping script enhancements in [#601](https://github.com/elastic/helm-charts/pull/601) [@jmlrt](https://github.com/jmlrt)


### APM Server

| PR                                                      | Author                                                 | Title                   |
|---------------------------------------------------------|--------------------------------------------------------|-------------------------|
| [#569](https://github.com/elastic/helm-charts/pull/569) | [@cartonalexandre](https://github.com/cartonalexandre) | Add support for envFrom |

### Elasticsearch

| PR                                                      | Author                                                 | Title                                             |
|---------------------------------------------------------|--------------------------------------------------------|---------------------------------------------------|
| [#522](https://github.com/elastic/helm-charts/pull/522) | [@domgoodwin](https://github.com/domgoodwin)           | Update defaults for extra values to support lists |
| [#569](https://github.com/elastic/helm-charts/pull/569) | [@cartonalexandre](https://github.com/cartonalexandre) | Add support for envFrom                           |
| [#583](https://github.com/elastic/helm-charts/pull/583) | [@Conky5](https://github.com/Conky5)                   | Use busybox for key generation in testing         |
| [#584](https://github.com/elastic/helm-charts/pull/584) | [@michelesr](https://github.com/michelesr)             | Set securityContext for test pod                  |
| [#586](https://github.com/elastic/helm-charts/pull/586) | [@jmlrt](https://github.com/jmlrt)                     | Update readiness probe endpoint                   |
| [#590](https://github.com/elastic/helm-charts/pull/590) | [@marcostvz](https://github.com/marcostvz)             | Adds imagePullSecrets for test Pod                |

### Filebeat

| PR                                                      | Author                             | Title                 |
|---------------------------------------------------------|------------------------------------|-----------------------|
| [#568](https://github.com/elastic/helm-charts/pull/568) | [@jmlrt](https://github.com/jmlrt) | Filebeat improvements |

### Kibana

| PR                                                      | Author                                                 | Title                                       |
|---------------------------------------------------------|--------------------------------------------------------|---------------------------------------------|
| [#549](https://github.com/elastic/helm-charts/pull/549) | [@kuisathaverat](https://github.com/kuisathaverat)     | Fix allow redirection on the readinessProbe |
| [#583](https://github.com/elastic/helm-charts/pull/583) | [@Conky5](https://github.com/Conky5)                   | Use busybox for key generation in testing   |
| [#569](https://github.com/elastic/helm-charts/pull/569) | [@cartonalexandre](https://github.com/cartonalexandre) | Add support for envFrom                     |

### Logstash

| PR                                                      | Author                                                 | Title                                           |
|---------------------------------------------------------|--------------------------------------------------------|-------------------------------------------------|
| [#569](https://github.com/elastic/helm-charts/pull/569) | [@cartonalexandre](https://github.com/cartonalexandre) | Add support for envFrom                         |
| [#591](https://github.com/elastic/helm-charts/pull/591) | [@jmlrt](https://github.com/jmlrt)                     | Update doc and values.yaml for http.host issues |

### Metricbeat

| PR                                                      | Author                             | Title                                     |
|---------------------------------------------------------|------------------------------------|-------------------------------------------|
| [#567](https://github.com/elastic/helm-charts/pull/567) | [@jmlrt](https://github.com/jmlrt) | Metricbeat improvements                   |
| [#572](https://github.com/elastic/helm-charts/pull/572) | [@jmlrt](https://github.com/jmlrt) | Split values for daemonset and deployment |
| [#585](https://github.com/elastic/helm-charts/pull/585) | [@jmlrt](https://github.com/jmlrt) | Add host networking option                |

## 6.8.9 - 2020/05/13

* First 6.x release
* 6.8.9 as the default stack version
* See [7.7.0 CHANGELOG](#770---20200513) except GA support (charts are
  staying in Beta for 6.8).


## 7.6.2 - 2020/03/31

* 7.6.2 as the default stack version
* 6.8.8 as 6.x tested version
* Helm 2.16.5 support in [#537](https://github.com/elastic/helm-charts/pull/537) [@jmlrt](https://github.com/jmlrt)
* Drop GKE 1.13 tests in [#533](https://github.com/elastic/helm-charts/pull/533) [@jmlrt](https://github.com/jmlrt)
* Few dev environment tweaks in [#521](https://github.com/elastic/helm-charts/pull/521) [@Conky5](https://github.com/Conky5)
* Version bumping script enhancements in [#524](https://github.com/elastic/helm-charts/pull/524) [@Conky5](https://github.com/Conky5)
* Staging image testing in [#532](https://github.com/elastic/helm-charts/pull/532), [#544](https://github.com/elastic/helm-charts/pull/544) & [#545](https://github.com/elastic/helm-charts/pull/545) [@Conky5](https://github.com/Conky5)

### APM Server

| PR                                                      | Author                                 | Title                          |
|---------------------------------------------------------|----------------------------------------|--------------------------------|
| [#508](https://github.com/elastic/helm-charts/pull/508) | [@kawat55](https://github.com/kawat55) | Fix `fullnameOverride` setting |
| [#509](https://github.com/elastic/helm-charts/pull/509) | [@qqshfox](https://github.com/qqshfox) | Fix `apiVersion` of HPA        |

### Elasticsearch

| PR                                                      | Author                                               | Title                                                       |
|---------------------------------------------------------|------------------------------------------------------|-------------------------------------------------------------|
| [#485](https://github.com/elastic/helm-charts/pull/485) | [@mschmidt291](https://github.com/mschmidt291)       | Add possibility to define custom `readinessProbe`           |
| [#517](https://github.com/elastic/helm-charts/pull/517) | [@maksim-m](https://github.com/maksim-m)             | Add namespace parameter to the test function to `NOTES.txt` |
| [#539](https://github.com/elastic/helm-charts/pull/539) | [@adulescentulus](https://github.com/adulescentulus) | Add `loadBalancerIP` option to service                      |

### Filebeat

| PR                                                      | Author                                   | Title                                                       |
|---------------------------------------------------------|------------------------------------------|-------------------------------------------------------------|
| [#530](https://github.com/elastic/helm-charts/pull/530) | [@flaper87](https://github.com/flaper87) | Accept a string as `extraInitContainers` value for Filebeat |

### Kibana

| PR                                                      | Author                                   | Title                                                                                  |
|---------------------------------------------------------|------------------------------------------|----------------------------------------------------------------------------------------|
| [#493](https://github.com/elastic/helm-charts/pull/493) | [@jamoflaw](https://github.com/jamoflaw) | Fix Mismatch Between Service Selector and Pod Labels when using Helm Aliases in Kibana |
| [#540](https://github.com/elastic/helm-charts/pull/540) | [@jmlrt](https://github.com/jmlrt)       | Optimize Kibana memory usage                                                           |

### Logstash

| PR                                                      | Author                                               | Title                                          |
|---------------------------------------------------------|------------------------------------------------------|------------------------------------------------|
| [#500](https://github.com/elastic/helm-charts/pull/500) | [@zeph](https://github.com/zeph)                     | Add warn to override Logstash default pipeline |
| [#505](https://github.com/elastic/helm-charts/pull/505) | [@ChiefAlexander](https://github.com/ChiefAlexander) | Update Logstash chart to support custom ports  |

## 7.6.1 - 2020/03/04

* 7.6.1 as the default stack version

### APM Server

| PR                                                      | Author                                   | Title             |
|---------------------------------------------------------|------------------------------------------|-------------------|
| [#479](https://github.com/elastic/helm-charts/pull/479) | [@vhatsura](https://github.com/vhatsura) | Fix template name |

### Elasticsearch

| PR                                                      | Author                                 | Title                                   |
|---------------------------------------------------------|----------------------------------------|-----------------------------------------|
| [#483](https://github.com/elastic/helm-charts/pull/483) | [@ta-ando](https://github.com/ta-ando) | Ad support for loadBalancerSourceRanges |


## 7.6.0 - 2020/02/11

* 7.6.0 as the default stack version
* Freeze pip dependencies [#463](https://github.com/elastic/helm-charts/pull/463) [@morganchristiansson](https://github.com/morganchristiansson)
* Format python scripts with [Black](https://black.readthedocs.io/en/stable/) [#475](https://github.com/elastic/helm-charts/pull/475) & [#477](https://github.com/elastic/helm-charts/pull/477) [@jmlrt](https://github.com/jmlrt)

### APM Server

| PR                                                      | Author                                   | Title                                       |
|---------------------------------------------------------|------------------------------------------|---------------------------------------------|
| [#324](https://github.com/elastic/helm-charts/pull/324) | [@pbecotte](https://github.com/pbecotte) | Add apm-server helm chart                   |
| [#459](https://github.com/elastic/helm-charts/pull/459) | [@jmlrt](https://github.com/jmlrt)       | Add ci tests for apm-server chart           |
| [#473](https://github.com/elastic/helm-charts/pull/473) | [@jmlrt](https://github.com/jmlrt)       | Add extraContainers and extraInitContainers |

### Elasticsearch

| PR                                                      | Author                                       | Title                       |
|---------------------------------------------------------|----------------------------------------------|-----------------------------|
| [#455](https://github.com/elastic/helm-charts/pull/455) | [@sachinmsft](https://github.com/sachinmsft) | Fixing typo                 |
| [#458](https://github.com/elastic/helm-charts/pull/458) | [@jmlrt](https://github.com/jmlrt)           | Set cpu request = cpu limit |
| [#473](https://github.com/elastic/helm-charts/pull/473) | [@jmlrt](https://github.com/jmlrt)           | Add extraContainers         |

### Filebeat

| PR                                                      | Author                               | Title                   |
|---------------------------------------------------------|--------------------------------------|-------------------------|
| [#466](https://github.com/elastic/helm-charts/pull/466) | [@vasrem](https://github.com/vasrem) | Add extraInitContainers |
| [#473](https://github.com/elastic/helm-charts/pull/473) | [@jmlrt](https://github.com/jmlrt)   | Add extraContainers     |

### Kibana

| PR                                                      | Author                             | Title                                       |
|---------------------------------------------------------|------------------------------------|---------------------------------------------|
| [#473](https://github.com/elastic/helm-charts/pull/473) | [@jmlrt](https://github.com/jmlrt) | Add extraContainers and extraInitContainers |

### Logstash

| PR                                                      | Author                                                         | Title                           |
|---------------------------------------------------------|----------------------------------------------------------------|---------------------------------|
| [#457](https://github.com/elastic/helm-charts/pull/457) | [@morganchristiansson](https://github.com/morganchristiansson) | Add fullnameOverride setting    |
| [#473](https://github.com/elastic/helm-charts/pull/473) | [@jmlrt](https://github.com/jmlrt)                             | Remove duplicate line in README |

### Metricbeat

| PR                                                      | Author                             | Title                                       |
|---------------------------------------------------------|------------------------------------|---------------------------------------------|
| [#473](https://github.com/elastic/helm-charts/pull/473) | [@jmlrt](https://github.com/jmlrt) | Add extraContainers and extraInitContainers |


## 7.5.2 - 2020/01/21

* 7.5.2 as the default stack version
* Testing of GKE for 1.12 dropped and 1.15 added [#435](https://github.com/elastic/helm-charts/pull/435) [@jmlrt](https://github.com/jmlrt)
* Add [Probot](https://probot.github.io) config to manage stale issues / PR [#421](https://github.com/elastic/helm-charts/pull/421) [@jmlrt](https://github.com/jmlrt)
* Fix README docs links on [Helm Hub](https://hub.helm.sh) [#438](https://github.com/elastic/helm-charts/pull/438) [@jmlrt](https://github.com/jmlrt)

### Elasticsearch

| PR                                                      | Author                                           | Title                                                           |
|---------------------------------------------------------|--------------------------------------------------|-----------------------------------------------------------------|
| [#382](https://github.com/elastic/helm-charts/pull/382) | [@jaumann](https://github.com/jaumann)           | Allow for name overrides of resources                           |
| [#433](https://github.com/elastic/helm-charts/pull/433) | [@jmlrt](https://github.com/jmlrt)               | Add example for [Microk8s](https://microk8s.io/)                |
| [#428](https://github.com/elastic/helm-charts/pull/428) | [@mmisztal1980](https://github.com/mmisztal1980) | Remove duplicate label                                          |
| [#434](https://github.com/elastic/helm-charts/pull/434) | [@jmlrt](https://github.com/jmlrt)               | Add workaround to fix [kind])https://kind.sigs.k8s.io/) example |
| [#444](https://github.com/elastic/helm-charts/pull/444) | [@naseemkullah](https://github.com/naseemkullah) | Add commented out example of a useful post start hook           |

### Filebeat

| PR                                                      | Author                                         | Title                                                                 |
|---------------------------------------------------------|------------------------------------------------|-----------------------------------------------------------------------|
| [#415](https://github.com/elastic/helm-charts/pull/415) | [@jmlrt](https://github.com/jmlrt)             | Add custom labels to pods                                             |
| [#369](https://github.com/elastic/helm-charts/pull/369) | [@jmymy](https://github.com/jmymy)             | Add support for `envfrom`                                             |
| [#420](https://github.com/elastic/helm-charts/pull/420) | [@jmlrt](https://github.com/jmlrt)             | Override probes commands                                              |
| [#430](https://github.com/elastic/helm-charts/pull/430) | [@krichter722](https://github.com/krichter722) | Fix default value of `extraVolumeMounts` and `extraVolumes` in README |

### Kibana

| PR                                                      | Author                                           | Title                                           |
|---------------------------------------------------------|--------------------------------------------------|-------------------------------------------------|
| [#415](https://github.com/elastic/helm-charts/pull/415) | [@jmlrt](https://github.com/jmlrt)               | Add custom labels to pods                       |
| [#422](https://github.com/elastic/helm-charts/pull/422) | [@victorsalaun](https://github.com/victorsalaun) | Remove useless `maxUnavailable` in Kibana chart |
| [#408](https://github.com/elastic/helm-charts/pull/408) | [@ichylinux](https://github.com/ichylinux)       | Add support for `loadBalancerSourceRanges`      |
| [#419](https://github.com/elastic/helm-charts/pull/419) | [@jmlrt](https://github.com/jmlrt)               | Add doc for plugin install                      |

### Logstash

| PR                                                      | Author                             | Title                     |
|---------------------------------------------------------|------------------------------------|---------------------------|
| [#415](https://github.com/elastic/helm-charts/pull/415) | [@jmlrt](https://github.com/jmlrt) | Add custom labels to pods |

### Metricbeat

| PR                                                      | Author                                   | Title                                                         |
|---------------------------------------------------------|------------------------------------------|---------------------------------------------------------------|
| [#415](https://github.com/elastic/helm-charts/pull/415) | [@jmlrt](https://github.com/jmlrt)       | Add custom labels to pods                                     |
| [#369](https://github.com/elastic/helm-charts/pull/369) | [@jmymy](https://github.com/jmymy)       | Add support for `envfrom`                                     |
| [#420](https://github.com/elastic/helm-charts/pull/420) | [@jmlrt](https://github.com/jmlrt)       | Override probes commands                                      |
| [#425](https://github.com/elastic/helm-charts/pull/425) | [@pbecotte](https://github.com/pbecotte) | Update `hostfs` to be a CLI option instead of a config option |
| [#436](https://github.com/elastic/helm-charts/pull/436) | [@gadiener](https://github.com/gadiener) | Add `priorityClassName` config                                |


## 7.5.1 - 2019/12/18

* 7.5.1 as the default stack version
* 6.8.6 as 6.x tested version
* Add a notice that Helm v3 is not supported in [#400](https://github.com/elastic/helm-charts/pull/400) [@jmlrt](https://github.com/jmlrt)
* Prefixed helper functions with chart name in [#407](https://github.com/elastic/helm-charts/pull/407) [bpdunni](https://github.com/bpdunni)
* Use details tag around code backticks for 'helm get' output in issue template in [#413](https://github.com/elastic/helm-charts/pull/413) [krichter722](https://github.com/krichter722)

### Filebeat

| PR                                                      | Author                                   | Title                                                 |
|---------------------------------------------------------|------------------------------------------|-------------------------------------------------------|
| [#403](https://github.com/elastic/helm-charts/pull/403) | [@ChrsMark](https://github.com/ChrsMark) | Remove in_cluster config from add_kubernetes_metadata |

### Kibana

| PR                                                      | Author                                               | Title                                |
|---------------------------------------------------------|------------------------------------------------------|--------------------------------------|
| [#411](https://github.com/elastic/helm-charts/pull/411) | [@usamaahmadkhan](https://github.com/usamaahmadkhan) | Enable labels to be added to service |

### Metricbeat

| PR                                                      | Author                             | Title                                                 |
|---------------------------------------------------------|------------------------------------|-------------------------------------------------------|
| [#397](https://github.com/elastic/helm-charts/pull/397) | [@jmlrt](https://github.com/jmlrt) | Add a notice about kube-state-metrics breaking change |


## 7.5.0 - 2019/12/02

* 7.5.0 as the default stack version
* 6.8.5 as 6.x tested version in [#386](https://github.com/elastic/helm-charts/pull/386) [@jmlrt](https://github.com/jmlrt)
* Helm 2.16.1 support in [#366](https://github.com/elastic/helm-charts/pull/366) [@jmlrt](https://github.com/jmlrt)
* Add Beats icons to Helm repository in [#345](https://github.com/elastic/helm-charts/pull/345) [@jmlrt](https://github.com/jmlrt)
* Make helm-tester docker image build less verbose in [#346](https://github.com/elastic/helm-charts/pull/346) [@jmlrt](https://github.com/jmlrt)
* Update install doc in [#364](https://github.com/elastic/helm-charts/pull/364) [@jmlrt](https://github.com/jmlrt)
* Add security notice to github issue template in [#368](https://github.com/elastic/helm-charts/pull/368) [@jmlrt](https://github.com/jmlrt)

### Elasticsearch

| PR                                                      | Author                                               | Title                                                                        |
|---------------------------------------------------------|------------------------------------------------------|------------------------------------------------------------------------------|
| [#344](https://github.com/elastic/helm-charts/pull/344) | [@usamaahmadkhan](https://github.com/usamaahmadkhan) | Add support for labels on services                                           |
| [#350](https://github.com/elastic/helm-charts/pull/350) | [@crgstar](https://github.com/crgstar)               | Use same imagePullPolicy in initContainer                                    |
| [#380](https://github.com/elastic/helm-charts/pull/380) | [@fatmcgav](https://github.com/fatmcgav)             | Tweak the 'readinessProbe' command to verify that master nodes are available |
| [#383](https://github.com/elastic/helm-charts/pull/383) | [@tanakapayam](https://github.com/tanakapayam)       | Apply labels to all pods                                                     |

### Filebeat

| PR                                                      | Author                                           | Title                                                                     |
|---------------------------------------------------------|--------------------------------------------------|---------------------------------------------------------------------------|
| [#330](https://github.com/elastic/helm-charts/pull/330) | [@tusciucalecs](https://github.com/tusciucalecs) | Support fullnameOverride                                                  |
| [#321](https://github.com/elastic/helm-charts/pull/321) | [@pbecotte](https://github.com/pbecotte)         | Use host networking so that the stats have the correct node information   |
| [#322](https://github.com/elastic/helm-charts/pull/322) | [@pbecotte](https://github.com/pbecotte)         | Use a list for extra volume mounts to match the comments and other values |

### Kibana

| PR                                                      | Author                                           | Title                    |
|---------------------------------------------------------|--------------------------------------------------|--------------------------|
| [#330](https://github.com/elastic/helm-charts/pull/330) | [@tusciucalecs](https://github.com/tusciucalecs) | Support fullnameOverride |

### Logstash

| PR                                                      | Author                             | Title                                         |
|---------------------------------------------------------|------------------------------------|-----------------------------------------------|
| [#333](https://github.com/elastic/helm-charts/pull/333) | [@jmlrt](https://github.com/jmlrt) | First version of logstash helm chart          |
| [#347](https://github.com/elastic/helm-charts/pull/347) | [@jmlrt](https://github.com/jmlrt) | Remove goss port test                         |
| [#367](https://github.com/elastic/helm-charts/pull/367) | [@jmlrt](https://github.com/jmlrt) | Update default values for memory requirements |

### Metricbeat

| PR                                                      | Author                                           | Title                                                                                     |
|---------------------------------------------------------|--------------------------------------------------|-------------------------------------------------------------------------------------------|
| [#352](https://github.com/elastic/helm-charts/pull/352) | [@masterkain](https://github.com/masterkain)     | Bump kube-state-metrics to latest chart and app version                                   |
| [#330](https://github.com/elastic/helm-charts/pull/330) | [@tusciucalecs](https://github.com/tusciucalecs) | Support fullnameOverride                                                                  |
| [#314](https://github.com/elastic/helm-charts/pull/314) | [@pbecotte](https://github.com/pbecotte)         | Add a couple extra mounts to pick up all the metrics from the host nodes on Digital Ocean |


## 7.4.1 - 2019/10/23

* 7.4.1 as the default stack version
* 6.8.4 as 6.x tested version
* Helm 2.15.1 support in [#338](https://github.com/elastic/helm-charts/pull/338) [@jmlrt](https://github.com/jmlrt)

### Elasticsearch

| PR                                                      | Author                                     | Title                                        |
|---------------------------------------------------------|--------------------------------------------|----------------------------------------------|
| [#313](https://github.com/elastic/helm-charts/pull/313) | [@Crazybus](https://github.com/Crazybus)   | Add logging when adding password to keystore |
| [#301](https://github.com/elastic/helm-charts/pull/301) | [@ravishivt](https://github.com/ravishivt) | Fix bug in keystore initContainer            |
| [#274](https://github.com/elastic/helm-charts/pull/274) | [@salaboy](https://github.com/salaboy)     | Add Example for Kubernetes KIND              |
| [#335](https://github.com/elastic/helm-charts/pull/335) | [@jmlrt](https://github.com/jmlrt)         | Fix deprecated note                          |
| [#337](https://github.com/elastic/helm-charts/pull/337) | [@jmlrt](https://github.com/jmlrt)         | Remove unused default value                  |

### Kibana

| PR                                                      | Author                             | Title                           |
|---------------------------------------------------------|------------------------------------|---------------------------------|
| [#326](https://github.com/elastic/helm-charts/pull/326) | [@jmlrt](https://github.com/jmlrt) | Remove unused antiAffinity keys |

### Metricbeat

| PR                                                      | Author                             | Title                                                  |
|---------------------------------------------------------|------------------------------------|--------------------------------------------------------|
| [#339](https://github.com/elastic/helm-charts/pull/339) | [@jmlrt](https://github.com/jmlrt) | Allow adding additional labels to Metricbeat Daemonset |


## 7.4.0 - 2019/10/01

* 7.4.0 as the default stack version
* Helm-tester Docker image migrated to Python 3 in [#297](https://github.com/elastic/helm-charts/pull/297) [@jmlrt](https://github.com/jmlrt)
* Helm-tester Python dependencies freeze in [#309](https://github.com/elastic/helm-charts/pull/309) [@jmlrt](https://github.com/jmlrt)

### Elasticsearch

| PR                                                      | Author                                     | Title                                                                  |
|---------------------------------------------------------|--------------------------------------------|------------------------------------------------------------------------|
| [#296](https://github.com/elastic/helm-charts/pull/296) | [@jmlrt](https://github.com/jmlrt)         | Fix "; \" when there is no additional command in the Makefiles         |
| [#298](https://github.com/elastic/helm-charts/pull/298) | [@floretan](https://github.com/floretan)   | Make it possible to override the endpoint template.                    |
| [#263](https://github.com/elastic/helm-charts/pull/263) | [@Crazybus](https://github.com/Crazybus)   | Add working examples for running Elasticsearch and Kibana on OpenShift |
| [#301](https://github.com/elastic/helm-charts/pull/301) | [@ravishivt](https://github.com/ravishivt) | Fix bug in keystore initContainer                                      |

### Kibana

| PR                                                      | Author                                           | Title                                                                               |
|---------------------------------------------------------|--------------------------------------------------|-------------------------------------------------------------------------------------|
| [#295](https://github.com/elastic/helm-charts/pull/295) | [@karlbohlmark](https://github.com/karlbohlmark) | Allow configuring lifecycle events                                                  |
| [#263](https://github.com/elastic/helm-charts/pull/263) | [@Crazybus](https://github.com/Crazybus)         | Add working examples for running Elasticsearch and Kibana on OpenShift              |
| [#303](https://github.com/elastic/helm-charts/pull/303) | [@code-chris](https://github.com/code-chris)     | Add compatibility for k8s 1.16 and change min k8s version due to ingress apiVersion |


### Filebeat

| PR                                                      | Author                                       | Title                                              |
|---------------------------------------------------------|----------------------------------------------|----------------------------------------------------|
| [#304](https://github.com/elastic/helm-charts/pull/304) | [@code-chris](https://github.com/code-chris) | Change min k8s version due to daemonset apiVersion |

### Metricbeat

| PR                                                      | Author                                       | Title                                          |
|---------------------------------------------------------|----------------------------------------------|------------------------------------------------|
| [#310](https://github.com/elastic/helm-charts/pull/310) | [@Crazybus](https://github.com/Crazybus)     | Make cluster role rules configurable           |
| [#305](https://github.com/elastic/helm-charts/pull/305) | [@code-chris](https://github.com/code-chris) | Change min k8s version due to used apiVersions |


## 7.3.2 - 2019/09/19

* 7.3.2 as the default stack version
* Testing of GKE for 1.11 dropped and 1.14 added [#287](https://github.com/elastic/helm-charts/pull/287)
* Make helper scripts python3 compatible [#255](https://github.com/elastic/helm-charts/pull/255) [@cclauss](https://github.com/cclauss)

### Elasticsearch

| PR                                                      | Author                                             | Title                                                                       |
|---------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------------|
| [#238](https://github.com/elastic/helm-charts/pull/238) | [@Crazybus](https://github.com/Crazybus)           | Update documentation and defaults for tmpl values                           |
| [#245](https://github.com/elastic/helm-charts/pull/245) | [@skitle](https://github.com/skitle)               | Fixed indent on elasticsearch extraVolumes tpl. Was causing parsing errors. |
| [#250](https://github.com/elastic/helm-charts/pull/250) | [@tanordheim](https://github.com/tanordheim)       | Update priorityClassName default values in READMEs                          |
| [#261](https://github.com/elastic/helm-charts/pull/261) | [@Crazybus](https://github.com/Crazybus)           | Bump google terraform provider to the latest                                |
| [#154](https://github.com/elastic/helm-charts/pull/154) | [@Crazybus](https://github.com/Crazybus)           | Keystore integration                                                        |
| [#290](https://github.com/elastic/helm-charts/pull/290) | [@Crazybus](https://github.com/Crazybus)           | Drop version from chart label in service                                    |
| [#270](https://github.com/elastic/helm-charts/pull/270) | [@GreenKnight15](https://github.com/GreenKnight15) | ES Variable Port Name                                                       |
| [#259](https://github.com/elastic/helm-charts/pull/259) | [@Crazybus](https://github.com/Crazybus)           | Set default runAsUser for pod security context                              |
| [#265](https://github.com/elastic/helm-charts/pull/265) | [@maximelenair](https://github.com/maximelenair)   | Hardening of the pod permissions.                                           |

### Kibana

| PR                                                      | Author                                       | Title                                              |
|---------------------------------------------------------|----------------------------------------------|----------------------------------------------------|
| [#250](https://github.com/elastic/helm-charts/pull/250) | [@tanordheim](https://github.com/tanordheim) | Update priorityClassName default values in READMEs |
| [#268](https://github.com/elastic/helm-charts/pull/268) | [@accek](https://github.com/accek)           | fixed bogus request of 500 millibytes mem          |
| [#272](https://github.com/elastic/helm-charts/pull/272) | [@rccrdpccl](https://github.com/rccrdpccl)   | use same env variable as application               |
| [#291](https://github.com/elastic/helm-charts/pull/291) | [@Crazybus](https://github.com/Crazybus)     | Explicitly test for a 200 for readinessProbe       |

### Filebeat

| PR                                                      | Author                                       | Title                                              |
|---------------------------------------------------------|----------------------------------------------|----------------------------------------------------|
| [#243](https://github.com/elastic/helm-charts/pull/243) | [@Crazybus](https://github.com/Crazybus)     | Add configurable nodeSelector and affinity spec    |
| [#248](https://github.com/elastic/helm-charts/pull/248) | [@tanordheim](https://github.com/tanordheim) | Add priorityClassName to filebeat chart            |
| [#250](https://github.com/elastic/helm-charts/pull/250) | [@tanordheim](https://github.com/tanordheim) | Update priorityClassName default values in READMEs |

### Metricbeat

| PR                                                      | Author                                   | Title                                                |
|---------------------------------------------------------|------------------------------------------|------------------------------------------------------|
| [#243](https://github.com/elastic/helm-charts/pull/243) | [@Crazybus](https://github.com/Crazybus) | Add configurable nodeSelector and affinity spec      |
| [#251](https://github.com/elastic/helm-charts/pull/251) | [@Crazybus](https://github.com/Crazybus) | Fix default configuration for kubernetes module      |
| [#289](https://github.com/elastic/helm-charts/pull/289) | [@Crazybus](https://github.com/Crazybus) | Remove default kube static metrics host to avoid co… |
| [#254](https://github.com/elastic/helm-charts/pull/254) | [@Azuka](https://github.com/Azuka)       | Enable events access to cluster role                 |


## 7.3.0 - 2019/07/31

* 7.3.0 as the default stack version

### Elasticsearch
| PR                                                      | Author                                                     | Title                                                                     |
|---------------------------------------------------------|------------------------------------------------------------|---------------------------------------------------------------------------|
| [#226](https://github.com/elastic/helm-charts/pull/226) | [@MichaelMarieJulie](https://github.com/MichaelMarieJulie) | Add configurable pods labels                                              |
| [#237](https://github.com/elastic/helm-charts/pull/237) | [@MichaelSp](https://github.com/MichaelSp)                 | Add back `service.alpha.kubernetes.io/tolerate-unready-endpoints: "true"` |

### Kibana
| PR                                                      | Author                                     | Title                               |
|---------------------------------------------------------|--------------------------------------------|-------------------------------------|
| [#225](https://github.com/elastic/helm-charts/pull/225) | [@plumcraft](https://github.com/plumcraft) | Add configurable pod labels         |
| [#230](https://github.com/elastic/helm-charts/pull/230) | [@Crazybus](https://github.com/Crazybus)   | Add subPath support to secretMounts |


## 7.2.1-0 - 2019/07/18

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


## 7.1.1 - 2019/06/07

* 7.1.1 as the default stack version
* Helm 2.14.0 as the tested version. Helm 2.14.0 has some extra validation built in which caused an issue with an [invalid field in the filebeat chart](https://github.com/elastic/helm-charts/issues/136).

### Elasticsearch

* [#146](https://github.com/elastic/helm-charts/pull/146) - @Crazybus - Add instructions for how to enable snapshots

### Kibana

* [#151](https://github.com/elastic/helm-charts/pull/151) - @natebwangsut - Added an option to add annotations(s) to service resource

### Filebeat

* [#140](https://github.com/elastic/helm-charts/pull/140) - @Crazybus - Remove fsGroup from container level security context


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


## 7.0.1-alpha1 - 2019/05/01

* 7.0.1 as the default stack version
* [Contributing guide](https://github.com/elastic/helm-charts/blob/main/CONTRIBUTING.md), [release process](https://github.com/elastic/helm-charts/blob/main/helpers/release.md), [changelog](https://github.com/elastic/helm-charts/blob/main/CHANGELOG.md) and [issue templates](https://github.com/elastic/helm-charts/tree/main/.github/ISSUE_TEMPLATE) added in [#111](https://github.com/elastic/helm-charts/pull/111)
* Automated testing for Kubernetes 1.10 dropped because it is no longer available in GKE
* Helm client version bumped to 2.13.1

### Elasticsearch

* [#100](https://github.com/elastic/helm-charts/pull/100) - @kuisathaverat - Remove deprecated zen ping unicast hosts setting
* [#114](https://github.com/elastic/helm-charts/pull/114) - @Crazybus - Make persistent volumes optional
* [#115](https://github.com/elastic/helm-charts/pull/115) - @Crazybus - Added an integration test for upgrading from the previous release and testing rolling upgrades

### Kibana

* [#107](https://github.com/elastic/helm-charts/pull/107) - @Crazybus - Make the health check path configurable to support webroots and other customizations.


## 7.0.0-alpha1 - 2019/04/17

* [#96](https://github.com/elastic/helm-charts/pull/96) - @Crazybus - 7.0.0 as the default stack version

### Elasticsearch

* [#94](https://github.com/elastic/helm-charts/pull/94) - @kimxogus - Remove hardcoded storageClassName
