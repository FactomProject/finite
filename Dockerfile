FROM python:3.7-stretch

#postgresql-contrib-11 postgresql-plpython3-11 \
RUN apt-get update \
    && apt-get -y install curl git vim tig \
    python3-dev python3-pip python3 \
    postgresql-client \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENTRYPOINT /bin/bash -c "tail -f /dev/null"
