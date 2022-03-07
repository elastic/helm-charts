import os
import sys
import base64

sys.path.insert(1, os.path.join(sys.path[0], "../../helpers"))
from helpers import helm_template

project = "metricbeat"
name = "release-name-" + project
kube_state_metric_name = "release-name-kube-state-metrics"


def test_defaults():
    config = """
    """

    r = helm_template(config)

    assert name in r["daemonset"]
    assert name + "-metrics" in r["deployment"]

    assert kube_state_metric_name in r["deployment"]
    assert (
        r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["containers"][0][
            "env"
        ][1]["value"]
        == "$(RELEASE_NAME_KUBE_STATE_METRICS_SERVICE_HOST):$(RELEASE_NAME_KUBE_STATE_METRICS_SERVICE_PORT_HTTP)"
    )

    c = r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0]
    assert c["name"] == project
    assert c["image"].startswith("docker.elastic.co/beats/" + project + ":")

    assert c["env"][0]["name"] == "POD_NAMESPACE"
    assert c["env"][0]["valueFrom"]["fieldRef"]["fieldPath"] == "metadata.namespace"

    assert "curl --fail 127.0.0.1:5066" in c["livenessProbe"]["exec"]["command"][-1]

    assert "metricbeat test output" in c["readinessProbe"]["exec"]["command"][-1]

    assert r["daemonset"][name]["spec"]["template"]["spec"]["tolerations"] == []

    assert "hostNetwork" not in r["daemonset"][name]["spec"]["template"]["spec"]
    assert "dnsPolicy" not in r["daemonset"][name]["spec"]["template"]["spec"]
    assert (
        "hostNetwork"
        not in r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]
    )
    assert (
        "dnsPolicy"
        not in r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]
    )

    assert (
        r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["tolerations"]
        == []
    )

    assert (
        r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0][
            "securityContext"
        ]["runAsUser"]
        == 0
    )
    assert (
        r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0][
            "securityContext"
        ]["privileged"]
        == False
    )
    assert (
        r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["containers"][0][
            "securityContext"
        ]["runAsUser"]
        == 0
    )
    assert (
        r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["containers"][0][
            "securityContext"
        ]["privileged"]
        == False
    )

    # Empty customizable defaults
    assert "imagePullSecrets" not in r["daemonset"][name]["spec"]["template"]["spec"]

    assert r["daemonset"][name]["spec"]["updateStrategy"]["type"] == "RollingUpdate"

    assert (
        r["daemonset"][name]["spec"]["template"]["spec"]["serviceAccountName"] == name
    )

    cfg = r["configmap"]

    assert name + "-config" not in cfg
    assert name + "-daemonset-config" in cfg
    assert name + "-deployment-config" in cfg

    assert "metricbeat.yml" in cfg[name + "-daemonset-config"]["data"]
    assert "metricbeat.yml" in cfg[name + "-deployment-config"]["data"]

    assert "module: system" in cfg[name + "-daemonset-config"]["data"]["metricbeat.yml"]
    assert (
        "module: system"
        not in cfg[name + "-deployment-config"]["data"]["metricbeat.yml"]
    )
    assert "state_pod" not in cfg[name + "-daemonset-config"]["data"]["metricbeat.yml"]
    assert "state_pod" in cfg[name + "-deployment-config"]["data"]["metricbeat.yml"]

    daemonset = r["daemonset"][name]["spec"]["template"]["spec"]

    assert {
        "configMap": {"name": name + "-config", "defaultMode": 0o600},
        "name": project + "-config",
    } not in daemonset["volumes"]
    assert {
        "configMap": {"name": name + "-daemonset-config", "defaultMode": 0o600},
        "name": project + "-config",
    } in daemonset["volumes"]

    assert {
        "name": "data",
        "hostPath": {
            "path": "/var/lib/" + name + "-default-data",
            "type": "DirectoryOrCreate",
        },
    } in daemonset["volumes"]

    assert {
        "mountPath": "/usr/share/metricbeat/metricbeat.yml",
        "name": project + "-config",
        "subPath": "metricbeat.yml",
        "readOnly": True,
    } in daemonset["containers"][0]["volumeMounts"]

    deployment = r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]

    assert {
        "configMap": {"name": name + "-config", "defaultMode": 0o600},
        "name": project + "-config",
    } not in deployment["volumes"]
    assert {
        "configMap": {"name": name + "-deployment-config", "defaultMode": 0o600},
        "name": project + "-config",
    } in deployment["volumes"]

    assert {
        "mountPath": "/usr/share/metricbeat/metricbeat.yml",
        "name": project + "-config",
        "subPath": "metricbeat.yml",
        "readOnly": True,
    } in deployment["containers"][0]["volumeMounts"]

    assert daemonset["containers"][0]["resources"] == {
        "requests": {"cpu": "100m", "memory": "100Mi"},
        "limits": {"cpu": "1000m", "memory": "200Mi"},
    }
    assert deployment["containers"][0]["resources"] == {
        "requests": {"cpu": "100m", "memory": "100Mi"},
        "limits": {"cpu": "1000m", "memory": "200Mi"},
    }

    assert "hostAliases" not in r["daemonset"][name]["spec"]["template"]["spec"]
    assert (
        "hostAliases"
        not in r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]
    )


