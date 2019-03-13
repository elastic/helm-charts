import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../helpers'))
from helpers import helm_template
import yaml

clusterName = 'elasticsearch'
nodeGroup = 'master'
uname = clusterName + '-' + nodeGroup


def test_defaults():
    config = '''
    '''

    r = helm_template(config)

    # Statefulset
    assert r['statefulset'][uname]['spec']['replicas'] == 3
    assert r['statefulset'][uname]['spec']['updateStrategy'] == {
        'type': 'RollingUpdate'}
    assert r['statefulset'][uname]['spec']['podManagementPolicy'] == 'Parallel'
    assert r['statefulset'][uname]['spec']['serviceName'] == uname + '-headless'
    assert r['statefulset'][uname]['spec']['template']['spec']['affinity']['podAntiAffinity']['requiredDuringSchedulingIgnoredDuringExecution'][0] == \
        {
            "labelSelector": {
                "matchExpressions": [
                    {
                        "key": "app",
                        "operator": "In",
                        "values": [
                            uname
                        ]
                    }
                ]
            },
            "topologyKey": "kubernetes.io/hostname"
    }

    # Default environment variables
    env_vars = [
        {
            'name': 'node.name',
            'valueFrom': {
                'fieldRef': {
                    'fieldPath': 'metadata.name'
                }
            }
        },
        {
            'name': 'discovery.zen.minimum_master_nodes',
            'value': '2'
        },
        {
            'name': 'discovery.zen.ping.unicast.hosts',
            'value': uname + '-headless'

        },
        {
            'name': 'network.host',
            'value': '0.0.0.0'
        },
        {
            'name': 'cluster.name',
            'value': clusterName
        },
        {
            'name': 'ES_JAVA_OPTS',
            'value': '-Xmx1g -Xms1g'
        },
        {
            'name': 'node.master',
            'value': 'true'
        },
        {
            'name': 'node.data',
            'value': 'true'
        },
        {
            'name': 'node.ingest',
            'value': 'true'
        },
    ]

    c = r['statefulset'][uname]['spec']['template']['spec']['containers'][0]
    for env in env_vars:
        assert env in c['env']

    # Image
    assert c['image'].startswith(
        'docker.elastic.co/elasticsearch/elasticsearch:')
    assert c['imagePullPolicy'] == 'IfNotPresent'
    assert c['name'] == 'elasticsearch'

    # Ports
    assert c['ports'][0] == {'name': 'http', 'containerPort': 9200}
    assert c['ports'][1] == {'name': 'transport', 'containerPort': 9300}

    # Health checks
    assert c['readinessProbe']['failureThreshold'] == 3
    assert c['readinessProbe']['initialDelaySeconds'] == 10
    assert c['readinessProbe']['periodSeconds'] == 10
    assert c['readinessProbe']['successThreshold'] == 3
    assert c['readinessProbe']['timeoutSeconds'] == 5

    assert 'curl' in c['readinessProbe']['exec']['command'][-1]
    assert 'http://127.0.0.1:9200' in c['readinessProbe']['exec']['command'][-1]

    # Resources
    assert c['resources'] == {
        'requests': {
            'cpu': '100m',
            'memory': '2Gi'
        },
        'limits': {
            'cpu': '1000m',
            'memory': '2Gi'
        }
    }

    # Mounts
    assert c['volumeMounts'][0]['mountPath'] == '/usr/share/elasticsearch/data'
    assert c['volumeMounts'][0]['name'] == uname

    v = r['statefulset'][uname]['spec']['volumeClaimTemplates'][0]
    assert v['metadata']['name'] == uname
    assert v['spec']['accessModes'] == ['ReadWriteOnce']
    assert v['spec']['resources']['requests']['storage'] == '30Gi'
    assert v['spec']['storageClassName'] == 'standard'

    # Init container
    i = r['statefulset'][uname]['spec']['template']['spec']['initContainers'][0]
    assert i['name'] == 'configure-sysctl'
    assert i['command'] == ['sysctl', '-w', 'vm.max_map_count=262144']
    assert i['image'].startswith(
        'docker.elastic.co/elasticsearch/elasticsearch:')
    assert i['securityContext'] == {
        'privileged': True,
        'runAsUser': 0
    }

    # Other
    assert r['statefulset'][uname]['spec']['template']['spec']['securityContext'] == {
        'fsGroup': 1000}
    assert r['statefulset'][uname]['spec']['template']['spec']['terminationGracePeriodSeconds'] == 120

    # Pod disruption budget
    assert r['poddisruptionbudget'][uname +
                                    '-pdb']['spec']['maxUnavailable'] == 1

    # Service
    s = r['service'][uname]
    assert s['metadata']['name'] == uname
    assert len(s['spec']['ports']) == 2
    assert s['spec']['ports'][0] == {
        'name': 'http', 'port': 9200, 'protocol': 'TCP'}
    assert s['spec']['ports'][1] == {
        'name': 'transport', 'port': 9300, 'protocol': 'TCP'}

    # Headless Service
    h = r['service'][uname + '-headless']
    assert h['spec']['clusterIP'] == 'None'
    assert h['spec']['ports'][0]['name'] == 'http'
    assert h['spec']['ports'][0]['port'] == 9200
    assert h['spec']['ports'][1]['name'] == 'transport'
    assert h['spec']['ports'][1]['port'] == 9300

    # Empty customizable defaults
    assert 'imagePullSecrets' not in r['statefulset'][uname]['spec']['template']['spec']
    assert 'tolerations' not in r['statefulset'][uname]['spec']['template']['spec']
    assert 'nodeSelector' not in r['statefulset'][uname]['spec']['template']['spec']
    assert 'ingress' not in r


