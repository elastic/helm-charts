FROM python:2.7-onbuild

RUN wget https://storage.googleapis.com/kubernetes-helm/helm-v2.7.2-linux-amd64.tar.gz && \
    tar xfv helm-v2.7.2-linux-amd64.tar.gz && \
    mv linux-amd64/helm /usr/local/bin/ && \
    rm -rf linux-amd64
