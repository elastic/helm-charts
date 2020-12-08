import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], "../../helpers"))
from helpers import helm_template

project = "filebeat"
name = "release-name-" + project


def test_defaults():
    config = """
    """

    r = helm_template(config)

    assert name in r["daemonset"]
    assert name in r["deployment"]

    c = r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0]
    assert c["name"] == project
    assert c["image"].startswith("docker.elastic.co/beats/" + project + ":")

    assert c["env"][0]["name"] == "POD_NAMESPACE"
    assert c["env"][0]["valueFrom"]["fieldRef"]["fieldPath"] == "metadata.namespace"

    assert "curl --fail 127.0.0.1:5066" in c["livenessProbe"]["exec"]["command"][-1]

    assert "filebeat test output" in c["readinessProbe"]["exec"]["command"][-1]

    assert r["daemonset"][name]["spec"]["template"]["spec"]["tolerations"] == []

    assert "hostNetwork" not in r["daemonset"][name]["spec"]["template"]["spec"]
    assert "dnsPolicy" not in r["daemonset"][name]["spec"]["template"]["spec"]
    assert "hostNetwork" not in r["deployment"][name]["spec"]["template"]["spec"]
    assert "dnsPolicy" not in r["deployment"][name]["spec"]["template"]["spec"]

    assert r["deployment"][name]["spec"]["template"]["spec"]["tolerations"] == []

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
        r["deployment"][name]["spec"]["template"]["spec"]["containers"][0][
            "securityContext"
        ]["runAsUser"]
        == 0
    )
    assert (
        r["deployment"][name]["spec"]["template"]["spec"]["containers"][0][
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

    assert "filebeat.yml" in cfg[name + "-daemonset-config"]["data"]
    assert "filebeat.yml" in cfg[name + "-deployment-config"]["data"]

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
            "path": "/var/lib/" + name + "-data",
            "type": "DirectoryOrCreate",
        },
    } in daemonset["volumes"]

    assert {
        "mountPath": "/usr/share/filebeat/filebeat.yml",
        "name": project + "-config",
        "subPath": "filebeat.yml",
        "readOnly": True,
    } in daemonset["containers"][0]["volumeMounts"]

    deployment = r["deployment"][name]["spec"]["template"]["spec"]

    assert {
        "configMap": {"name": name + "-config", "defaultMode": 0o600},
        "name": project + "-config",
    } not in deployment["volumes"]
    assert {
        "configMap": {"name": name + "-deployment-config", "defaultMode": 0o600},
        "name": project + "-config",
    } in deployment["volumes"]

    assert {
        "mountPath": "/usr/share/filebeat/filebeat.yml",
        "name": project + "-config",
        "subPath": "filebeat.yml",
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
    deployment_name = name
    extraContainerDeployment = r["deployment"][deployment_name]["spec"]["template"][
        "spec"
    ]["containers"]
    assert {
        "name": "do-something",
        "image": "busybox",
        "command": ["do", "something"],
    } in extraContainerDeployment


def test_adding_init_containers_as_yaml():
    config = """
extraInitContainers:
- name: dummy-init
  image: busybox
  command: ['echo', 'hey']
"""
    r = helm_template(config)
    initContainers = r["daemonset"][name]["spec"]["template"]["spec"]["initContainers"]
    assert {
        "name": "dummy-init",
        "image": "busybox",
        "command": ["echo", "hey"],
    } in initContainers


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
    deployment_name = name
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
    assert {"name": "LOG_LEVEL", "value": "DEBUG"} not in r["deployment"][name]["spec"][
        "template"
    ]["spec"]["containers"][0]["env"]

    config = """
deployment:
  extraEnvs:
  - name: LOG_LEVEL
    value: DEBUG
"""
    r = helm_template(config)
    assert {"name": "LOG_LEVEL", "value": "DEBUG"} in r["deployment"][name]["spec"][
        "template"
    ]["spec"]["containers"][0]["env"]
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
    assert {"name": "LOG_LEVEL", "value": "DEBUG"} in r["deployment"][name]["spec"][
        "template"
    ]["spec"]["containers"][0]["env"]


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
    assert "hostNetwork" not in r["deployment"][name]["spec"]["template"]["spec"]
    assert "dnsPolicy" not in r["deployment"][name]["spec"]["template"]["spec"]


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
    assert r["deployment"][name]["spec"]["template"]["spec"]["tolerations"] == []

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
        r["deployment"][name]["spec"]["template"]["spec"]["tolerations"][0]["key"]
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
        r["deployment"][name]["spec"]["template"]["spec"]["tolerations"][0]["key"]
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
    assert "serviceaccount" not in r
    assert "clusterrole" not in r
    assert "clusterrolebinding" not in r


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
        r["deployment"][name]["spec"]["template"]["spec"]["containers"][0][
            "securityContext"
        ]["runAsUser"]
        == 0
    )
    assert (
        r["deployment"][name]["spec"]["template"]["spec"]["containers"][0][
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
        r["deployment"][name]["spec"]["template"]["spec"]["containers"][0][
            "securityContext"
        ]["runAsUser"]
        == 1001
    )
    assert (
        r["deployment"][name]["spec"]["template"]["spec"]["containers"][0][
            "securityContext"
        ]["privileged"]
        == False
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
        r["deployment"][name]["spec"]["template"]["spec"]["containers"][0][
            "securityContext"
        ]["runAsUser"]
        == 1001
    )
    assert (
        r["deployment"][name]["spec"]["template"]["spec"]["containers"][0][
            "securityContext"
        ]["privileged"]
        == False
    )


def test_adding_in_filebeat_config():
    config = """
daemonset:
  filebeatConfig:
    filebeat.yml: |
      key: daemonset
    daemonset-config.yml: |
      hello = daemonset

deployment:
  filebeatConfig:
    filebeat.yml: |
      key: deployment
    deployment-config.yml: |
      hello = deployment
"""
    r = helm_template(config)
    cfg = r["configmap"]

    assert "filebeat.yml" in cfg[name + "-daemonset-config"]["data"]
    assert "daemonset-config.yml" in cfg[name + "-daemonset-config"]["data"]
    assert "deployment-config.yml" not in cfg[name + "-daemonset-config"]["data"]
    assert "filebeat.yml" in cfg[name + "-deployment-config"]["data"]
    assert "deployment-config.yml" in cfg[name + "-deployment-config"]["data"]
    assert "daemonset-config.yml" not in cfg[name + "-deployment-config"]["data"]

    assert "key: daemonset" in cfg[name + "-daemonset-config"]["data"]["filebeat.yml"]
    assert "key: deployment" in cfg[name + "-deployment-config"]["data"]["filebeat.yml"]

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
        "mountPath": "/usr/share/filebeat/daemonset-config.yml",
        "name": project + "-config",
        "subPath": "daemonset-config.yml",
        "readOnly": True,
    } in daemonset["containers"][0]["volumeMounts"]

    deployment = r["deployment"][name]["spec"]["template"]["spec"]
    assert {
        "mountPath": "/usr/share/filebeat/deployment-config.yml",
        "name": project + "-config",
        "subPath": "deployment-config.yml",
        "readOnly": True,
    } in deployment["containers"][0]["volumeMounts"]


