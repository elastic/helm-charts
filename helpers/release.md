# Release process

* Update the [changelog](/CHANGELOG.md)
* Update the stack and chart versions in [bumper.py](/helpers/bumper.py) and run the script. This will update the versions in all the right places
* Open a pull request and wait for a green build before merging
* Create a [new release](https://github.com/elastic/helm-charts/releases/new) and include the latest changelog entry
* Run the [release script](/helpers/release.py) to build and upload the artifact
  ```
  GCS_BUCKET=elastic-helm-charts python release.py
  ```
