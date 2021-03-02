-- lists all records of table if name value not null
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
