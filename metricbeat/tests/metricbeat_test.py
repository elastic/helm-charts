import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], "../../helpers"))
from helpers import helm_template

project = "metricbeat"
name = "release-name-" + project


def test_defaults():
    config = """
    """

    r = helm_template(config)

    assert name in r["daemonset"]

    c = r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0]
    assert c["name"] == project
    assert c["image"].startswith("docker.elastic.co/beats/" + project + ":")

    assert c["env"][0]["name"] == "POD_NAMESPACE"
    assert c["env"][0]["valueFrom"]["fieldRef"]["fieldPath"] == "metadata.namespace"

    assert "curl --fail 127.0.0.1:5066" in c["livenessProbe"]["exec"]["command"][-1]

    assert "metricbeat test output" in c["readinessProbe"]["exec"]["command"][-1]

    # Empty customizable defaults
    assert "imagePullSecrets" not in r["daemonset"][name]["spec"]["template"]["spec"]
    assert "tolerations" not in r["daemonset"][name]["spec"]["template"]["spec"]

    assert r["daemonset"][name]["spec"]["updateStrategy"]["type"] == "RollingUpdate"

    assert (
        r["daemonset"][name]["spec"]["template"]["spec"]["serviceAccountName"] == name
    )

    volumes = r["daemonset"][name]["spec"]["template"]["spec"]["volumes"]
    assert {
        "name": "data",
        "hostPath": {
            "path": "/var/lib/" + name + "-default-data",
            "type": "DirectoryOrCreate",
        },
    } in volumes


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
extraEnvs:
- name: LOG_LEVEL
  value: DEBUG
"""
    r = helm_template(config)
    envs = r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0]["env"]
    assert {"name": "LOG_LEVEL", "value": "DEBUG"} in envs


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


def test_adding_tolerations():
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
podSecurityContext:
  runAsUser: 1001
  privileged: false
"""
    r = helm_template(config)
    c = r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0]
    assert c["securityContext"]["runAsUser"] == 1001
    assert c["securityContext"]["privileged"] == False


def test_adding_in_metricbeat_config():
    config = """
metricbeatConfig:
  metricbeat.yml: |
    key:
      nestedkey: value
    dot.notation: test

  other-config.yml: |
    hello = world
"""
    r = helm_template(config)
    c = r["configmap"][name + "-config"]["data"]

    assert "metricbeat.yml" in c
    assert "other-config.yml" in c

    assert "nestedkey: value" in c["metricbeat.yml"]
    assert "dot.notation: test" in c["metricbeat.yml"]

    assert "hello = world" in c["other-config.yml"]

    d = r["daemonset"][name]["spec"]["template"]["spec"]

    assert {
        "configMap": {"name": name + "-config", "defaultMode": 0o600},
        "name": project + "-config",
    } in d["volumes"]
    assert {
        "mountPath": "/usr/share/metricbeat/metricbeat.yml",
        "name": project + "-config",
        "subPath": "metricbeat.yml",
        "readOnly": True,
    } in d["containers"][0]["volumeMounts"]
    assert {
        "mountPath": "/usr/share/metricbeat/other-config.yml",
        "name": project + "-config",
        "subPath": "other-config.yml",
        "readOnly": True,
    } in d["containers"][0]["volumeMounts"]

    assert (
        "configChecksum"
        in r["daemonset"][name]["spec"]["template"]["metadata"]["annotations"]
    )


def test_adding_a_secret_mount():
    config = """
secretMounts:
  - name: elastic-certificates
    secretName: elastic-certificates-name
    path: /usr/share/metricbeat/config/certs
"""
    r = helm_template(config)
    s = r["daemonset"][name]["spec"]["template"]["spec"]
    assert s["containers"][0]["volumeMounts"][0] == {
        "mountPath": "/usr/share/metricbeat/config/certs",
        "name": "elastic-certificates",
    }
    assert s["volumes"][0] == {
        "name": "elastic-certificates",
        "secret": {"secretName": "elastic-certificates-name"},
    }


def test_adding_a_extra_volume_with_volume_mount():
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
    extraVolume = r["daemonset"][name]["spec"]["template"]["spec"]["volumes"]
    assert {"name": "extras", "emptyDir": {}} in extraVolume
    extraVolumeMounts = r["daemonset"][name]["spec"]["template"]["spec"]["containers"][
        0
    ]["volumeMounts"]
    assert {
        "name": "extras",
        "mountPath": "/usr/share/extras",
        "readOnly": True,
    } in extraVolumeMounts


def test_adding_a_node_selector():
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


def test_adding_pod_labels():
    config = """
labels:
  app.kubernetes.io/name: metricbeat
"""
    r = helm_template(config)
    assert (
        r["daemonset"][name]["metadata"]["labels"]["app.kubernetes.io/name"]
        == "metricbeat"
    )
    assert (
        r["daemonset"][name]["spec"]["template"]["metadata"]["labels"][
            "app.kubernetes.io/name"
        ]
        == "metricbeat"
    )


def test_adding_env_from():
    config = """
envFrom:
- configMapRef:
    name: configmap-name
"""
    r = helm_template(config)
    configMapRef = r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0][
        "envFrom"
    ][0]["configMapRef"]
    assert configMapRef == {"name": "configmap-name"}


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
