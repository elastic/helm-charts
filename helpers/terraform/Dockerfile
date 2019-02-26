FROM centos:7

ENV VAULT_VERSION 0.9.3
ENV TERRAFORM_VERSION=0.11.7
ENV KUBECTL_VERSION=1.10.7
ENV HELM_VERSION=2.8.2

RUN yum -y install \
    make \
    unzip \
    which

RUN yum -y install \
    https://packages.cloud.google.com/yum/pool/654962a43cb6bc6b47bc312424410b7c203e1beb73386d868d9e614839c82609-google-cloud-sdk-215.0.0-1.el7.noarch.rpm && \
    gcloud config set core/disable_usage_reporting true && \
    gcloud config set component_manager/disable_update_check true && \
    gcloud version

RUN curl --retry 5 -O https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip && \
    unzip vault_${VAULT_VERSION}_linux_amd64.zip -d /usr/local/bin/ && \
    chmod +x /usr/local/bin/vault && \
    vault version

RUN curl --retry 5 -O https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/local/bin/ && \
    rm -f terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    terraform version

RUN curl --retry 5 -O https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl && \
    mv kubectl /usr/local/bin/ && \
    chmod a+x /usr/local/bin/kubectl && \
    kubectl version --client

RUN curl --retry 5 -O https://storage.googleapis.com/kubernetes-helm/helm-v${HELM_VERSION}-linux-amd64.tar.gz && \
    tar xfv helm-v${HELM_VERSION}-linux-amd64.tar.gz && \
    mv linux-amd64/helm /usr/local/bin/ && \
    rm -rf linux-amd64 && \
    helm version --client
