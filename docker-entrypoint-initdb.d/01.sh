#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    create table photos (
	title	     VARCHAR(50) PRIMARY KEY,
	username     VARCHAR(100) NOT NULL );


    create table users (
	username	 VARCHAR(120) PRIMARY KEY,
	password     VARCHAR(100) NOT NULL, 
	full_name    VARCHAR(100) NOT NULL);

insert into users (username, password, full_name) values ('Matt', 'bam', 'Matt Left');
EOSQL