def test_increasing_the_replicas():
    config = '''
replicas: 5
'''
    r = helm_template(config)
    assert r['statefulset'][uname]['spec']['replicas'] == 5


def test_disabling_pod_disruption_budget():
    config = '''
maxUnavailable: false
'''
    r = helm_template(config)
    assert 'poddisruptionbudget' not in r


def test_overriding_the_image_and_tag():
    config = '''
image: customImage
imageTag: 6.2.4
'''
    r = helm_template(config)
    assert r['statefulset'][uname]['spec']['template']['spec']['containers'][0]['image'] == 'customImage:6.2.4'


def test_set_discovery_hosts_to_custom_master_service():
    config = '''
masterService: "elasticsearch-custommaster"
'''
    r = helm_template(config)
    env = r['statefulset'][uname]['spec']['template']['spec']['containers'][0]['env']
    assert {'name': 'discovery.zen.ping.unicast.hosts',
            'value': 'elasticsearch-custommaster-headless'} in env

def test_set_master_service_to_default_nodegroup_name_if_not_set():
    config = '''
nodeGroup: "data"
'''
    r = helm_template(config)
    env = r['statefulset']['elasticsearch-data']['spec']['template']['spec']['containers'][0]['env']
    assert {'name': 'discovery.zen.ping.unicast.hosts',
            'value': 'elasticsearch-master-headless'} in env

def test_set_master_service_to_default_nodegroup_name_with_custom_cluster_name():
    config = '''
clusterName: "custom"
nodeGroup: "data"
'''
    r = helm_template(config)
    env = r['statefulset']['custom-data']['spec']['template']['spec']['containers'][0]['env']
    assert {'name': 'discovery.zen.ping.unicast.hosts',
            'value': 'custom-master-headless'} in env


def test_set_initial_master_nodes_when_using_v_7():
    config = '''
esMajorVersion: 7
roles:
  master: "true"
'''
    r = helm_template(config)
    env = r['statefulset'][uname]['spec']['template']['spec']['containers'][0]['env']
    assert {
            'name': 'cluster.initial_master_nodes',
            'value': 'elasticsearch-master-0,' +
                     'elasticsearch-master-1,' +
                     'elasticsearch-master-2,'
        } in env

    for e in env:
        assert e['name'] != 'discovery.zen.minimum_master_nodes'

def test_dont_set_initial_master_nodes_if_not_master_when_using_es_version_7():
    config = '''
esMajorVersion: 7
roles:
  master: "false"
'''
    r = helm_template(config)
    env = r['statefulset'][uname]['spec']['template']['spec']['containers'][0]['env']
    for e in env:
        assert e['name'] != 'cluster.initial_master_nodes'

def test_enabling_machine_learning_role():
    config = '''
roles:
  ml: "true"
'''
    r = helm_template(config)
    env = r['statefulset'][uname]['spec']['template']['spec']['containers'][0]['env']

    assert {'name': 'node.ml',
            'value': 'true'} in env


def test_adding_extra_env_vars():
    config = '''
extraEnvs:
  - name: hello
    value: world
'''
    r = helm_template(config)
    env = r['statefulset'][uname]['spec']['template']['spec']['containers'][0]['env']
    assert {'name': 'hello', 'value': 'world'} in env


def test_adding_a_secret_mount():
    config = '''
secretMounts:
  - name: elastic-certificates
    secretName: elastic-certificates
    path: /usr/share/elasticsearch/config/certs
'''
    r = helm_template(config)
    s = r['statefulset'][uname]['spec']['template']['spec']
    assert s['containers'][0]['volumeMounts'][-1] == {
        'mountPath': '/usr/share/elasticsearch/config/certs',
        'name': 'elastic-certificates'
    }
    assert s['volumes'] == [{
        'name': 'elastic-certificates',
        'secret': {
            'secretName': 'elastic-certificates'
        }
    }]


def test_adding_a_secret_mount_with_subpath():
    config = '''
secretMounts:
  - name: elastic-certificates
    secretName: elastic-certificates
    path: /usr/share/elasticsearch/config/certs
    subPath: cert.crt
'''
    r = helm_template(config)
    s = r['statefulset'][uname]['spec']['template']['spec']
    assert s['containers'][0]['volumeMounts'][-1] == {
        'mountPath': '/usr/share/elasticsearch/config/certs',
        'subPath': 'cert.crt',
        'name': 'elastic-certificates'
    }


def test_adding_image_pull_secrets():
    config = '''
imagePullSecrets:
  - name: test-registry
'''
    r = helm_template(config)
    assert r['statefulset'][uname]['spec']['template']['spec']['imagePullSecrets'][0]['name'] == 'test-registry'


