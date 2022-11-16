FROM python:3.10.2-slim

ENV DOCKER_VERSION=20.10.12
ENV GCLOUD_VERSION=375.0.0
ENV HELM_VERSION=3.10.2
ENV KUBECTL_VERSION=1.21.6
ENV TERRAFORM_VERSION=0.11.7
ENV VAULT_VERSION=1.9.3

RUN apt-get update && apt-get upgrade -y && \
  apt-get install --no-install-recommends -y curl jq make openssl unzip && \
  rm -rf /var/lib/apt/lists/*

RUN curl -O  https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${GCLOUD_VERSION}-linux-x86_64.tar.gz && \
  tar xvf google-cloud-sdk-${GCLOUD_VERSION}-linux-x86_64.tar.gz && \
  ./google-cloud-sdk/install.sh --quiet --usage-reporting=false --path-update=true && \
  rm -fr google-cloud-sdk-${GCLOUD_VERSION}-linux-x86_64.tar.gz && \
  ln -s /google-cloud-sdk/bin/gcloud /usr/local/bin/gcloud && \
  gcloud config set component_manager/disable_update_check true && \
  gcloud version

RUN curl -O https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip && \
  unzip vault_${VAULT_VERSION}_linux_amd64.zip -d /usr/local/bin/ && \
  chmod +x /usr/local/bin/vault && \
  rm -f vault_${VAULT_VERSION}_linux_amd64.zip && \
  vault version

RUN curl -O https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
  unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/local/bin/ && \
  rm -f terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
  terraform version

RUN curl -O https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl && \
  mv kubectl /usr/local/bin/ && \
  chmod a+x /usr/local/bin/kubectl && \
  kubectl version --client

RUN curl -O https://get.helm.sh/helm-v${HELM_VERSION}-linux-amd64.tar.gz && \
  tar xfv helm-v${HELM_VERSION}-linux-amd64.tar.gz && \
  mv linux-amd64/helm /usr/local/bin/ && \
  rm -rf helm-v${HELM_VERSION}-linux-amd64.tar.gz linux-amd64 && \
  helm version --client

RUN curl -O https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz && \
  tar xfv docker* && \
  mv docker/docker /usr/local/bin && \
  rm -rf docker-${DOCKER_VERSION}.tgz docker/ && \
  docker -v
