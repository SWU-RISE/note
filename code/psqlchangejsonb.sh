CREATE TABLE test (id serial, sec text, name text);
INSERT INTO test (id, sec, name) VALUES (1,'{"gender":"male","sections":{"a":1,"b":2}}','subject');
ALTER TABLE test ALTER COLUMN sec TYPE JSONB USING sec::JSONB;
