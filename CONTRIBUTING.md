# Contributing to the Elastic Helm charts
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Adding new features](#adding-new-features)
- [Requirements for submiting a pull request](#requirements-for-submiting-a-pull-request)
- [CLA (Contributor License Agreement)](#cla-contributor-license-agreement)
- [How We Use Git and GitHub](#how-we-use-git-and-github)
  - [Forking](#forking)
  - [Branching](#branching)
  - [Commits and Merging](#commits-and-merging)
    - [Rebasing and fixing merge conflicts](#rebasing-and-fixing-merge-conflicts)
  - [What Goes Into a Pull Request](#what-goes-into-a-pull-request)
- [Submitting a Pull Request](#submitting-a-pull-request)
- [Releases](#releases)
- [Testing](#testing)
  - [Templating tests](#templating-tests)
  - [Integration tests](#integration-tests)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!-- Use this to update TOC: -->
<!-- docker run --rm -it -v $(pwd):/usr/src jorgeandrada/doctoc --github -->


## Adding new features

If you aren't 100% sure that this is a feature that makes sense for everyone.
Please open an issue first to discuss with the maintainers before investing a
lot of time into it.


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

Please make sure you have signed our [Contributor License Agreement][]. We are
not asking you to assign copyright to us, but to give us the right to distribute
your code without restriction. We ask this of all contributors in order to
assure our users of the origin and continuing existence of the code.
You only need to sign the CLA once.


## How We Use Git and GitHub

### Forking

We follow the [GitHub forking model][] for collaborating on Helm charts code.
This model assumes that you have a remote called `upstream` which points to the
official helm-charts repo, which we'll refer to in later code snippets.

### Branching

* All work on the next major release (`8.0.0`) goes into main.
* Past major release branches are named `{majorVersion}.x`. They contain work
that will go into the next minor release. For example, if the next minor release
is `7.8.0`, work for it should go into the `7.x` branch.
* Past minor release branches are named `{majorVersion}.{minorVersion}`. They
contain work that will go into the next patch release. For example, if the next
patch release is `7.7.1`, work for it should go into the `7.7` branch.
* All work is done on feature branches and merged into one of these branches.
* Where appropriate, we'll backport changes into older release branches.

### Commits and Merging

* Feel free to make as many commits as you want, while working on a branch.
* Please use your commit messages to include helpful information on your
changes and an explanation of *why* you made the changes that you did.
* Resolve merge conflicts by rebasing the target branch over your feature
branch, and force-pushing (see below for instructions).
* When merging, we'll squash your commits into a single commit.

#### Rebasing and fixing merge conflicts

Rebasing can be tricky, and fixing merge conflicts can be even trickier because
it involves force pushing. This is all compounded by the fact that attempting to
push a rebased branch remotely will be rejected by git, and you'll be prompted
to do a `pull`, which is not at all what you should do (this will really mess up
your branch's history).

Here's how you should rebase main onto your branch, and how to fix merge
conflicts when they arise.

First, make sure main is up-to-date.

```shell
git checkout main
git fetch upstream
git rebase upstream/main
```

Then, check out your branch and rebase main on top of it, which will apply all
of the new commits on main to your branch, and then apply all of your branch's
new commits after that.

```shell
git checkout name-of-your-branch
git rebase main
```

You want to make sure there are no merge conflicts. If there are merge
conflicts, git will pause the rebase and allow you to fix the conflicts before
continuing.

You can use `git status` to see which files contain conflicts. They'll be the
ones that aren't staged for commit. Open those files, and look for where git has
marked the conflicts. Resolve the conflicts so that the changes you want to make
to the code have been incorporated in a way that doesn't destroy work that's
been done in main. Refer to main's commit history on GitHub if you need to
gain a better understanding of how code is conflicting and how best to resolve
it.

Once you've resolved all of the merge conflicts, use `git add -A` to stage them
to be committed, and then use `git rebase --continue` to tell git to continue
the rebase.

When the rebase has completed, you will need to force push your branch because
the history is now completely different than what's on the remote. **This is
potentially dangerous** because it will completely overwrite what you have on
the remote, so you need to be sure that you haven't lost any work when resolving
merge conflicts. (If there weren't any merge conflicts, then you can force push
without having to worry about this.)

```
git push origin name-of-your-branch --force
```

This will overwrite the remote branch with what you have locally. You're done!

**Note that you should not run `git pull`**, for example in response to a push
rejection like this:

```
! [rejected] name-of-your-branch -> name-of-your-branch (non-fast-forward)
error: failed to push some refs to 'https://github.com/YourGitHubHandle/helm-charts.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

Assuming you've successfully rebased and you're happy with the code, you should
force push instead.

### What Goes Into a Pull Request

* Please include an explanation of your changes in your PR description.
* Links to relevant issues, external resources, or related PRs are very
important and useful.
* Please update any tests that pertain to your code, and add new tests where
appropriate.
* See [Submitting a Pull Request](#submitting-a-pull-request) for more info.


## Submitting a Pull Request

Push your local changes to your forked copy of the repository and submit a Pull
Request. In the Pull Request, describe what your changes do and mention the
number of the issue where discussion has taken place, e.g., `Closes #123`.

Always submit your pull request against `main` unless the bug is only present in an
older version. If the bug affects both main and another branch say so in your
pull request.

Then sit back and wait. There will probably be discussion about the Pull Request
and, if any changes are needed, we'll work with you to get your Pull Request
merged into helm-charts.


## Releases

Just like with the rest of the stack, all versions in this helm-charts repo are
bumped and released at the same time. There is no need to bump the version in
your pull request.

Charts are released from version branches (example `7.7` branch).

[Elastic Helm repository][] is updated only during releases.


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
using `make build test`

Note that templating tests are formatted using [Black][], you should run
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


[black]: https://black.readthedocs.io/en/stable/
[cla section]: #cla-contributor-license-agreement
[contributor license agreement]: https://www.elastic.co/contributor-agreement
[elastic helm repository]: https://helm.elastic.co
[github forking model]: https://help.github.com/articles/fork-a-repo/
[goss]: https://github.com/aelsabbahy/goss/blob/master/docs/manual.md
[integration test example]: https://github.com/elastic/helm-charts/blob/main/elasticsearch/examples/default/test/goss.yaml
[integration tests section]: #integration-tests
[pytest]: https://docs.pytest.org/en/latest/
[serverspec]: https://serverspec.org
[templating test example]: https://github.com/elastic/helm-charts/blob/main/elasticsearch/tests/elasticsearch_test.py
[templating tests section]: #templating-tests
[releases section]: #releases
[requirements.txt]: https://github.com/elastic/helm-charts/blob/main/requirements.txt