def test_adding_a_extra_container():
    config = """
extraContainers: |
  - name: do-something
    image: busybox
    command: ['do', 'something']
"""
    r = helm_template(config)
    extraContainerDaemonset = r["daemonset"][name]["spec"]["template"]["spec"][
        "containers"
    ]
    assert {
        "name": "do-something",
        "image": "busybox",
        "command": ["do", "something"],
    } in extraContainerDaemonset
    deployment_name = name + "-metrics"
    extraContainerDeployment = r["deployment"][deployment_name]["spec"]["template"][
        "spec"
    ]["containers"]
    assert {
        "name": "do-something",
        "image": "busybox",
        "command": ["do", "something"],
    } in extraContainerDeployment


def test_adding_a_extra_init_container():
    config = """
extraInitContainers: |
  - name: do-something
    image: busybox
    command: ['do', 'something']
"""
    r = helm_template(config)
    extraInitContainerDaemonset = r["daemonset"][name]["spec"]["template"]["spec"][
        "initContainers"
    ]
    assert {
        "name": "do-something",
        "image": "busybox",
        "command": ["do", "something"],
    } in extraInitContainerDaemonset
    deployment_name = name + "-metrics"
    extraInitContainerDeployment = r["deployment"][deployment_name]["spec"]["template"][
        "spec"
    ]["initContainers"]
    assert {
        "name": "do-something",
        "image": "busybox",
        "command": ["do", "something"],
    } in extraInitContainerDeployment


def test_adding_envs():
    config = """
daemonset:
  extraEnvs:
  - name: LOG_LEVEL
    value: DEBUG
"""
    r = helm_template(config)
    assert {"name": "LOG_LEVEL", "value": "DEBUG"} in r["daemonset"][name]["spec"][
        "template"
    ]["spec"]["containers"][0]["env"]
    assert {"name": "LOG_LEVEL", "value": "DEBUG"} not in r["deployment"][
        name + "-metrics"
    ]["spec"]["template"]["spec"]["containers"][0]["env"]

    config = """
deployment:
  extraEnvs:
  - name: LOG_LEVEL
    value: DEBUG
"""
    r = helm_template(config)
    assert {"name": "LOG_LEVEL", "value": "DEBUG"} in r["deployment"][
        name + "-metrics"
    ]["spec"]["template"]["spec"]["containers"][0]["env"]
    assert {"name": "LOG_LEVEL", "value": "DEBUG"} not in r["daemonset"][name]["spec"][
        "template"
    ]["spec"]["containers"][0]["env"]


def test_adding_deprecated_envs():
    config = """
extraEnvs:
- name: LOG_LEVEL
  value: DEBUG
"""
    r = helm_template(config)
    assert {"name": "LOG_LEVEL", "value": "DEBUG"} in r["daemonset"][name]["spec"][
        "template"
    ]["spec"]["containers"][0]["env"]
    assert {"name": "LOG_LEVEL", "value": "DEBUG"} in r["deployment"][
        name + "-metrics"
    ]["spec"]["template"]["spec"]["containers"][0]["env"]


def test_adding_image_pull_secrets():
    config = """
imagePullSecrets:
  - name: test-registry
"""
    r = helm_template(config)
    assert (
        r["daemonset"][name]["spec"]["template"]["spec"]["imagePullSecrets"][0]["name"]
        == "test-registry"
    )


def test_adding_host_networking():
    config = """
daemonset:
  hostNetworking: true
"""
    r = helm_template(config)
    assert r["daemonset"][name]["spec"]["template"]["spec"]["hostNetwork"] is True
    assert (
        r["daemonset"][name]["spec"]["template"]["spec"]["dnsPolicy"]
        == "ClusterFirstWithHostNet"
    )
    assert (
        "hostNetwork"
        not in r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]
    )
    assert (
        "dnsPolicy"
        not in r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]
    )


def test_adding_tolerations():
    config = """
daemonset:
  tolerations:
  - key: "key1"
    operator: "Equal"
    value: "value1"
    effect: "NoExecute"
    tolerationSeconds: 3600
"""
    r = helm_template(config)
    assert (
        r["daemonset"][name]["spec"]["template"]["spec"]["tolerations"][0]["key"]
        == "key1"
    )
    assert (
        r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["tolerations"]
        == []
    )

    config = """
deployment:
  tolerations:
  - key: "key1"
    operator: "Equal"
    value: "value1"
    effect: "NoExecute"
    tolerationSeconds: 3600
"""
    r = helm_template(config)
    assert (
        r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["tolerations"][
            0
        ]["key"]
        == "key1"
    )
    assert r["daemonset"][name]["spec"]["template"]["spec"]["tolerations"] == []


def test_adding_deprecated_tolerations():
    config = """
tolerations:
- key: "key1"
  operator: "Equal"
  value: "value1"
  effect: "NoExecute"
  tolerationSeconds: 3600
"""
    r = helm_template(config)
    assert (
        r["daemonset"][name]["spec"]["template"]["spec"]["tolerations"][0]["key"]
        == "key1"
    )
    assert (
        r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["tolerations"][
            0
        ]["key"]
        == "key1"
    )


