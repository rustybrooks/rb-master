FROM ubuntu:18.04
MAINTAINER AlienVault
ARG buildVersion
ENV BUILD_VERSION=$buildVersion
ENV FLASK_APP="api" RUN_TYPE="gunicorn"
COPY requirements.txt /task
RUN pip install -r /task/requirements.txt
COPY . /task
ENTRYPOINT /task/entrypoint.sh
