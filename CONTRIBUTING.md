# Contributing to the Elastic helm charts

## CLA (Contributor License Agreement)

If you haven't already you will need to sign the [CLA](https://www.elastic.co/contributor-agreement) before your pull request can be reviewed and merged.

## Version bumps

Just like with the rest of the stack, all versions in this helm chart repo are bumped and released at the same time. There is no need to bump the version in your pull request.

## Testing and documentation

When making any changes be sure to also update the following:

* Charts README.md
* The templating tests which can be found in `${CHART}/tests/*.py`. [Example](/elasticsearch/tests/elasticsearch_test.py)
* The integration tests which can be found in `${CHART}/examples/*/test/goss.yaml`. [Example](/elasticsearch/examples/default/test/goss.yaml)

## Adding new features

If you aren't 100% sure that this is a feature that makes sense for everyone. Please open an issue first to discuss with the maintainers before investing a lot of time into it. 
