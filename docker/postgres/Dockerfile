FROM postgres:12.2

ARG POSTGRES_TEST_DB

COPY ./init-user-db.sh /docker-entrypoint-initdb.d/init-user-db.sh
