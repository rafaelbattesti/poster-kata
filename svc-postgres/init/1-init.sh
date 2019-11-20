#!/bin/bash

# Author: Rafael Battesti - rafaelbattesti.com
# Since: 2019-11-19

set -euo pipefail

# TODO: Create users

# Create databases
createdb sws
createdb sws_dw

# Create schemas
psql -v ON_ERROR_STOP=1 --username "${POSTGRES_USER}" --dbname sws < /svc-postgres/init/sws.sql
psql -v ON_ERROR_STOP=1 --username "${POSTGRES_USER}" --dbname sws_dw < /svc-postgres/init/sws_dw.sql

# TODO: Grant permissions - isolate schemas