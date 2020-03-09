import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], "../../helpers"))
from helpers import helm_template
import yaml


name = "release-name-logstash"


def test_defaults():
    config = """
"""

    r = helm_template(config)

    # Statefulset
    assert r["statefulset"][name]["spec"]["replicas"] == 1
    assert r["statefulset"][name]["spec"]["updateStrategy"] == {"type": "RollingUpdate"}
    assert r["statefulset"][name]["spec"]["podManagementPolicy"] == "Parallel"
    assert r["statefulset"][name]["spec"]["template"]["spec"]["affinity"][
        "podAntiAffinity"
    ]["requiredDuringSchedulingIgnoredDuringExecution"][0] == {
        "labelSelector": {
            "matchExpressions": [{"key": "app", "operator": "In", "values": [name]}]
        },
        "topologyKey": "kubernetes.io/hostname",
    }

    # Default environment variables
    env_vars = [
        {"name": "LS_JAVA_OPTS", "value": "-Xmx1g -Xms1g"},
    ]

    c = r["statefulset"][name]["spec"]["template"]["spec"]["containers"][0]
    for env in env_vars:
        assert env in c["env"]

    # Image
    assert c["image"].startswith("docker.elastic.co/logstash/logstash:")
    assert c["imagePullPolicy"] == "IfNotPresent"
    assert c["name"] == "logstash"

    # Ports
    assert c["ports"][0] == {"name": "http", "containerPort": 9600}

    # Health checks
    assert c["livenessProbe"]["failureThreshold"] == 3
    assert c["livenessProbe"]["initialDelaySeconds"] == 300
    assert c["livenessProbe"]["periodSeconds"] == 10
    assert c["livenessProbe"]["successThreshold"] == 1
    assert c["livenessProbe"]["timeoutSeconds"] == 5
    assert "/" in c["livenessProbe"]["httpGet"]["path"]
    assert "http" in c["livenessProbe"]["httpGet"]["port"]

    assert c["readinessProbe"]["failureThreshold"] == 3
    assert c["readinessProbe"]["initialDelaySeconds"] == 60
    assert c["readinessProbe"]["periodSeconds"] == 10
    assert c["readinessProbe"]["successThreshold"] == 3
    assert c["readinessProbe"]["timeoutSeconds"] == 5
    assert "/" in c["readinessProbe"]["httpGet"]["path"]
    assert "http" in c["readinessProbe"]["httpGet"]["port"]

    # Resources
    assert c["resources"] == {
        "requests": {"cpu": "100m", "memory": "1536Mi"},
        "limits": {"cpu": "1000m", "memory": "1536Mi"},
    }

    # Persistence
    assert "volumeClaimTemplates" not in r["statefulset"][name]["spec"]
    assert (
        r["statefulset"][name]["spec"]["template"]["spec"]["containers"][0][
            "volumeMounts"
        ]
        == None
    )

    # Service
    assert "serviceName" not in r["statefulset"][name]["spec"]
    assert "service" not in r

    # Other
    assert r["statefulset"][name]["spec"]["template"]["spec"]["securityContext"] == {
        "fsGroup": 1000,
        "runAsUser": 1000,
    }
    assert (
        r["statefulset"][name]["spec"]["template"]["spec"][
            "terminationGracePeriodSeconds"
        ]
        == 120
    )

    # Pod disruption budget
    assert r["poddisruptionbudget"][name + "-pdb"]["spec"]["maxUnavailable"] == 1

    # Empty customizable defaults
    assert "imagePullSecrets" not in r["statefulset"][name]["spec"]["template"]["spec"]
    assert "tolerations" not in r["statefulset"][name]["spec"]["template"]["spec"]
    assert "nodeSelector" not in r["statefulset"][name]["spec"]["template"]["spec"]


def test_increasing_the_replicas():
    config = """
replicas: 5
"""
    r = helm_template(config)
    assert r["statefulset"][name]["spec"]["replicas"] == 5


