import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], "../../helpers"))
from helpers import helm_template

project = "apm-server"
name = "release-name-" + project


def test_defaults():
    config = ""

    r = helm_template(config)
    assert name in r["deployment"]
    assert name in r["service"]

    s = r["service"][name]["spec"]
    assert s["ports"][0]["port"] == 8200
    assert s["ports"][0]["name"] == "http"
    assert s["ports"][0]["protocol"] == "TCP"
    assert s["ports"][0]["targetPort"] == 8200

    c = r["deployment"][name]["spec"]["template"]["spec"]["containers"][0]
    assert c["name"] == "apm-server"
    assert c["image"].startswith("docker.elastic.co/apm/apm-server:")
    assert c["ports"][0]["containerPort"] == 8200


def test_adding_a_extra_container():
    config = """
extraContainers: |
  - name: do-something
    image: busybox
    command: ['do', 'something']
"""
    r = helm_template(config)
    extraContainer = r["deployment"][name]["spec"]["template"]["spec"]["containers"]
    assert {
        "name": "do-something",
        "image": "busybox",
        "command": ["do", "something"],
    } in extraContainer


def test_adding_a_extra_init_container():
    config = """
extraInitContainers: |
  - name: do-something
    image: busybox
    command: ['do', 'something']
"""
    r = helm_template(config)
    extraInitContainer = r["deployment"][name]["spec"]["template"]["spec"][
        "initContainers"
    ]
    assert {
        "name": "do-something",
        "image": "busybox",
        "command": ["do", "something"],
    } in extraInitContainer


def test_adding_envs():
    config = """
extraEnvs:
- name: LOG_LEVEL
  value: DEBUG
"""
    r = helm_template(config)
    envs = r["deployment"][name]["spec"]["template"]["spec"]["containers"][0]["env"]
    assert {"name": "LOG_LEVEL", "value": "DEBUG"} in envs


def test_adding_env_from():
    config = """
envFrom:
- secretRef:
    name: secret-name
"""
    r = helm_template(config)
    secretRef = r["deployment"][name]["spec"]["template"]["spec"]["containers"][0][
        "envFrom"
    ][0]["secretRef"]
    assert secretRef == {"name": "secret-name"}


def test_adding_image_pull_secrets():
    config = """
imagePullSecrets:
  - name: test-registry
"""
    r = helm_template(config)
    assert (
        r["deployment"][name]["spec"]["template"]["spec"]["imagePullSecrets"][0]["name"]
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
        r["deployment"][name]["spec"]["template"]["spec"]["tolerations"][0]["key"]
        == "key1"
    )


def test_override_the_default_update_strategy():
    config = """
updateStrategy:
  type: "OnDelete"
"""

    r = helm_template(config)
    assert r["deployment"][name]["spec"]["strategy"]["type"] == "OnDelete"


def test_setting_a_custom_service_account():
    config = """
serviceAccount: notdefault
"""
    r = helm_template(config)
    assert (
        r["deployment"][name]["spec"]["template"]["spec"]["serviceAccountName"]
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
podSecurityContext:
  runAsUser: 1001
  privileged: false
"""
    r = helm_template(config)
    c = r["deployment"][name]["spec"]["template"]["spec"]["containers"][0]
    assert c["securityContext"]["runAsUser"] == 1001
    assert c["securityContext"]["privileged"] is False


def test_adding_in_apm_config():
    config = """
apmConfig:
  apm-server.yml: |
    key:
      nestedkey: value
    dot.notation: test

  other-config.yml: |
    hello = world
"""
    r = helm_template(config)
    print(r["configmap"].keys())
    c = r["configmap"][name + "-config"]["data"]

    assert "apm-server.yml" in c
    assert "other-config.yml" in c

    assert "nestedkey: value" in c["apm-server.yml"]
    assert "dot.notation: test" in c["apm-server.yml"]

    assert "hello = world" in c["other-config.yml"]

    d = r["deployment"][name]["spec"]["template"]["spec"]

    assert {
        "configMap": {"name": name + "-config", "defaultMode": 0o600},
        "name": project + "-config",
    } in d["volumes"]
    assert {
        "mountPath": "/usr/share/apm-server/apm-server.yml",
        "name": project + "-config",
        "subPath": "apm-server.yml",
        "readOnly": True,
    } in d["containers"][0]["volumeMounts"]
    assert {
        "mountPath": "/usr/share/apm-server/other-config.yml",
        "name": project + "-config",
        "subPath": "other-config.yml",
        "readOnly": True,
    } in d["containers"][0]["volumeMounts"]

    assert (
        "configChecksum"
        in r["deployment"][name]["spec"]["template"]["metadata"]["annotations"].keys()
    )


def test_adding_a_secret_mount():
    config = """
secretMounts:
  - name: elastic-certificates
    secretName: elastic-certs
    path: /usr/share/apm-server/config/certs
"""
    r = helm_template(config)
    s = r["deployment"][name]["spec"]["template"]["spec"]
    assert s["containers"][0]["volumeMounts"][0] == {
        "mountPath": "/usr/share/apm-server/config/certs",
        "name": "elastic-certificates",
    }
    assert s["volumes"][0] == {
        "name": "elastic-certificates",
        "secret": {"secretName": "elastic-certs"},
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
    extraVolume = r["deployment"][name]["spec"]["template"]["spec"]["volumes"]
    assert {"name": "extras", "emptyDir": {}} in extraVolume
    extraVolumeMounts = r["deployment"][name]["spec"]["template"]["spec"]["containers"][
        0
    ]["volumeMounts"]
    assert {
        "name": "extras",
        "mountPath": "/usr/share/extras",
        "readOnly": True,
    } in extraVolumeMounts


def test_adding_pod_labels():
    config = """
labels:
  app.kubernetes.io/name: apm-server
"""
    r = helm_template(config)
    assert (
        r["deployment"][name]["metadata"]["labels"]["app.kubernetes.io/name"]
        == "apm-server"
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


def test_adding_a_node_selector():
    config = """
nodeSelector:
  disktype: ssd
"""
    r = helm_template(config)
    assert (
        r["deployment"][name]["spec"]["template"]["spec"]["nodeSelector"]["disktype"]
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
          - apm-server
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
    spec = r["deployment"][name]["spec"]["template"]["spec"]
    assert "priorityClassName" not in spec

    config = """
priorityClassName: "highest"
"""
    r = helm_template(config)
    priority_class_name = r["deployment"][name]["spec"]["template"]["spec"][
        "priorityClassName"
    ]
    assert priority_class_name == "highest"


def test_setting_fullnameOverride():
    config = """
fullnameOverride: "apm-server-custom"
"""
    r = helm_template(config)

    custom_name = "apm-server-custom"
    assert custom_name in r["deployment"]
    assert custom_name in r["service"]

    assert (
        r["deployment"][custom_name]["spec"]["template"]["spec"]["containers"][0][
            "name"
        ]
        == project
    )