def test_adding_tolerations():
    config = '''
tolerations:
- key: "key1"
  operator: "Equal"
  value: "value1"
  effect: "NoExecute"
  tolerationSeconds: 3600
'''
    r = helm_template(config)
    assert r['statefulset'][uname]['spec']['template']['spec']['tolerations'][0]['key'] == 'key1'

def test_adding_pod_annotations():
    config = '''
podAnnotations:
  iam.amazonaws.com/role: es-role
'''
    r = helm_template(config)
    assert r['statefulset'][uname]['spec']['template']['metadata']['annotations']['iam.amazonaws.com/role'] == 'es-role'


def test_adding_a_node_selector():
    config = '''
nodeSelector:
  disktype: ssd
'''
    r = helm_template(config)
    assert r['statefulset'][uname]['spec']['template']['spec']['nodeSelector']['disktype'] == 'ssd'

def test_adding_resources_to_initcontainer():
    config = '''
initResources:
  limits:
    cpu: "25m"
    memory: "128Mi"
  requests:
    cpu: "25m"
    memory: "128Mi"
'''
    r = helm_template(config)
    i = r['statefulset'][uname]['spec']['template']['spec']['initContainers'][0]

    assert i['resources'] == {
        'requests': {
            'cpu': '25m',
            'memory': '128Mi'
        },
        'limits': {
            'cpu': '25m',
            'memory': '128Mi'
        }
    }

def test_adding_a_node_affinity():
    config = '''
nodeAffinity:
  preferredDuringSchedulingIgnoredDuringExecution:
  - weight: 100
    preference:
      matchExpressions:
      - key: mylabel
        operator: In
        values:
        - myvalue
'''
    r = helm_template(config)
    assert r['statefulset'][uname]['spec']['template']['spec']['affinity']['nodeAffinity'] == {
        'preferredDuringSchedulingIgnoredDuringExecution': [{
            'weight': 100,
            'preference': {
                'matchExpressions': [{
                    'key': 'mylabel',
                    'operator': 'In',
                    'values': [
                        'myvalue'
                    ]
                }]
            }
        }]
    }


def test_adding_an_ingress_rule():
    config = '''
ingress:
  enabled: true
  annotations:
    kubernetes.io/ingress.class: nginx
  path: /
  hosts:
    - elasticsearch.elastic.co
  tls:
  - secretName: elastic-co-wildcard
    hosts:
     - elasticsearch.elastic.co
'''

    r = helm_template(config)
    assert uname in r['ingress']
    i = r['ingress'][uname]['spec']
    assert i['tls'][0]['hosts'][0] == 'elasticsearch.elastic.co'
    assert i['tls'][0]['secretName'] == 'elastic-co-wildcard'

    assert i['rules'][0]['host'] == 'elasticsearch.elastic.co'
    assert i['rules'][0]['http']['paths'][0]['path'] == '/'
    assert i['rules'][0]['http']['paths'][0]['backend']['serviceName'] == uname
    assert i['rules'][0]['http']['paths'][0]['backend']['servicePort'] == 9200


def test_changing_the_protocol():
    config = '''
protocol: https
'''
    r = helm_template(config)
    c = r['statefulset'][uname]['spec']['template']['spec']['containers'][0]
    assert 'https://127.0.0.1:9200' in c['readinessProbe']['exec']['command'][-1]

def test_changing_the_cluster_health_status():
    config = '''
clusterHealthCheckParams: 'wait_for_no_initializing_shards=true&timeout=60s'
'''
    r = helm_template(config)
    c = r['statefulset'][uname]['spec']['template']['spec']['containers'][0]
    assert '/_cluster/health?wait_for_no_initializing_shards=true&timeout=60s' in c['readinessProbe']['exec']['command'][-1]

def test_adding_in_es_config():
    config = '''
esConfig:
  elasticsearch.yml: |
    key:
      nestedkey: value
    dot.notation: test

  log4j2.properties: |
    appender.rolling.name = rolling
'''
    r = helm_template(config)
    c = r['configmap'][uname + '-config']['data']

    assert 'elasticsearch.yml' in c
    assert 'log4j2.properties' in c

    assert 'nestedkey: value' in c['elasticsearch.yml']
    assert 'dot.notation: test' in c['elasticsearch.yml']

    assert 'appender.rolling.name = rolling' in c['log4j2.properties']

    s = r['statefulset'][uname]['spec']['template']['spec']

    assert {'configMap': {'name': 'elasticsearch-master-config'}, 'name': 'esconfig'} in s['volumes']
    assert {'mountPath': '/usr/share/elasticsearch/config/elasticsearch.yml', 'name': 'esconfig', 'subPath': 'elasticsearch.yml'} in s['containers'][0]['volumeMounts']
    assert {'mountPath': '/usr/share/elasticsearch/config/log4j2.properties', 'name': 'esconfig', 'subPath': 'log4j2.properties'} in s['containers'][0]['volumeMounts']

    assert 'configchecksum' in r['statefulset'][uname]['spec']['template']['metadata']['annotations']