def test_disabling_pod_disruption_budget():
    config = """
maxUnavailable: false
"""
    r = helm_template(config)
    assert "poddisruptionbudget" not in r


def test_overriding_the_image_and_tag():
    config = """
image: customImage
imageTag: 6.2.4
"""
    r = helm_template(config)
    assert (
        r["statefulset"][name]["spec"]["template"]["spec"]["containers"][0]["image"]
        == "customImage:6.2.4"
    )


def test_adding_extra_env_vars():
    config = """
extraEnvs:
  - name: hello
    value: world
"""
    r = helm_template(config)
    env = r["statefulset"][name]["spec"]["template"]["spec"]["containers"][0]["env"]
    assert {"name": "hello", "value": "world"} in env


def test_adding_a_extra_volume_with_volume_mount():
    config = """
extraVolumes: |
  - name: extras
    emptyDir: {}
extraVolumeMounts: |
  - name: extras
    mountPath: /usr/share/extras
    readOnly: true
"""
    r = helm_template(config)
    extraVolume = r["statefulset"][name]["spec"]["template"]["spec"]["volumes"]
    assert {"name": "extras", "emptyDir": {}} in extraVolume
    extraVolumeMounts = r["statefulset"][name]["spec"]["template"]["spec"][
        "containers"
    ][0]["volumeMounts"]
    assert {
        "name": "extras",
        "mountPath": "/usr/share/extras",
        "readOnly": True,
    } in extraVolumeMounts


def test_adding_a_extra_container():
    config = """
extraContainers: |
  - name: do-something
    image: busybox
    command: ['do', 'something']
"""
    r = helm_template(config)
    extraContainer = r["statefulset"][name]["spec"]["template"]["spec"]["containers"]
    assert {
        "name": "do-something",
        "image": "busybox",
        "command": ["do", "something"],
    } in extraContainer


def test_adding_a_extra_port():
    config = """
extraPorts:
  - name: foo
    containerPort: 30000
"""
    r = helm_template(config)
    extraPorts = r["statefulset"][name]["spec"]["template"]["spec"]["containers"][0][
        "ports"
    ]
    assert {"name": "foo", "containerPort": 30000,} in extraPorts


def test_adding_a_extra_init_container():
    config = """
extraInitContainers: |
  - name: do-something
    image: busybox
    command: ['do', 'something']
"""
    r = helm_template(config)
    extraInitContainer = r["statefulset"][name]["spec"]["template"]["spec"][
        "initContainers"
    ]
    assert {
        "name": "do-something",
        "image": "busybox",
        "command": ["do", "something"],
    } in extraInitContainer


def test_adding_persistence():
    config = """
persistence:
  enabled: true
"""
    r = helm_template(config)
    c = r["statefulset"][name]["spec"]["template"]["spec"]["containers"][0]
    assert c["volumeMounts"][0]["mountPath"] == "/usr/share/logstash/data"
    assert c["volumeMounts"][0]["name"] == name

    v = r["statefulset"]["release-name-logstash"]["spec"]["volumeClaimTemplates"][0]
    assert v["metadata"]["name"] == name
    assert v["spec"]["accessModes"] == ["ReadWriteOnce"]
    assert v["spec"]["resources"]["requests"]["storage"] == "1Gi"


def test_adding_storageclass_annotation_to_volumeclaimtemplate():
    config = """
persistence:
  enabled: true
  annotations:
    volume.beta.kubernetes.io/storage-class: id
"""
    r = helm_template(config)
    annotations = r["statefulset"][name]["spec"]["volumeClaimTemplates"][0]["metadata"][
        "annotations"
    ]
    assert annotations["volume.beta.kubernetes.io/storage-class"] == "id"


def test_adding_multiple_persistence_annotations():
    config = """
    persistence:
      enabled: true
      annotations:
        hello: world
        world: hello
"""
    r = helm_template(config)
    annotations = r["statefulset"][name]["spec"]["volumeClaimTemplates"][0]["metadata"][
        "annotations"
    ]

    assert annotations["hello"] == "world"
    assert annotations["world"] == "hello"


