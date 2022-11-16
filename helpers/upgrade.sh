#!/usr/bin/env bash
#
# upgrade.sh deploy some Helm chart to a specific released version,
# then upgrade it.
#
# An optional version can be specified for Docker image tag to use for upgrade.
# This is required for main branch because upgrade from Elasticsearch 7.X
# to 8.5.1 doesn't work.
#
set -euo pipefail

TO=""

usage() {
  cat <<-EOF
	USAGE:
	  $0 --chart <chart-name> --release <release-name> --from <version> [--to <docker-image-version>]
	  $0 --help

	OPTIONS:
    --chart <chart-name>
      Name of the Elastic Helm chart to install (ie: elasticsearch)
	  --release <release-name>
	    Name of the Helm release to install (ie: helm-upgrade-elasticsearch)
	  --from <version>
	    Version to use for first install (ie: 7.7.0)
    --to <docker-image-version>
      Version of the Docker images to use for upgrade (ie: 7.10.0)
	EOF
  exit 1
}

while [[ $# -gt 0 ]]
do
  key="$1"

  case $key in
    --help)
      usage
    ;;
    --chart)
      CHART="$2"
      shift 2
    ;;
    --release)
      RELEASE="$2"
      shift 2
    ;;
    --from)
      FROM="$2"
      shift 2
    ;;
    --to)
      TO="--set imageTag=$2"
      shift 2
    ;;
    *)
      log "Unrecognized argument: '$key'"
      usage
    ;;
  esac
done

helm repo add elastic https://helm.elastic.co

# Initial install
printf "Installing %s %s\n" "$RELEASE" "$FROM"
helm upgrade --wait --timeout=1200s --install --version "$FROM" --values values.yaml "$RELEASE" elastic/"$CHART"

# Upgrade
printf "Upgrading %s\n" "$RELEASE"
# shellcheck disable=SC2086
helm upgrade --wait --timeout=1200s --install --set terminationGracePeriod=121 $TO --values values.yaml "$RELEASE" ../../
