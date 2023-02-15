-- Creates the table "unique_id"
-- Should not fail if not exists
CREATE TABLE unique_id(
       id   INT UNIQUE DEFAULT 1,
       name VARCHAR(256))
