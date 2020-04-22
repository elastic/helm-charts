# Contributing to the Elastic helm charts

## Requirements for submiting a pull request

Before submitting a pull request make sure you validated the following
requirements:

* CLA should be signed (see [CLA section][] for more details).

* Charts version shouldn't be bumped (see [Releases section][] for more
details).

* Charts `README.md` should be updated if required (especially updating default
values if they have been changed).

* Templating tests should be added/updated (see [Templating tests section][] for
more details).

* Integration tests should be added/updated (see [Integration tests section][]
for more details).

## CLA (Contributor License Agreement)

If you haven't already you will need to sign the [CLA][] before your pull
request can be reviewed and merged.

## Branches workflow

Pull request are merged on `master` branch, then they should be backported to
version branches (example `7.7` branch).

>TODO: add more details about version branching.

## Releases

Just like with the rest of the stack, all versions in this helm chart repo are
bumped and released at the same time. There is no need to bump the version in
your pull request.

Charts are released from version branchs (example `7.7` branch).

[Elastic Helm repository][] is updated only during releases.

>TODO: add more details about releases (see also [release.md][]).

## Testing

### Templating tests

Templating tests which can be found in `${CHART}/tests/*.py`
([Example][templating test example]).

These charts use [pytest][] to test the templating logic. The dependencies for
testing can be installed from the [requirements.txt][] in the parent directory:

```
pip install -r ./requirements.txt
```

Tests can then be run from each chart directory using `make pytest`

You can also use `make template` (equivalent to `helm template` ) to look at the
YAML being generated:

It is possible to run all of the tests and linting inside of a Docker container
using `make test`

Note that templating tests are formated using [Black][], you should run
`make lint-python` (equivalent to `black --diff --check .` ) to validate them or
`black .` to apply formatting before submitting a pull request which will modify
them.

### Integration tests

Integration tests which can be found in `${CHART}/examples/*/test/goss.yaml`
([Example][integration test example]).

Integration tests are run using [goss][] which is a [Serverspec][] like tool
written in golang. See [integration test example][] for an example of what the
tests look like.

The different integration tests are present in each chart's `examples`
directory.

Each charts contains an `examples/default` integration test which validate the
chart deployment with default values.

`examples` directory contains also integration tests for other use cases (for
example: using `oss` Docker images, using `6.x` version or using `security` ).

Every directory which contains some `test` subdirectory is an integration test
(`examples` directory contains also some configuration examples for some
specific scenarios without tests like configuration for specific k8s providers).

To run the goss tests against the default example:

```
cd examples/default
make goss
```

## Adding new features

If you aren't 100% sure that this is a feature that makes sense for everyone.
Please open an issue first to discuss with the maintainers before investing a
lot of time into it.

[black]: https://black.readthedocs.io/en/stable/
[cla]: https://www.elastic.co/contributor-agreement
[cla section]: #cla-contributor-license-agreement
[elastic helm repository]: https://helm.elastic.co
[goss]: https://github.com/aelsabbahy/goss/blob/master/docs/manual.md
[integration test example]: https://github.com/elastic/helm-charts/blob/master/elasticsearch/examples/default/test/goss.yaml
[integration tests section]: #integration-tests
[pytest]: https://docs.pytest.org/en/latest/
[serverspec]: https://serverspec.org
[templating test example]: https://github.com/elastic/helm-charts/blob/master/elasticsearch/tests/elasticsearch_test.py
[templating tests section]: #templating-tests
[release.md]: https://github.com/elastic/helm-charts/blob/master/helpers/release.md
[releases section]: #releases
[requirements.txt]: https://github.com/elastic/helm-charts/blob/master/requirements.txt