def test_override_the_default_update_strategy():
    config = """
updateStrategy: OnDelete
"""

    r = helm_template(config)
    assert r["daemonset"][name]["spec"]["updateStrategy"]["type"] == "OnDelete"


def test_setting_a_custom_service_account():
    config = """
serviceAccount: notdefault
"""
    r = helm_template(config)
    assert (
        r["daemonset"][name]["spec"]["template"]["spec"]["serviceAccountName"]
        == "notdefault"
    )


def test_self_managing_rbac_resources():
    config = """
managedServiceAccount: false
"""
    r = helm_template(config)
    assert name not in r["serviceaccount"]
    assert name not in r["clusterrole"]
    assert name not in r["clusterrolebinding"]


def test_setting_pod_security_context():
    config = """
daemonset:
  securityContext:
    runAsUser: 1001
    privileged: false
"""
    r = helm_template(config)
    assert (
        r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0][
            "securityContext"
        ]["runAsUser"]
        == 1001
    )
    assert (
        r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0][
            "securityContext"
        ]["privileged"]
        == False
    )
    assert (
        r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["containers"][0][
            "securityContext"
        ]["runAsUser"]
        == 0
    )
    assert (
        r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["containers"][0][
            "securityContext"
        ]["privileged"]
        == False
    )

    config = """
deployment:
  securityContext:
    runAsUser: 1001
    privileged: false
"""
    r = helm_template(config)
    assert (
        r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["containers"][0][
            "securityContext"
        ]["runAsUser"]
        == 1001
    )
    assert (
        r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["containers"][0][
            "securityContext"
        ]["privileged"]
        == False
    )
    assert (
        r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0][
            "securityContext"
        ]["runAsUser"]
        == False
    )
    assert (
        r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0][
            "securityContext"
        ]["privileged"]
        == False
    )


def test_setting_deprecated_pod_security_context():
    config = """
podSecurityContext:
  runAsUser: 1001
  privileged: false
"""
    r = helm_template(config)
    assert (
        r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0][
            "securityContext"
        ]["runAsUser"]
        == 1001
    )
    assert (
        r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0][
            "securityContext"
        ]["privileged"]
        == False
    )
    assert (
        r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["containers"][0][
            "securityContext"
        ]["runAsUser"]
        == 1001
    )
    assert (
        r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["containers"][0][
            "securityContext"
        ]["privileged"]
        == False
    )


def test_adding_in_metricbeat_config():
    config = """
daemonset:
  metricbeatConfig:
    metricbeat.yml: |
      key: daemonset
    daemonset-config.yml: |
      hello = daemonset

deployment:
  metricbeatConfig:
    metricbeat.yml: |
      key: deployment
    deployment-config.yml: |
      hello = deployment
"""
    r = helm_template(config)
    cfg = r["configmap"]

    assert "metricbeat.yml" in cfg[name + "-daemonset-config"]["data"]
    assert "daemonset-config.yml" in cfg[name + "-daemonset-config"]["data"]
    assert "deployment-config.yml" not in cfg[name + "-daemonset-config"]["data"]
    assert "metricbeat.yml" in cfg[name + "-deployment-config"]["data"]
    assert "deployment-config.yml" in cfg[name + "-deployment-config"]["data"]
    assert "daemonset-config.yml" not in cfg[name + "-deployment-config"]["data"]

    assert "key: daemonset" in cfg[name + "-daemonset-config"]["data"]["metricbeat.yml"]
    assert (
        "key: deployment" in cfg[name + "-deployment-config"]["data"]["metricbeat.yml"]
    )

    assert (
        "hello = daemonset"
        in cfg[name + "-daemonset-config"]["data"]["daemonset-config.yml"]
    )
    assert (
        "hello = deployment"
        in cfg[name + "-deployment-config"]["data"]["deployment-config.yml"]
    )

    daemonset = r["daemonset"][name]["spec"]["template"]["spec"]
    assert {
        "mountPath": "/usr/share/metricbeat/daemonset-config.yml",
        "name": project + "-config",
        "subPath": "daemonset-config.yml",
        "readOnly": True,
    } in daemonset["containers"][0]["volumeMounts"]

    deployment = r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]
    assert {
        "mountPath": "/usr/share/metricbeat/deployment-config.yml",
        "name": project + "-config",
        "subPath": "deployment-config.yml",
        "readOnly": True,
    } in deployment["containers"][0]["volumeMounts"]


