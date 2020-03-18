#!/usr/bin/env python2

#
# Usage:
#   ./bumper.py
#
# Configurable environment variables:
# - BUMPER_VERSION_6 overrides the 6.x.x version.
# - BUMPER_VERSION_7 overrides the 7.x.x version.
# - BUMPER_USE_STAGING_IMAGES set to "true" causes the
#   docker.elastic.co/staging/ docker registry namespace to be used.
#

import re
import os
import glob
import subprocess
import fileinput

os.chdir(os.path.join(os.path.dirname(__file__), ".."))

versions = {
    6: os.environ.get("BUMPER_VERSION_6", "6.8.7"),
    7: os.environ.get("BUMPER_VERSION_7", "7.6.1"),
}

chart_version = versions[7]

file_patterns = [
    "*/examples/*/test/goss*.y*ml",
    "*/examples/*/*.y*ml",
    "helpers/examples.mk",
    "*/README.md",
    "*/values.y*ml",
    "*/Chart.y*ml",
]

# Anything matching this regex won't have version bumps changed
# This was happening because strings like 127.0.0.1 match for 7.0.0
blacklist = re.compile(r".*127.0.0.1.*")

for major, version in versions.iteritems():
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

if os.environ.get("BUMPER_USE_STAGING_IMAGES") == "true":
    image_file_patterns = file_patterns + [
        "*/tests/*.py",
        "**/templates/*.tpl",
        "**/Makefile",
    ]

    for pattern in image_file_patterns:
        for f in glob.glob(pattern):
            print(f)
            for line in fileinput.input([f], inplace=True):
                print(
                    re.sub(
                        r"docker.elastic.co/.+/",
                        "docker.elastic.co/staging/",
                        line.rstrip(),
                    )
                )
