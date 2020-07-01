provider "google" {
  project = "${var.project}"
  region  = "${var.primary_region}"
  version = "2.13.0"
}

terraform {
  backend "gcs" {}
}

resource "google_container_cluster" "cluster" {
  description        = "Helm testing kubernetes cluster"
  name               = "${var.cluster_name}"
  zone               = "${var.primary_zone}"
  initial_node_count = "${var.initial_node_count}"
  additional_zones   = "${var.additional_zones}"
  min_master_version = "${var.kubernetes_version}"
  node_version       = "${var.kubernetes_version}"
  logging_service    = "none"
  monitoring_service = "none"

  network    = "${var.network}"
  subnetwork = "${var.subnetwork}"

  node_config = {
    machine_type = "${var.machine_type}"
  }

  timeouts {
    create = "180m"
    delete = "180m"
    update = "180m"
  }
}