def test_adding_in_deprecated_filebeat_config():
    config = """
filebeatConfig:
  filebeat.yml: |
    key:
      nestedkey: value
    dot.notation: test
"""
    r = helm_template(config)
    c = r["configmap"][name + "-config"]["data"]

    assert "filebeat.yml" in c

    assert "nestedkey: value" in c["filebeat.yml"]
    assert "dot.notation: test" in c["filebeat.yml"]

    daemonset = r["daemonset"][name]["spec"]["template"]["spec"]

    assert {
        "configMap": {"name": name + "-config", "defaultMode": 0o600},
        "name": project + "-config",
    } in daemonset["volumes"]
    assert {
        "mountPath": "/usr/share/filebeat/filebeat.yml",
        "name": project + "-config",
        "subPath": "filebeat.yml",
        "readOnly": True,
    } in daemonset["containers"][0]["volumeMounts"]

    assert (
        "configChecksum"
        in r["daemonset"][name]["spec"]["template"]["metadata"]["annotations"]
    )

    deployment = r["deployment"][name]["spec"]["template"]["spec"]

    assert {
        "configMap": {"name": name + "-config", "defaultMode": 0o600},
        "name": project + "-config",
    } in deployment["volumes"]
    assert {
        "mountPath": "/usr/share/filebeat/filebeat.yml",
        "name": project + "-config",
        "subPath": "filebeat.yml",
        "readOnly": True,
    } in deployment["containers"][0]["volumeMounts"]

    assert (
        "configChecksum"
        in r["deployment"][name]["spec"]["template"]["metadata"]["annotations"]
    )