def test_adding_in_deprecated_metricbeat_config():
    config = """
metricbeatConfig:
  metricbeat.yml: |
    key:
      nestedkey: value
    dot.notation: test

  kube-state-metrics-metricbeat.yml: |
    hello = world
"""
    r = helm_template(config)
    c = r["configmap"][name + "-config"]["data"]

    assert "metricbeat.yml" in c
    assert "kube-state-metrics-metricbeat.yml" in c

    assert "nestedkey: value" in c["metricbeat.yml"]
    assert "dot.notation: test" in c["metricbeat.yml"]

    assert "hello = world" in c["kube-state-metrics-metricbeat.yml"]

    daemonset = r["daemonset"][name]["spec"]["template"]["spec"]

    assert {
        "configMap": {"name": name + "-config", "defaultMode": 0o600},
        "name": project + "-config",
    } in daemonset["volumes"]
    assert {
        "mountPath": "/usr/share/metricbeat/metricbeat.yml",
        "name": project + "-config",
        "subPath": "metricbeat.yml",
        "readOnly": True,
    } in daemonset["containers"][0]["volumeMounts"]
    assert {
        "mountPath": "/usr/share/metricbeat/kube-state-metrics-metricbeat.yml",
        "name": project + "-config",
        "subPath": "kube-state-metrics-metricbeat.yml",
        "readOnly": True,
    } in daemonset["containers"][0]["volumeMounts"]

    assert (
        "configChecksum"
        in r["daemonset"][name]["spec"]["template"]["metadata"]["annotations"]
    )

    deployment = r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]

    assert {
        "configMap": {"name": name + "-config", "defaultMode": 0o600},
        "name": project + "-config",
    } in deployment["volumes"]
    assert {
        "mountPath": "/usr/share/metricbeat/metricbeat.yml",
        "name": project + "-config",
        "subPath": "metricbeat.yml",
        "readOnly": True,
    } in deployment["containers"][0]["volumeMounts"]
    assert {
        "mountPath": "/usr/share/metricbeat/kube-state-metrics-metricbeat.yml",
        "name": project + "-config",
        "subPath": "kube-state-metrics-metricbeat.yml",
        "readOnly": True,
    } in deployment["containers"][0]["volumeMounts"]
    assert ("/usr/share/metricbeat/kube-state-metrics-metricbeat.yml") in deployment[
        "containers"
    ][0]["args"]

    assert (
        "configChecksum"
        in r["deployment"][name + "-metrics"]["spec"]["template"]["metadata"][
            "annotations"
        ]
    )


def test_adding_a_secret_mount():
    config = """
daemonset:
  secretMounts:
    - name: elastic-certificates
      secretName: elastic-certificates-name
      path: /usr/share/metricbeat/config/certs
"""
    r = helm_template(config)
    assert {
        "mountPath": "/usr/share/metricbeat/config/certs",
        "name": "elastic-certificates",
    } in r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0][
        "volumeMounts"
    ]
    assert {
        "name": "elastic-certificates",
        "secret": {"secretName": "elastic-certificates-name"},
    } in r["daemonset"][name]["spec"]["template"]["spec"]["volumes"]

    assert {
        "mountPath": "/usr/share/metricbeat/config/certs",
        "name": "elastic-certificates",
    } not in r["deployment"][name + "-metrics"]["spec"]["template"]["spec"][
        "containers"
    ][
        0
    ][
        "volumeMounts"
    ]
    assert {
        "name": "elastic-certificates",
        "secret": {"secretName": "elastic-certificates-name"},
    } not in r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["volumes"]

    config = """
deployment:
  secretMounts:
    - name: elastic-certificates
      secretName: elastic-certificates-name
      path: /usr/share/metricbeat/config/certs
"""
    r = helm_template(config)
    assert {
        "mountPath": "/usr/share/metricbeat/config/certs",
        "name": "elastic-certificates",
    } in r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["containers"][
        0
    ][
        "volumeMounts"
    ]
    assert {
        "name": "elastic-certificates",
        "secret": {"secretName": "elastic-certificates-name"},
    } in r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["volumes"]

    assert {
        "mountPath": "/usr/share/metricbeat/config/certs",
        "name": "elastic-certificates",
    } not in r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0][
        "volumeMounts"
    ]
    assert {
        "name": "elastic-certificates",
        "secret": {"secretName": "elastic-certificates-name"},
    } not in r["daemonset"][name]["spec"]["template"]["spec"]["volumes"]


def test_adding_a_deprecated_secret_mount():
    config = """
secretMounts:
  - name: elastic-certificates
    secretName: elastic-certificates-name
    path: /usr/share/metricbeat/config/certs
"""
    r = helm_template(config)
    assert {
        "mountPath": "/usr/share/metricbeat/config/certs",
        "name": "elastic-certificates",
    } in r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0][
        "volumeMounts"
    ]
    assert {
        "name": "elastic-certificates",
        "secret": {"secretName": "elastic-certificates-name"},
    } in r["daemonset"][name]["spec"]["template"]["spec"]["volumes"]

    assert r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["containers"][
        0
    ]["volumeMounts"][0] == {
        "mountPath": "/usr/share/metricbeat/config/certs",
        "name": "elastic-certificates",
    }
    assert r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["volumes"][
        0
    ] == {
        "name": "elastic-certificates",
        "secret": {"secretName": "elastic-certificates-name"},
    }


