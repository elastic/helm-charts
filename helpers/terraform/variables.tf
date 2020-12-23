variable "cluster_name" {
  description = "Name of the GKE cluster"
}

variable "kubernetes_version" {
  description = "GKE Kubernetes version for deployment (master and pools)"
  default     = "1.9.7-gke.6"
}

variable "initial_node_count" {
  description = "Default amount of nodes per zone that will be launched"
  default     = 1
}

variable "primary_region" {
  description = "The primary region provision resources within."
  default     = "us-central1"
}

variable "primary_zone" {
  description = "The primary zone to provision resources within."
  default     = "us-central1-a"
}

variable "project" {
  description = "The Google Cloud Platform project ID to target."
}

variable "additional_zones" {
  description = "Zones that the node pool will use in addition to the primary zone"
  type        = "list"

  default = [
    "us-central1-b",
    "us-central1-c",
    "us-central1-f",
  ]
}

variable "machine_type" {
  description = "Machine type for the kubernetes nodes"
  default     = "custom-10-30720"
}

variable "network" {
  default = "helm-charts-k8s"
}

variable "subnetwork" {
  default = "helm-charts-k8s"
}
