-- Write a scripts that creates table unique_id with default unique value

CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256));
