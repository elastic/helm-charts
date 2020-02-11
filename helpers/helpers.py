import tempfile
import yaml
import os
import json
from subprocess import check_output


def helm_template(config):
    with tempfile.NamedTemporaryFile() as temp:
        with open(temp.name, "w") as values:
            values.write(config)
        helm_cmd = "helm template -f {0} ./".format(temp.name)
        result = yaml.load_all(check_output(helm_cmd.split()))

        results = {}
        for r in result:
            if r:
                kind = r["kind"].lower()
                if kind not in results:
                    results[kind] = {}
                results[kind][r["metadata"]["name"]] = r

        if os.environ.get("DEBUG"):
            print(json.dumps(results, indent=4, sort_keys=True))
        return results
