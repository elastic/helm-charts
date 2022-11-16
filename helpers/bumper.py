#!/usr/bin/env python2

#
# Usage:
#   ./bumper.py
#
# Configurable environment variables:
# - BUMPER_USE_STAGING_IMAGES set to "true" causes the
#   docker.elastic.co/staging/ docker registry namespace to be used.
#

import re
import os
import glob
import fileinput

os.chdir(os.path.join(os.path.dirname(__file__), ".."))

version = "8.5.1"
major = "8"

chart_version = version

file_patterns = [
    "*/examples/*/*.y*ml",
    "*/examples/*/README.md",
    "helpers/examples.mk",
    "*/README.md",
    "*/values.y*ml",
    "*/Chart.y*ml",
]

goss_files = ["*/examples/*/test/goss*.y*ml"]


# Anything matching this regex won't have version bumps changed
# This was happening because strings like 127.0.0.1 match for 7.0.0
# "7.0.0-alpha1" and "7.4.0" are also used in elasticsearch upgrade test and so
# shouldn't be bumped
blacklist = re.compile(r".*127.0.0.1.*|.*7.0.0-alpha1.*|.*7.4.0.*")

print("Updating version...")

r = re.compile(r"{0}\.[0-9]*\.[0-9]*-?[0-9]?".format(major))
for pattern in file_patterns:
    for f in glob.glob(pattern):
        print(f)
        for line in fileinput.input([f], inplace=True):
            if re.match(blacklist, line):
                print(line.rstrip())
            else:
                if f.endswith("Chart.yaml") and line.startswith("version:"):
                    print(r.sub(chart_version, line.rstrip()))
                else:
                    print(r.sub(version, line.rstrip()))
for pattern in goss_files:
    for f in glob.glob(pattern):
        print(f)
        for line in fileinput.input([f], inplace=True):
            # If we have a version with a build id, like 7.7.0-abcdabcd,
            # strip off the latter part and only use the 7.7.0 in the goss
            # tests
            version_without_build_id = re.sub(r"-.*", "", version)
            if re.match(blacklist, line):
                print(line.rstrip())
            else:
                print(r.sub(version_without_build_id, line.rstrip()))


if os.environ.get("BUMPER_USE_STAGING_IMAGES") == "true":
    image_file_patterns = file_patterns + [
        "*/tests/*.py",
        "**/templates/*.tpl",
        # some tests use docker images in their makefile
        "*/examples/*/Makefile",
    ]

    print("\nUpdating namespaces...")

    for pattern in image_file_patterns:
        for f in glob.glob(pattern):
            print(f)
            for line in fileinput.input([f], inplace=True):
                print(
                    re.sub(
                        r"docker.elastic.co/.+?/",
                        "docker.elastic.co/staging/",
                        line.rstrip(),
                    )
                )

    print("\nUpdating imagePullSecrets...")

    for f in glob.glob("*/values.y*ml"):
        print(f)
        for line in fileinput.input([f], inplace=True):
            print(
                line.rstrip().replace(
                    "imagePullSecrets: []",
                    "imagePullSecrets: [{name: registry-staging}]",
                )
            )