def test_adding_a_extra_volume_with_volume_mount():
    config = """
daemonset:
  extraVolumes:
    - name: extras
      emptyDir: {}
  extraVolumeMounts:
    - name: extras
      mountPath: /usr/share/extras
      readOnly: true
"""
    r = helm_template(config)
    assert {"name": "extras", "emptyDir": {}} in r["daemonset"][name]["spec"][
        "template"
    ]["spec"]["volumes"]
    assert {"name": "extras", "mountPath": "/usr/share/extras", "readOnly": True,} in r[
        "daemonset"
    ][name]["spec"]["template"]["spec"]["containers"][0]["volumeMounts"]
    assert {"name": "extras", "emptyDir": {}} not in r["deployment"][name + "-metrics"][
        "spec"
    ]["template"]["spec"]["volumes"]
    assert {
        "name": "extras",
        "mountPath": "/usr/share/extras",
        "readOnly": True,
    } not in r["deployment"][name + "-metrics"]["spec"]["template"]["spec"][
        "containers"
    ][
        0
    ][
        "volumeMounts"
    ]

    config = """
deployment:
  extraVolumes:
    - name: extras
      emptyDir: {}
  extraVolumeMounts:
    - name: extras
      mountPath: /usr/share/extras
      readOnly: true
"""
    r = helm_template(config)
    assert {"name": "extras", "emptyDir": {}} in r["deployment"][name + "-metrics"][
        "spec"
    ]["template"]["spec"]["volumes"]
    assert {"name": "extras", "mountPath": "/usr/share/extras", "readOnly": True,} in r[
        "deployment"
    ][name + "-metrics"]["spec"]["template"]["spec"]["containers"][0]["volumeMounts"]
    assert {"name": "extras", "emptyDir": {}} not in r["daemonset"][name]["spec"][
        "template"
    ]["spec"]["volumes"]
    assert {
        "name": "extras",
        "mountPath": "/usr/share/extras",
        "readOnly": True,
    } not in r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0][
        "volumeMounts"
    ]


def test_adding_a_deprecated_extra_volume_with_volume_mount():
    config = """
extraVolumes:
  - name: extras
    emptyDir: {}
extraVolumeMounts:
  - name: extras
    mountPath: /usr/share/extras
    readOnly: true
"""
    r = helm_template(config)
    assert {"name": "extras", "emptyDir": {}} in r["daemonset"][name]["spec"][
        "template"
    ]["spec"]["volumes"]
    assert {"name": "extras", "mountPath": "/usr/share/extras", "readOnly": True,} in r[
        "daemonset"
    ][name]["spec"]["template"]["spec"]["containers"][0]["volumeMounts"]
    assert {"name": "extras", "emptyDir": {}} in r["deployment"][name + "-metrics"][
        "spec"
    ]["template"]["spec"]["volumes"]
    assert {"name": "extras", "mountPath": "/usr/share/extras", "readOnly": True,} in r[
        "deployment"
    ][name + "-metrics"]["spec"]["template"]["spec"]["containers"][0]["volumeMounts"]


def test_adding_a_node_selector():
    config = """
daemonset:
  nodeSelector:
    disktype: ssd
"""
    r = helm_template(config)
    assert (
        r["daemonset"][name]["spec"]["template"]["spec"]["nodeSelector"]["disktype"]
        == "ssd"
    )
    assert (
        r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["nodeSelector"]
        == {}
    )

    config = """
deployment:
  nodeSelector:
    disktype: ssd
"""
    r = helm_template(config)
    assert (
        r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["nodeSelector"][
            "disktype"
        ]
        == "ssd"
    )
    assert r["daemonset"][name]["spec"]["template"]["spec"]["nodeSelector"] == {}


def test_adding_deprecated_node_selector():
    config = """
nodeSelector:
  disktype: ssd
"""
    r = helm_template(config)
    assert (
        r["daemonset"][name]["spec"]["template"]["spec"]["nodeSelector"]["disktype"]
        == "ssd"
    )


def test_adding_an_affinity_rule():
    config = """
affinity:
  podAntiAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
    - labelSelector:
        matchExpressions:
        - key: app
          operator: In
          values:
          - metricbeat
      topologyKey: kubernetes.io/hostname
"""

    r = helm_template(config)
    assert (
        r["daemonset"][name]["spec"]["template"]["spec"]["affinity"]["podAntiAffinity"][
            "requiredDuringSchedulingIgnoredDuringExecution"
        ][0]["topologyKey"]
        == "kubernetes.io/hostname"
    )
    assert (
        r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["affinity"] == {}
    )

    config = """
daemonset:
  affinity:
    podAntiAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
          - key: app
            operator: In
            values:
            - metricbeat
        topologyKey: kubernetes.io/hostname
"""

    r = helm_template(config)
    assert (
        r["daemonset"][name]["spec"]["template"]["spec"]["affinity"]["podAntiAffinity"][
            "requiredDuringSchedulingIgnoredDuringExecution"
        ][0]["topologyKey"]
        == "kubernetes.io/hostname"
    )

    config = """
deployment:
  affinity:
    podAntiAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
          - key: app
            operator: In
            values:
            - metricbeat
        topologyKey: kubernetes.io/hostname
"""

    r = helm_template(config)
    assert (
        r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["affinity"][
            "podAntiAffinity"
        ]["requiredDuringSchedulingIgnoredDuringExecution"][0]["topologyKey"]
        == "kubernetes.io/hostname"
    )


def test_priority_class_name():
    config = """
priorityClassName: ""
"""
    r = helm_template(config)
    daemonset_spec = r["daemonset"][name]["spec"]["template"]["spec"]
    deployment_spec = r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]
    assert "priorityClassName" not in daemonset_spec
    assert "priorityClassName" not in deployment_spec

    config = """
priorityClassName: "highest"
"""
    r = helm_template(config)
    daemonset_priority_class_name = r["daemonset"][name]["spec"]["template"]["spec"][
        "priorityClassName"
    ]
    deployment_priority_class_name = r["deployment"][name + "-metrics"]["spec"][
        "template"
    ]["spec"]["priorityClassName"]
    assert daemonset_priority_class_name == "highest"
    assert deployment_priority_class_name == "highest"


