import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../../helpers'))
from helpers import helm_template
import yaml

name = 'RELEASE-NAME-kibana'
version = '6.6.2'
elasticsearchURL = 'http://elasticsearch-master:9200'


def test_defaults():
    config = '''
    '''

    r = helm_template(config)

    assert name in r['deployment']
    assert name in r['service']

    s = r['service'][name]['spec']
    assert s['ports'][0]['port'] == 5601
    assert s['ports'][0]['name'] == 'http'
    assert s['ports'][0]['protocol'] == 'TCP'

    c = r['deployment'][name]['spec']['template']['spec']['containers'][0]
    assert c['name'] == 'kibana'
    assert c['image'] == 'docker.elastic.co/kibana/kibana:' + version
    assert c['ports'][0]['containerPort'] == 5601

    assert c['env'][0]['name'] == 'ELASTICSEARCH_URL'
    assert c['env'][0]['value'] == elasticsearchURL

    # Empty customizable defaults
    assert 'imagePullSecrets' not in r['deployment'][name]['spec']['template']['spec']
    assert 'tolerations' not in r['deployment'][name]['spec']['template']['spec']
    assert 'nodeSelector' not in r['deployment'][name]['spec']['template']['spec']
    assert 'ingress' not in r

    assert r['deployment'][name]['spec']['strategy']['type'] == 'Recreate'

def test_overriding_the_elasticsearch_hosts():
    config = '''
    elasticsearchHosts: 'http://hello.world'
    '''

    r = helm_template(config)

    c = r['deployment'][name]['spec']['template']['spec']['containers'][0]
    assert c['env'][0]['name'] == 'ELASTICSEARCH_HOSTS'
    assert c['env'][0]['value'] == 'http://hello.world'

def test_overriding_the_elasticsearch_url():
    config = '''
    elasticsearchURL: 'http://hello.world'
    '''

    r = helm_template(config)

    c = r['deployment'][name]['spec']['template']['spec']['containers'][0]
    assert c['env'][0]['name'] == 'ELASTICSEARCH_URL'
    assert c['env'][0]['value'] == 'http://hello.world'


def test_overriding_the_port():
    config = '''
    httpPort: 5602
    '''

    r = helm_template(config)

    c = r['deployment'][name]['spec']['template']['spec']['containers'][0]
    assert c['ports'][0]['containerPort'] == 5602


def test_adding_image_pull_secrets():
    config = '''
imagePullSecrets:
  - name: test-registry
'''
    r = helm_template(config)
    assert r['deployment'][name]['spec']['template']['spec']['imagePullSecrets'][0]['name'] == 'test-registry'


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
    assert r['deployment'][name]['spec']['template']['spec']['tolerations'][0]['key'] == 'key1'


def test_adding_a_node_selector():
    config = '''
nodeSelector:
  disktype: ssd
'''
    r = helm_template(config)
    assert r['deployment'][name]['spec']['template']['spec']['nodeSelector']['disktype'] == 'ssd'


def test_adding_an_affinity_rule():
    config = '''
affinity:
  podAntiAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
    - labelSelector:
        matchExpressions:
        - key: app
          operator: In
          values:
          - kibana
      topologyKey: kubernetes.io/hostname
'''

    r = helm_template(config)
    assert r['deployment'][name]['spec']['template']['spec']['affinity']['podAntiAffinity'][
        'requiredDuringSchedulingIgnoredDuringExecution'][0]['topologyKey'] == 'kubernetes.io/hostname'


def test_adding_an_ingress_rule():
    config = '''
ingress:
  enabled: true
  annotations:
    kubernetes.io/ingress.class: nginx
  path: /
  hosts:
    - kibana.elastic.co
  tls:
  - secretName: elastic-co-wildcard
    hosts:
     - kibana.elastic.co
'''

    r = helm_template(config)
    assert name in r['ingress']
    i = r['ingress'][name]['spec']
    assert i['tls'][0]['hosts'][0] == 'kibana.elastic.co'
    assert i['tls'][0]['secretName'] == 'elastic-co-wildcard'

    assert i['rules'][0]['host'] == 'kibana.elastic.co'
    assert i['rules'][0]['http']['paths'][0]['path'] == '/'
    assert i['rules'][0]['http']['paths'][0]['backend']['serviceName'] == name
    assert i['rules'][0]['http']['paths'][0]['backend']['servicePort'] == 5601

def test_override_the_default_update_strategy():
    config = '''
updateStrategy:
  type: "RollingUpdate"
  rollingUpdate:
    maxUnavailable: 1
    maxSurge: 1
'''

    r = helm_template(config)
    assert r['deployment'][name]['spec']['strategy']['type'] == 'RollingUpdate'
    assert r['deployment'][name]['spec']['strategy']['rollingUpdate']['maxUnavailable'] == 1
    assert r['deployment'][name]['spec']['strategy']['rollingUpdate']['maxSurge'] == 1

def test_using_a_name_override():
    config = '''
nameOverride: overrider
'''

    r = helm_template(config)
    assert 'overrider-kibana' in r['deployment']

def test_setting_a_custom_service_account():
    config = '''
serviceAccount: notdefault
'''
    r = helm_template(config)
    assert r['deployment'][name]['spec']['template']['spec']['serviceAccount'] == 'notdefault'

def test_setting_pod_security_context():
    config = '''
podSecurityContext:
  runAsUser: 1001
  fsGroup: 1002
'''
    r = helm_template(config)
    assert r['deployment'][name]['spec']['template']['spec']['securityContext']['runAsUser'] == 1001
    assert r['deployment'][name]['spec']['template']['spec']['securityContext']['fsGroup'] == 1002

def test_adding_in_kibana_config():
    config = '''
kibanaConfig:
  kibana.yml: |
    key:
      nestedkey: value
    dot.notation: test

  other-config.yml: |
    hello = world
'''
    r = helm_template(config)
    c = r['configmap'][name + '-config']['data']

    assert 'kibana.yml' in c
    assert 'other-config.yml' in c

    assert 'nestedkey: value' in c['kibana.yml']
    assert 'dot.notation: test' in c['kibana.yml']

    assert 'hello = world' in c['other-config.yml']

    d = r['deployment'][name]['spec']['template']['spec']

    assert {'configMap': {'name': name + '-config'}, 'name': 'kibanaconfig'} in d['volumes']
    assert {'mountPath': '/usr/share/kibana/config/kibana.yml', 'name': 'kibanaconfig', 'subPath': 'kibana.yml'} in d['containers'][0]['volumeMounts']
    assert {'mountPath': '/usr/share/kibana/config/other-config.yml', 'name': 'kibanaconfig', 'subPath': 'other-config.yml'} in d['containers'][0]['volumeMounts']

    assert 'configchecksum' in r['deployment'][name]['spec']['template']['metadata']['annotations']

def test_changing_the_protocol():
    config = '''
protocol: https
'''
    r = helm_template(config)
    c = r['deployment'][name]['spec']['template']['spec']['containers'][0]
    assert 'https://' in c['readinessProbe']['exec']['command'][-1]
