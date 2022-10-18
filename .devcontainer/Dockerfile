# SEE: https://github.com/microsoft/vscode-remote-try-python/blob/main/.devcontainer/Dockerfile
# SEE: https://github.com/microsoft/vscode-dev-containers/tree/main/containers/python-3

# See here for image contents: https://github.com/microsoft/vscode-dev-containers/blob/v0.202.3/containers/python-3/.devcontainer/base.Dockerfile
# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG VARIANT=3.10-bullseye
FROM mcr.microsoft.com/devcontainers/python:${VARIANT}

# Install Java

RUN apt update && \
    apt install -y openjdk-11-jdk && \
    ln -s /usr/lib/jvm/java-11-openjdk-*/ /usr/lib/jvm/java-11-openjdk 

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk

# Install requirements

COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
   && rm -rf /tmp/pip-tmp