def test_cluster_role_rules():
    config = ""
    r = helm_template(config)
    rules = r["clusterrole"]["release-name-metricbeat-cluster-role"]["rules"][0]
    assert rules["apiGroups"][0] == ""
    assert rules["verbs"][0] == "get"
    assert rules["resources"][0] == "nodes"

    config = """
clusterRoleRules:
  - apiGroups:
    - "someone"
    verbs:
    - "or"
    resources:
    - "something"
"""
    r = helm_template(config)
    rules = r["clusterrole"]["release-name-metricbeat-cluster-role"]["rules"][0]
    assert rules["apiGroups"][0] == "someone"
    assert rules["verbs"][0] == "or"
    assert rules["resources"][0] == "something"


def test_adding_deprecated_labels():
    config = """
labels:
  app-test: metricbeat
"""
    r = helm_template(config)
    assert r["daemonset"][name]["metadata"]["labels"]["app-test"] == "metricbeat"
    assert (
        r["deployment"][name + "-metrics"]["metadata"]["labels"]["app-test"]
        == "metricbeat"
    )
    assert (
        r["daemonset"][name]["spec"]["template"]["metadata"]["labels"]["app-test"]
        == "metricbeat"
    )
    assert (
        r["deployment"][name + "-metrics"]["spec"]["template"]["metadata"]["labels"][
            "app-test"
        ]
        == "metricbeat"
    )


def test_adding_daemonset_labels():
    config = """
daemonset:
  labels:
    app-test: metricbeat
"""
    r = helm_template(config)
    assert r["daemonset"][name]["metadata"]["labels"]["app-test"] == "metricbeat"
    assert (
        r["daemonset"][name]["spec"]["template"]["metadata"]["labels"]["app-test"]
        == "metricbeat"
    )


def test_adding_daemonset_labels_surpasses_root_labels():
    config = """
labels:
  app-test: root-metricbeat
daemonset:
  labels:
    app-test: daemonset-metricbeat
"""
    r = helm_template(config)
    assert (
        r["daemonset"][name]["metadata"]["labels"]["app-test"] == "daemonset-metricbeat"
    )
    assert (
        r["daemonset"][name]["spec"]["template"]["metadata"]["labels"]["app-test"]
        == "daemonset-metricbeat"
    )


def test_adding_deployment_labels():
    config = """
deployment:
  labels:
    app-test: metricbeat
"""
    r = helm_template(config)
    assert (
        r["deployment"][name + "-metrics"]["metadata"]["labels"]["app-test"]
        == "metricbeat"
    )
    assert (
        r["deployment"][name + "-metrics"]["spec"]["template"]["metadata"]["labels"][
            "app-test"
        ]
        == "metricbeat"
    )


def test_adding_deployment_labels_surpasses_root_labels():
    config = """
labels:
  app-test: root-metricbeat
deployment:
  labels:
    app-test: deployment-metricbeat
"""
    r = helm_template(config)
    assert (
        r["deployment"][name + "-metrics"]["metadata"]["labels"]["app-test"]
        == "deployment-metricbeat"
    )
    assert (
        r["deployment"][name + "-metrics"]["spec"]["template"]["metadata"]["labels"][
            "app-test"
        ]
        == "deployment-metricbeat"
    )


def test_adding_serviceaccount_annotations():
    config = """
serviceAccountAnnotations:
  eks.amazonaws.com/role-arn: arn:aws:iam::111111111111:role/k8s.clustername.namespace.serviceaccount
"""
    r = helm_template(config)
    assert (
        r["serviceaccount"][name]["metadata"]["annotations"][
            "eks.amazonaws.com/role-arn"
        ]
        == "arn:aws:iam::111111111111:role/k8s.clustername.namespace.serviceaccount"
    )


def test_adding_env_from():
    config = """
daemonset:
  envFrom:
  - configMapRef:
      name: configmap-name
"""
    r = helm_template(config)
    assert r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0]["envFrom"][
        0
    ]["configMapRef"] == {"name": "configmap-name"}
    assert (
        r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["containers"][0][
            "envFrom"
        ]
        == []
    )

    config = """
deployment:
  envFrom:
  - configMapRef:
      name: configmap-name
"""
    r = helm_template(config)
    assert r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["containers"][
        0
    ]["envFrom"][0]["configMapRef"] == {"name": "configmap-name"}
    assert (
        r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0]["envFrom"]
        == []
    )


def test_adding_deprecated_env_from():
    config = """
envFrom:
- configMapRef:
    name: configmap-name
"""
    r = helm_template(config)
    assert r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0]["envFrom"][
        0
    ]["configMapRef"] == {"name": "configmap-name"}
    assert r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["containers"][
        0
    ]["envFrom"][0]["configMapRef"] == {"name": "configmap-name"}