def test_adding_a_secret_mount():
    config = """
daemonset:
  secretMounts:
    - name: elastic-certificates
      secretName: elastic-certificates-name
      path: /usr/share/filebeat/config/certs
"""
    r = helm_template(config)
    assert (
        {
            "mountPath": "/usr/share/filebeat/config/certs",
            "name": "elastic-certificates",
        }
        in r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0][
            "volumeMounts"
        ]
    )
    assert {
        "name": "elastic-certificates",
        "secret": {"secretName": "elastic-certificates-name"},
    } in r["daemonset"][name]["spec"]["template"]["spec"]["volumes"]

    assert (
        {
            "mountPath": "/usr/share/filebeat/config/certs",
            "name": "elastic-certificates",
        }
        not in r["deployment"][name]["spec"]["template"]["spec"]["containers"][0][
            "volumeMounts"
        ]
    )
    assert {
        "name": "elastic-certificates",
        "secret": {"secretName": "elastic-certificates-name"},
    } not in r["deployment"][name]["spec"]["template"]["spec"]["volumes"]

    config = """
deployment:
  secretMounts:
    - name: elastic-certificates
      secretName: elastic-certificates-name
      path: /usr/share/filebeat/config/certs
"""
    r = helm_template(config)
    assert (
        {
            "mountPath": "/usr/share/filebeat/config/certs",
            "name": "elastic-certificates",
        }
        in r["deployment"][name]["spec"]["template"]["spec"]["containers"][0][
            "volumeMounts"
        ]
    )
    assert {
        "name": "elastic-certificates",
        "secret": {"secretName": "elastic-certificates-name"},
    } in r["deployment"][name]["spec"]["template"]["spec"]["volumes"]

    assert (
        {
            "mountPath": "/usr/share/filebeat/config/certs",
            "name": "elastic-certificates",
        }
        not in r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0][
            "volumeMounts"
        ]
    )
    assert {
        "name": "elastic-certificates",
        "secret": {"secretName": "elastic-certificates-name"},
    } not in r["daemonset"][name]["spec"]["template"]["spec"]["volumes"]


