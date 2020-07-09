#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER image_gallery;
    CREATE DATABASE image_gallery;
    GRANT ALL PRIVILEGES ON DATABASE image_gallery TO image_gallery;
EOSQL