def test_adding_a_secret_mount():
    config = """
secretMounts:
  - name: elastic-certificates
    secretName: elastic-certs
    path: /usr/share/logstash/config/certs
"""
    r = helm_template(config)
    s = r["statefulset"][name]["spec"]["template"]["spec"]
    assert s["containers"][0]["volumeMounts"][-1] == {
        "mountPath": "/usr/share/logstash/config/certs",
        "name": "elastic-certificates",
    }
    assert s["volumes"] == [
        {"name": "elastic-certificates", "secret": {"secretName": "elastic-certs"}}
    ]


def test_adding_a_secret_mount_with_subpath():
    config = """
secretMounts:
  - name: elastic-certificates
    secretName: elastic-certs
    path: /usr/share/logstash/config/certs
    subPath: cert.crt
"""
    r = helm_template(config)
    s = r["statefulset"][name]["spec"]["template"]["spec"]
    assert s["containers"][0]["volumeMounts"][-1] == {
        "mountPath": "/usr/share/logstash/config/certs",
        "subPath": "cert.crt",
        "name": "elastic-certificates",
    }


def test_adding_image_pull_secrets():
    config = """
imagePullSecrets:
  - name: test-registry
"""
    r = helm_template(config)
    assert (
        r["statefulset"][name]["spec"]["template"]["spec"]["imagePullSecrets"][0][
            "name"
        ]
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
        r["statefulset"][name]["spec"]["template"]["spec"]["tolerations"][0]["key"]
        == "key1"
    )


def test_adding_pod_annotations():
    config = """
podAnnotations:
  iam.amazonaws.com/role: logstash-role
"""
    r = helm_template(config)
    assert (
        r["statefulset"][name]["spec"]["template"]["metadata"]["annotations"][
            "iam.amazonaws.com/role"
        ]
        == "logstash-role"
    )


def test_adding_a_node_selector():
    config = """
nodeSelector:
  disktype: ssd
"""
    r = helm_template(config)
    assert (
        r["statefulset"][name]["spec"]["template"]["spec"]["nodeSelector"]["disktype"]
        == "ssd"
    )


def test_adding_a_node_affinity():
    config = """
nodeAffinity:
  preferredDuringSchedulingIgnoredDuringExecution:
  - weight: 100
    preference:
      matchExpressions:
      - key: mylabel
        operator: In
        values:
        - myvalue
"""
    r = helm_template(config)
    assert r["statefulset"]["release-name-logstash"]["spec"]["template"]["spec"][
        "affinity"
    ]["nodeAffinity"] == {
        "preferredDuringSchedulingIgnoredDuringExecution": [
            {
                "weight": 100,
                "preference": {
                    "matchExpressions": [
                        {"key": "mylabel", "operator": "In", "values": ["myvalue"]}
                    ]
                },
            }
        ]
    }


def test_adding_in_logstash_config():
    config = """
logstashConfig:
  logstash.yml: |
    key:
      nestedkey: value
    dot.notation: test

  log4j2.properties: |
    appender.rolling.name = rolling
"""
    r = helm_template(config)
    c = r["configmap"][name + "-config"]["data"]

    assert "logstash.yml" in c
    assert "log4j2.properties" in c

    assert "nestedkey: value" in c["logstash.yml"]
    assert "dot.notation: test" in c["logstash.yml"]

    assert "appender.rolling.name = rolling" in c["log4j2.properties"]

    s = r["statefulset"][name]["spec"]["template"]["spec"]

    assert {
        "configMap": {"name": "release-name-logstash-config"},
        "name": "logstashconfig",
    } in s["volumes"]
    assert {
        "mountPath": "/usr/share/logstash/config/logstash.yml",
        "name": "logstashconfig",
        "subPath": "logstash.yml",
    } in s["containers"][0]["volumeMounts"]
    assert {
        "mountPath": "/usr/share/logstash/config/log4j2.properties",
        "name": "logstashconfig",
        "subPath": "log4j2.properties",
    } in s["containers"][0]["volumeMounts"]

    assert (
        "configchecksum"
        in r["statefulset"][name]["spec"]["template"]["metadata"]["annotations"]
    )