def test_adding_a_deprecated_secret_mount():
    config = """
secretMounts:
  - name: elastic-certificates
    secretName: elastic-certificates-name
    path: /usr/share/filebeat/config/certs
"""
    r = helm_template(config)
    assert (
        {
            "mountPath": "/usr/share/filebeat/config/certs",
            "name": "elastic-certificates",
        }
        in r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0][
            "volumeMounts"
        ]
    )
    assert {
        "name": "elastic-certificates",
        "secret": {"secretName": "elastic-certificates-name"},
    } in r["daemonset"][name]["spec"]["template"]["spec"]["volumes"]

    assert r["deployment"][name]["spec"]["template"]["spec"]["containers"][0][
        "volumeMounts"
    ][0] == {
        "mountPath": "/usr/share/filebeat/config/certs",
        "name": "elastic-certificates",
    }
    assert r["deployment"][name]["spec"]["template"]["spec"]["volumes"][0] == {
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
    assert {"name": "extras", "emptyDir": {}} not in r["deployment"][name]["spec"][
        "template"
    ]["spec"]["volumes"]
    assert (
        {"name": "extras", "mountPath": "/usr/share/extras", "readOnly": True,}
        not in r["deployment"][name]["spec"]["template"]["spec"]["containers"][0][
            "volumeMounts"
        ]
    )

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
    assert {"name": "extras", "emptyDir": {}} in r["deployment"][name]["spec"][
        "template"
    ]["spec"]["volumes"]
    assert {"name": "extras", "mountPath": "/usr/share/extras", "readOnly": True,} in r[
        "deployment"
    ][name]["spec"]["template"]["spec"]["containers"][0]["volumeMounts"]
    assert {"name": "extras", "emptyDir": {}} not in r["daemonset"][name]["spec"][
        "template"
    ]["spec"]["volumes"]
    assert (
        {"name": "extras", "mountPath": "/usr/share/extras", "readOnly": True,}
        not in r["daemonset"][name]["spec"]["template"]["spec"]["containers"][0][
            "volumeMounts"
        ]
    )


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
    assert {"name": "extras", "emptyDir": {}} in r["deployment"][name]["spec"][
        "template"
    ]["spec"]["volumes"]
    assert {"name": "extras", "mountPath": "/usr/share/extras", "readOnly": True,} in r[
        "deployment"
    ][name]["spec"]["template"]["spec"]["containers"][0]["volumeMounts"]


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
    assert r["deployment"][name]["spec"]["template"]["spec"]["nodeSelector"] == {}

    config = """
deployment:
  nodeSelector:
    disktype: ssd
"""
    r = helm_template(config)
    assert (
        r["deployment"][name]["spec"]["template"]["spec"]["nodeSelector"]["disktype"]
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
          - filebeat
      topologyKey: kubernetes.io/hostname
"""

    r = helm_template(config)
    assert (
        r["daemonset"][name]["spec"]["template"]["spec"]["affinity"]["podAntiAffinity"][
            "requiredDuringSchedulingIgnoredDuringExecution"
        ][0]["topologyKey"]
        == "kubernetes.io/hostname"
    )
    assert r["deployment"][name]["spec"]["template"]["spec"]["affinity"] == {}

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
            - filebeat
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
            - filebeat
        topologyKey: kubernetes.io/hostname
"""

    r = helm_template(config)
    assert (
        r["deployment"][name]["spec"]["template"]["spec"]["affinity"][
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
    deployment_spec = r["deployment"][name]["spec"]["template"]["spec"]
    assert "priorityClassName" not in daemonset_spec
    assert "priorityClassName" not in deployment_spec

    config = """
priorityClassName: "highest"
"""
    r = helm_template(config)
    daemonset_priority_class_name = r["daemonset"][name]["spec"]["template"]["spec"][
        "priorityClassName"
    ]
    deployment_priority_class_name = r["deployment"][name]["spec"]["template"]["spec"][
        "priorityClassName"
    ]
    assert daemonset_priority_class_name == "highest"
    assert deployment_priority_class_name == "highest"


def test_adding_deprecated_labels():
    config = """
labels:
  app-test: filebeat
"""
    r = helm_template(config)
    assert r["daemonset"][name]["metadata"]["labels"]["app-test"] == "filebeat"
    assert r["deployment"][name]["metadata"]["labels"]["app-test"] == "filebeat"
    assert (
        r["daemonset"][name]["spec"]["template"]["metadata"]["labels"]["app-test"]
        == "filebeat"
    )
    assert (
        r["deployment"][name]["spec"]["template"]["metadata"]["labels"]["app-test"]
        == "filebeat"
    )


def test_adding_daemonset_labels():
    config = """
daemonset:
  labels:
    app-test: filebeat
"""
    r = helm_template(config)
    assert r["daemonset"][name]["metadata"]["labels"]["app-test"] == "filebeat"
    assert (
        r["daemonset"][name]["spec"]["template"]["metadata"]["labels"]["app-test"]
        == "filebeat"
    )


def test_adding_daemonset_labels_surpasses_root_labels():
    config = """
labels:
  app-test: root-filebeat
daemonset:
  labels:
    app-test: daemonset-filebeat
"""
    r = helm_template(config)
    assert (
        r["daemonset"][name]["metadata"]["labels"]["app-test"] == "daemonset-filebeat"
    )
    assert (
        r["daemonset"][name]["spec"]["template"]["metadata"]["labels"]["app-test"]
        == "daemonset-filebeat"
    )


def test_adding_deployment_labels():
    config = """
deployment:
  labels:
    app-test: filebeat
"""
    r = helm_template(config)
    assert r["deployment"][name]["metadata"]["labels"]["app-test"] == "filebeat"
    assert (
        r["deployment"][name]["spec"]["template"]["metadata"]["labels"]["app-test"]
        == "filebeat"
    )


def test_adding_deployment_labels_surpasses_root_labels():
    config = """
labels:
  app-test: root-filebeat
deployment:
  labels:
    app-test: deployment-filebeat
"""
    r = helm_template(config)
    assert (
        r["deployment"][name]["metadata"]["labels"]["app-test"] == "deployment-filebeat"
    )
    assert (
        r["deployment"][name]["spec"]["template"]["metadata"]["labels"]["app-test"]
        == "deployment-filebeat"
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
        r["deployment"][name]["spec"]["template"]["spec"]["containers"][0]["envFrom"]
        == []
    )

    config = """
deployment:
  envFrom:
  - configMapRef:
      name: configmap-name
"""
    r = helm_template(config)
    assert r["deployment"][name]["spec"]["template"]["spec"]["containers"][0][
        "envFrom"
    ][0]["configMapRef"] == {"name": "configmap-name"}
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
    assert r["deployment"][name]["spec"]["template"]["spec"]["containers"][0][
        "envFrom"
    ][0]["configMapRef"] == {"name": "configmap-name"}


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
    assert r["deployment"][name]["spec"]["template"]["spec"]["containers"][0][
        "resources"
    ] == {
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
    assert r["deployment"][name]["spec"]["template"]["spec"]["containers"][0][
        "resources"
    ] == {
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
    assert r["deployment"][name]["spec"]["template"]["spec"]["containers"][0][
        "resources"
    ] == {
        "requests": {"cpu": "25m", "memory": "128Mi"},
        "limits": {"cpu": "25m", "memory": "128Mi"},
    }


def test_setting_fullnameOverride():
    config = """
fullnameOverride: 'filebeat-custom'
"""
    r = helm_template(config)

    custom_name = "filebeat-custom"
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
            "path": "/var/lib/" + custom_name + "-data",
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
    assert "annotations" not in r["deployment"][name]["metadata"]
    config = """
deployment:
    annotations:
        grault: "waldo"
"""
    r = helm_template(config)
    assert "grault" in r["deployment"][name]["metadata"]["annotations"]
    assert r["deployment"][name]["metadata"]["annotations"]["grault"] == "waldo"
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

    assert name + "-daemonset-config" in cfg
    assert name + "-deployment-config" not in cfg
