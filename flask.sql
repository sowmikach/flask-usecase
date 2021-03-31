create database mydb;
use mydb;
show tables;
create table savedquery(queryname VARCHAR(150), querydetails VARCHAR(250), created_date timestamp DEFAULT current_timestamp );
select * from savedquery;

