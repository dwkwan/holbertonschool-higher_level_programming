--  all records of the table second_table of the database
-- lists all records of the table second_table of the database that have name
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