def test_adding_in_pipeline():
    config = """
logstashPipeline:
  uptime.conf: |
    input { stdin { } } }
    output { stdout { { } } }
"""
    r = helm_template(config)
    c = r["configmap"][name + "-pipeline"]["data"]

    assert "uptime.conf" in c

    assert "input { stdin { } } }" in c["uptime.conf"]
    assert "output { stdout { { } } }" in c["uptime.conf"]

    assert (
        "pipelinechecksum"
        in r["statefulset"][name]["spec"]["template"]["metadata"]["annotations"]
    )


def test_priority_class_name():
    config = """
priorityClassName: ""
"""
    r = helm_template(config)
    spec = r["statefulset"][name]["spec"]["template"]["spec"]
    assert "priorityClassName" not in spec

    config = """
priorityClassName: "highest"
"""
    r = helm_template(config)
    priority_class_name = r["statefulset"][name]["spec"]["template"]["spec"][
        "priorityClassName"
    ]
    assert priority_class_name == "highest"


def test_scheduler_name():
    r = helm_template("")
    spec = r["statefulset"][name]["spec"]["template"]["spec"]
    assert "schedulerName" not in spec

    config = """
schedulerName: "stork"
"""
    r = helm_template(config)
    assert (
        r["statefulset"][name]["spec"]["template"]["spec"]["schedulerName"] == "stork"
    )


def test_lifecycle_hooks():
    config = ""
    r = helm_template(config)
    c = r["statefulset"][name]["spec"]["template"]["spec"]["containers"][0]
    assert "lifecycle" not in c

    config = """
    lifecycle:
      preStop:
        exec:
          command: ["/bin/bash","/preStop"]
    """
    r = helm_template(config)
    c = r["statefulset"][name]["spec"]["template"]["spec"]["containers"][0]

    assert c["lifecycle"]["preStop"]["exec"]["command"] == ["/bin/bash", "/preStop"]


def test_set_pod_security_context():
    config = ""
    r = helm_template(config)
    assert (
        r["statefulset"][name]["spec"]["template"]["spec"]["securityContext"]["fsGroup"]
        == 1000
    )
    assert (
        r["statefulset"][name]["spec"]["template"]["spec"]["securityContext"][
            "runAsUser"
        ]
        == 1000
    )

    config = """
    podSecurityContext:
      fsGroup: 1001
      other: test
    """

    r = helm_template(config)

    assert (
        r["statefulset"][name]["spec"]["template"]["spec"]["securityContext"]["fsGroup"]
        == 1001
    )
    assert (
        r["statefulset"][name]["spec"]["template"]["spec"]["securityContext"]["other"]
        == "test"
    )


def test_set_container_security_context():
    config = ""

    r = helm_template(config)
    c = r["statefulset"][name]["spec"]["template"]["spec"]["containers"][0]
    assert c["securityContext"]["capabilities"]["drop"] == ["ALL"]
    assert c["securityContext"]["runAsNonRoot"] == True
    assert c["securityContext"]["runAsUser"] == 1000

    config = """
    securityContext:
      runAsUser: 1001
      other: test
"""

    r = helm_template(config)
    c = r["statefulset"][name]["spec"]["template"]["spec"]["containers"][0]
    assert c["securityContext"]["capabilities"]["drop"] == ["ALL"]
    assert c["securityContext"]["runAsNonRoot"] == True
    assert c["securityContext"]["runAsUser"] == 1001
    assert c["securityContext"]["other"] == "test"


