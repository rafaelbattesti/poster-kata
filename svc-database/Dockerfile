FROM postgres

LABEL maintainer "Rafael Battesti - me@rafaelbattesti.com"

ENV PG_DROPIN "/docker-entrypoint-initdb.d"

RUN mkdir -p ${PG_DROPIN}

COPY ./svc-database /svc-database
COPY ./svc-database/init/*.sh ${PG_DROPIN}/