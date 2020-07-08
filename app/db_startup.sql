create table photos (
	title	     VARCHAR(50) PRIMARY KEY,
	username     VARCHAR(100) NOT NULL );


create table users (
	username	     VARCHAR(120) PRIMARY KEY,
	password     VARCHAR(100) NOT NULL, 
	full_name    VARCHAR(100) NOT NULL);

insert into users (username, password, full_name) values ('Matt', 'bam', 'Matt Left');

insert into users (username, password, full_name) values ('dongji', 'cpsc4973', 'dongji');

insert into users (username, password, full_name) values ('sean', 'yes', 'Sean James');

