FROM python:3.10.2-slim

ENV HELM_VERSION=3.10.2

RUN apt-get update && apt-get upgrade -y && \
  apt-get install --no-install-recommends -y make wget && \
  rm -rf /var/lib/apt/lists/*

RUN wget --no-verbose https://get.helm.sh/helm-v${HELM_VERSION}-linux-amd64.tar.gz && \
  tar xfv helm-v${HELM_VERSION}-linux-amd64.tar.gz && \
  mv linux-amd64/helm /usr/local/bin/ && \
  mkdir --parents --mode=777 /.config/helm && \
  HOME=/ helm repo add prometheus-community https://prometheus-community.github.io/helm-charts && \
  rm -rf helm-v${HELM_VERSION}-linux-amd64.tar.gz linux-amd64

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

COPY . /usr/src/app
