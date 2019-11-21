#!/bin/bash

# Author: Rafael Battesti - rafaelbattesti.com
# Since: 2019-11-19

set -euo pipefail

psql -v ON_ERROR_STOP=1 \
    --username "${POSTGRES_USER}" \
    --dbname sws \
    -c "SELECT current_database() AS db, * FROM pg_catalog.pg_tables WHERE schemaname NOT IN ('pg_catalog', 'information_schema')"

psql -v ON_ERROR_STOP=1 \
    --username "${POSTGRES_USER}" \
    --dbname sws_dw \
    -c "SELECT current_database() AS db, * FROM pg_catalog.pg_tables WHERE schemaname NOT IN ('pg_catalog', 'information_schema')"

psql -v ON_ERROR_STOP=1 \
    --username "${POSTGRES_USER}" \
    --dbname sws_dw \
    -c "SELECT current_database() AS db, * FROM pg_catalog.pg_views WHERE schemaname NOT IN ('pg_catalog', 'information_schema')"