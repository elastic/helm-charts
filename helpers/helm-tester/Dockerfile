FROM python:3.7

ENV HELM_VERSION=3.6.2

RUN wget --no-verbose https://get.helm.sh/helm-v${HELM_VERSION}-linux-amd64.tar.gz && \
    tar xfv helm-v${HELM_VERSION}-linux-amd64.tar.gz && \
    mv linux-amd64/helm /usr/local/bin/ && \
    mkdir --parents --mode=777 /.config/helm && \
    HOME=/ helm repo add stable https://charts.helm.sh/stable && \
    rm -rf helm-v${HELM_VERSION}-linux-amd64.tar.gz linux-amd64

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

COPY . /usr/src/app
