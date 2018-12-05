FROM otx/{{cookiecutter.project_slug}}:latest
MAINTAINER AlienVault
ENV RUN_TYPE="tests"
COPY test_requirements.txt /task
RUN pip install -r /task/test_requirements.txt
COPY . /task
