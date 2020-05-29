#!/usr/bin/env bash

set -exo pipefail

usage() {
  cat <<-EOF
	USAGE:
	  $0 [--release <release-name>] [--from <elasticsearch-version>] --to <elasticsearch-version>
	  $0 --help

	OPTIONS:
    --release <release-name>
	    Name of the Helm release to install
	  --from <elasticsearch-version>
	    Elasticsearch version to use for first install
	EOF
  exit 1
}

RELEASE="helm-es-upgrade"
FROM=""

while [[ $# -gt 0 ]]
do
  key="$1"

  case $key in
    --help)
      usage
    ;;
    --release)
      RELEASE="$2"
      shift 2
    ;;
    --from)
      FROM="$2"
      shift 2
    ;;
    *)
      log "Unrecognized argument: '$key'"
      usage
    ;;
  esac
done

# Elasticsearch chart < 7.4.0 are not compatible with K8S >= 1.16)
if [[ -z $FROM ]]
then
  KUBE_MINOR_VERSION=$(kubectl version --client -o yaml | grep minor | sed 's/[^0-9]*//g')

  if [ "$KUBE_MINOR_VERSION" -lt 16 ]
  then
    FROM="7.0.0-alpha1"
  else
    FROM="7.4.0"
  fi
fi

helm repo add elastic https://helm.elastic.co

# Initial install
helm upgrade --wait --timeout=600 --install "$RELEASE" elastic/elasticsearch --version "$FROM" --set clusterName=upgrade -f ../docker-for-mac/values.yaml
kubectl rollout status sts/upgrade-master --timeout=600s

# Upgrade
helm upgrade --wait --timeout=600 --set terminationGracePeriod=121 --install "$RELEASE" ../../ --set clusterName=upgrade -f ../docker-for-mac/values.yaml
kubectl rollout status sts/upgrade-master --timeout=600s
