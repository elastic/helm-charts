#!/usr/bin/env python2
import re
import os
import glob
import subprocess
import fileinput

os.chdir(os.path.join(os.path.dirname(__file__), '..'))

versions = {
    5: '5.6.16',
    6: '6.8.0',
    7: '7.1.0',
}

file_patterns = [
    '*/examples/*/test/goss.y*ml',
    '*/examples/*/*.y*ml',
    '*/README.md',
    '*/values.y*ml',
    '*/Chart.y*ml',
]

# Anything matching this regex won't have version bumps changed
# This was happening because strings like 127.0.0.1 match for 7.0.0
blacklist = re.compile(r".*127.0.0.1.*")

for major, version in versions.iteritems():
    r = re.compile(r"{0}\.[0-9]*\.[0-9]*".format(major))
    for pattern in file_patterns:
        for f in glob.glob(pattern):
            print(f)
            for line in fileinput.input([f], inplace=True):
                if re.match(blacklist, line):
                    print(line.rstrip())
                else:
                    print(r.sub(version, line.rstrip()))
