-- Creates the bable "id_not_null" on the server
-- DB will be passed in the msql command
CREATE TABLE IF NOT EXISTS id_not_null(
       id   INT DEFAULT 1,
       name VARCHAR(256))