def test_overriding_resources():
    config = """
daemonset:
  resources:
    limits:
      cpu: "25m"
      memory: "128Mi"
    requests:
      cpu: "25m"
      memory: "128Mi"
"""
    r = helm_template(config)
    assert r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0][
        "resources"
    ] == {
        "requests": {"cpu": "25m", "memory": "128Mi"},
        "limits": {"cpu": "25m", "memory": "128Mi"},
    }
    assert r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["containers"][
        0
    ]["resources"] == {
        "requests": {"cpu": "100m", "memory": "100Mi"},
        "limits": {"cpu": "1000m", "memory": "200Mi"},
    }

    config = """
deployment:
  resources:
    limits:
      cpu: "25m"
      memory: "128Mi"
    requests:
      cpu: "25m"
      memory: "128Mi"
"""
    r = helm_template(config)
    assert r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0][
        "resources"
    ] == {
        "requests": {"cpu": "100m", "memory": "100Mi"},
        "limits": {"cpu": "1000m", "memory": "200Mi"},
    }
    assert r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["containers"][
        0
    ]["resources"] == {
        "requests": {"cpu": "25m", "memory": "128Mi"},
        "limits": {"cpu": "25m", "memory": "128Mi"},
    }


def test_adding_deprecated_resources():
    config = """
resources:
  limits:
    cpu: "25m"
    memory: "128Mi"
  requests:
    cpu: "25m"
    memory: "128Mi"
"""
    r = helm_template(config)
    assert r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0][
        "resources"
    ] == {
        "requests": {"cpu": "25m", "memory": "128Mi"},
        "limits": {"cpu": "25m", "memory": "128Mi"},
    }
    assert r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["containers"][
        0
    ]["resources"] == {
        "requests": {"cpu": "25m", "memory": "128Mi"},
        "limits": {"cpu": "25m", "memory": "128Mi"},
    }


def test_setting_fullnameOverride():
    config = """
fullnameOverride: 'metricbeat-custom'
"""
    r = helm_template(config)

    custom_name = "metricbeat-custom"
    assert custom_name in r["daemonset"]
    assert (
        r["daemonset"][custom_name]["spec"]["template"]["spec"]["containers"][0]["name"]
        == project
    )
    assert (
        r["daemonset"][custom_name]["spec"]["template"]["spec"]["serviceAccountName"]
        == name
    )
    volumes = r["daemonset"][custom_name]["spec"]["template"]["spec"]["volumes"]
    assert {
        "name": "data",
        "hostPath": {
            "path": "/var/lib/" + custom_name + "-default-data",
            "type": "DirectoryOrCreate",
        },
    } in volumes


def test_adding_annotations():
    config = """
daemonset:
    annotations:
        foo: "bar"
"""
    r = helm_template(config)
    assert "foo" in r["daemonset"][name]["metadata"]["annotations"]
    assert r["daemonset"][name]["metadata"]["annotations"]["foo"] == "bar"
    assert "annotations" not in r["deployment"][name + "-metrics"]["metadata"]
    config = """
deployment:
    annotations:
        grault: "waldo"
"""
    r = helm_template(config)
    assert "grault" in r["deployment"][name + "-metrics"]["metadata"]["annotations"]
    assert (
        r["deployment"][name + "-metrics"]["metadata"]["annotations"]["grault"]
        == "waldo"
    )
    assert "annotations" not in r["daemonset"][name]["metadata"]


def test_disable_daemonset():
    config = """
daemonset:
    enabled: false
"""
    r = helm_template(config)
    cfg = r["configmap"]

    assert name not in r.get("daemonset", {})
    assert name + "-daemonset-config" not in cfg
    assert name + "-deployment-config" in cfg


def test_disable_deployment():
    config = """
deployment:
    enabled: false
"""
    r = helm_template(config)
    cfg = r["configmap"]

    assert name + "-metrics" not in r.get("deployment", {})
    assert name + "-daemonset-config" in cfg
    assert name + "-deployment-config" not in cfg


def test_do_not_install_kube_stat_metrics():
    config = """
kube_state_metrics:
  enabled: false
"""
    r = helm_template(config)

    assert kube_state_metric_name not in r["deployment"]
    assert (
        r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["containers"][0][
            "env"
        ][1]["name"]
        == "KUBE_STATE_METRICS_HOSTS"
    )
    assert (
        r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["containers"][0][
            "env"
        ][1]["value"]
        == "kube-state-metrics:8080"
    )


def test_custom_kube_stat_metrics_host():
    config = """
kube_state_metrics:
  enabled: false
  host: "kube-state-metrics.kube-system:9999"
"""
    r = helm_template(config)

    assert (
        r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]["containers"][0][
            "env"
        ][1]["value"]
        == "kube-state-metrics.kube-system:9999"
    )


def test_adding_a_secret():
    content = "LS1CRUdJTiBgUFJJVkFURSB"
    config = """
secrets:
  - name: "env"
    value:
      ELASTICSEARCH_PASSWORD: {elk_pass}
""".format(
        elk_pass=content
    )
    content_b64 = base64.b64encode(content.encode("ascii")).decode("ascii")

    r = helm_template(config)
    secret_name = name + "-env"
    s = r["secret"][secret_name]
    assert s["metadata"]["labels"]["app"] == name
    assert len(r["secret"]) == 1
    assert len(s["data"]) == 1
    assert s["data"] == {"ELASTICSEARCH_PASSWORD": content_b64}


