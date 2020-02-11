#!/usr/bin/env python2

import glob
import os
import subprocess
import yaml

try:
    raw_input
except NameError:  # Python 3
    raw_input = input

os.chdir(os.path.join(os.path.dirname(__file__), ".."))

bucket = "gs://" + os.environ["GCS_BUCKET"]


def run(cmd):
    if "DEBUG" in os.environ:
        print(" ".join(cmd))
    else:
        subprocess.check_call(cmd)


# Cleanup existing releases
for release in glob.glob("*/*.tgz"):
    print("Removing: " + release)
    os.remove(release)

for filepath in glob.iglob("*/Chart.yaml"):
    chart = os.path.split(os.path.dirname(filepath))[-1]

    # Download dependencies
    run(["helm", "dependency", "update", chart])

    # Package up the chart
    run(["helm", "package", chart, "--destination", chart])

    # Upload it to the GCS bucket if it doesn't exist
    source = "{chart}/{chart}-*.tgz".format(**locals())
    destination = "{bucket}/helm/{chart}/".format(**locals())
    run(["gsutil", "cp", "-n", source, destination])

# Grab the current index so we can merge it with the latest releases
run(["gsutil", "cp", bucket + "/index.yaml", "index.yaml.old"])

# Merge it with the old index to include the older releases
run(
    [
        "helm",
        "repo",
        "index",
        "--merge",
        "index.yaml.old",
        "--url",
        "https://helm.elastic.co/helm/",
        ".",
    ]
)

with open("index.yaml", "r") as index:
    print("=" * 80)
    print(index.read())
    print("=" * 80)

answer = raw_input('Upload new index.yaml? ("y" or "yes")\n')
if answer in ["y", "yes"]:
    run(["gsutil", "cp", "index.yaml", bucket + "/index.yaml"])