def test_adding_pod_labels():
    config = """
labels:
  app.kubernetes.io/name: logstash
"""
    r = helm_template(config)
    assert (
        r["statefulset"][name]["metadata"]["labels"]["app.kubernetes.io/name"]
        == "logstash"
    )
    assert (
        r["statefulset"][name]["spec"]["template"]["metadata"]["labels"][
            "app.kubernetes.io/name"
        ]
        == "logstash"
    )


def test_pod_security_policy():
    ## Make sure the default config is not creating any resources
    config = ""
    resources = ("role", "rolebinding", "serviceaccount", "podsecuritypolicy")
    r = helm_template(config)
    for resource in resources:
        assert resource not in r
    assert (
        "serviceAccountName" not in r["statefulset"][name]["spec"]["template"]["spec"]
    )

    ## Make sure all the resources are created with default values
    config = """
rbac:
  create: true
  serviceAccountName: ""

podSecurityPolicy:
  create: true
  name: ""
"""
    r = helm_template(config)
    for resource in resources:
        assert resource in r
    assert r["role"][name]["rules"][0] == {
        "apiGroups": ["extensions"],
        "verbs": ["use"],
        "resources": ["podsecuritypolicies"],
        "resourceNames": [name],
    }
    assert r["rolebinding"][name]["subjects"] == [
        {"kind": "ServiceAccount", "namespace": "default", "name": name}
    ]
    assert r["rolebinding"][name]["roleRef"] == {
        "apiGroup": "rbac.authorization.k8s.io",
        "kind": "Role",
        "name": name,
    }
    assert (
        r["statefulset"][name]["spec"]["template"]["spec"]["serviceAccountName"] == name
    )
    psp_spec = r["podsecuritypolicy"][name]["spec"]
    assert psp_spec["privileged"] is True


def test_external_pod_security_policy():
    ## Make sure we can use an externally defined pod security policy
    config = """
rbac:
  create: true
  serviceAccountName: ""

podSecurityPolicy:
  create: false
  name: "customPodSecurityPolicy"
"""
    resources = ("role", "rolebinding")
    r = helm_template(config)
    for resource in resources:
        assert resource in r

    assert r["role"][name]["rules"][0] == {
        "apiGroups": ["extensions"],
        "verbs": ["use"],
        "resources": ["podsecuritypolicies"],
        "resourceNames": ["customPodSecurityPolicy"],
    }


def test_external_service_account():
    ## Make sure we can use an externally defined service account
    config = """
rbac:
  create: false
  serviceAccountName: "customServiceAccountName"

podSecurityPolicy:
  create: false
  name: ""
"""
    resources = ("role", "rolebinding", "serviceaccount")
    r = helm_template(config)

    assert (
        r["statefulset"][name]["spec"]["template"]["spec"]["serviceAccountName"]
        == "customServiceAccountName"
    )
    # When referencing an external service account we do not want any resources to be created.
    for resource in resources:
        assert resource not in r


def test_adding_a_service():
    config = """
service:
  annotations: {}
  type: ClusterIP
  ports:
    - name: beats
      port: 5044
      protocol: TCP
      targetPort: 5044
"""
    r = helm_template(config)
    s = r["service"][name]
    assert s["metadata"]["name"] == name
    assert s["metadata"]["annotations"] == {}
    assert s["spec"]["type"] == "ClusterIP"
    assert len(s["spec"]["ports"]) == 1
    assert s["spec"]["ports"][0] == {
        "name": "beats",
        "port": 5044,
        "protocol": "TCP",
        "targetPort": 5044,
    }


def test_setting_fullnameOverride():
    config = """
fullnameOverride: 'logstash-custom'
"""
    r = helm_template(config)

    custom_name = "logstash-custom"
    assert custom_name in r["statefulset"]
    assert (
        r["statefulset"][custom_name]["spec"]["template"]["spec"]["containers"][0][
            "name"
        ]
        == "logstash"
    )
