-- Create the table "force_name", DB name passed as argument
-- Script should nit fail if table already exists
CREATE TABLE IF NOT EXISTS force_name(
       id   INT,
       name VARCHAR(256) NOT NULL);