def test_adding_secret_from_file():
    content = """
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEApCt3ychnqZHsS
DylPFZn55xDaDcWco1oNFdBGzFjw+
zkuMFMOv7ab+yOFwHeEeAAEkEgy1u
Da1vIscBs1K0kbEFRSqySLuNHWiJp
wK2cI/gJc+S9Qd9Qsn0XGjmjQ6P2p
ot2hvCOtnei998OmDSYORKBq2jiv/
-----END RSA PRIVATE KEY-----
"""
    config = """
secrets:
  - name: "tls"
    value:
      cert.key.filepath: "secrets/private.key"
"""
    content_b64 = base64.b64encode(content.encode("ascii")).decode("ascii")
    work_dir = os.path.join(os.path.abspath(os.getcwd()), "secrets")
    filename = os.path.join(work_dir, "private.key")
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write(content)

    with open(filename, "r") as f:
        data = f.read()
        assert data == content

    r = helm_template(config)
    secret_name = name + "-tls"
    s = r["secret"][secret_name]
    assert s["metadata"]["labels"]["app"] == name
    assert len(r["secret"]) == 1
    assert len(s["data"]) == 1
    assert s["data"] == {
        "cert.key": content_b64,
    }

    os.remove(filename)
    os.rmdir(work_dir)


def test_adding_multiple_data_secret():
    content = {
        "elk_pass": "LS1CRUdJTiBgUFJJVkFURSB",
        "api_key": "ui2CsdUadTiBasRJRkl9tvNnw",
    }
    config = """
secrets:
  - name: "env"
    value:
      ELASTICSEARCH_PASSWORD: {elk_pass}
      api_key: {api_key}
""".format(
        elk_pass=content["elk_pass"], api_key=content["api_key"]
    )
    content_b64 = {
        "elk_pass": base64.b64encode(content["elk_pass"].encode("ascii")).decode(
            "ascii"
        ),
        "api_key": base64.b64encode(content["api_key"].encode("ascii")).decode("ascii"),
    }

    r = helm_template(config)
    secret_name = name + "-env"
    s = r["secret"][secret_name]
    assert s["metadata"]["labels"]["app"] == name
    assert len(r["secret"]) == 1
    assert len(s["data"]) == 2
    assert s["data"] == {
        "ELASTICSEARCH_PASSWORD": content_b64["elk_pass"],
        "api_key": content_b64["api_key"],
    }


def test_adding_multiple_secrets():
    content = {
        "elk_pass": "LS1CRUdJTiBgUFJJVkFURSB",
        "cert_crt": "LS0tLS1CRUdJTiBlRJRALKJDDQVRFLS0tLS0K",
        "cert_key": "LS0tLS1CRUdJTiBgUFJJVkFURSBLRVktLS0tLQo",
    }
    config = """
secrets:
  - name: "env"
    value:
      ELASTICSEARCH_PASSWORD: {elk_pass}
  - name: "tls"
    value:
      cert.crt: {cert_crt}
      cert.key: {cert_key}

""".format(
        elk_pass=content["elk_pass"],
        cert_crt=content["cert_crt"],
        cert_key=content["cert_key"],
    )
    content_b64 = {
        "elk_pass": base64.b64encode(content["elk_pass"].encode("ascii")).decode(
            "ascii"
        ),
        "cert_crt": base64.b64encode(content["cert_crt"].encode("ascii")).decode(
            "ascii"
        ),
        "cert_key": base64.b64encode(content["cert_key"].encode("ascii")).decode(
            "ascii"
        ),
    }

    r = helm_template(config)
    secret_names = {"env": name + "-env", "tls": name + "-tls"}
    s_env = r["secret"][secret_names["env"]]
    s_tls = r["secret"][secret_names["tls"]]
    assert len(r["secret"]) == 2
    assert len(s_env["data"]) == 1
    assert s_env["data"] == {
        "ELASTICSEARCH_PASSWORD": content_b64["elk_pass"],
    }
    assert len(s_tls["data"]) == 2
    assert s_tls["data"] == {
        "cert.crt": content_b64["cert_crt"],
        "cert.key": content_b64["cert_key"],
    }


def test_hostaliases():
    config = """
daemonset:
  hostAliases:
  - ip: "127.0.0.1"
    hostnames:
    - "foo.local"
    - "bar.local"
"""
    r = helm_template(config)
    assert (
        "hostAliases"
        not in r["deployment"][name + "-metrics"]["spec"]["template"]["spec"]
    )
    hostAliases = r["daemonset"][name]["spec"]["template"]["spec"]["hostAliases"]
    assert {"ip": "127.0.0.1", "hostnames": ["foo.local", "bar.local"]} in hostAliases

    config = """
deployment:
  hostAliases:
  - ip: "127.0.0.1"
    hostnames:
    - "foo.local"
    - "bar.local"
"""
    r = helm_template(config)
    assert "hostAliases" not in r["daemonset"][name]["spec"]["template"]["spec"]
    hostAliases = r["deployment"][name + "-metrics"]["spec"]["template"]["spec"][
        "hostAliases"
    ]
    assert {"ip": "127.0.0.1", "hostnames": ["foo.local", "bar.local"]} in hostAliases
