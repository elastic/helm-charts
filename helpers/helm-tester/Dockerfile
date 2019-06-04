FROM python:2.7-onbuild

ENV HELM_VERSION=2.14.0

RUN wget https://storage.googleapis.com/kubernetes-helm/helm-v${HELM_VERSION}-linux-amd64.tar.gz && \
    tar xfv helm-v${HELM_VERSION}-linux-amd64.tar.gz && \
    mv linux-amd64/helm /usr/local/bin/ && \
    rm -rf linux-amd64
