-- all records of the table second_table
-- lists all records of the table second_table with scores greater than or equal to 10
SELECT
	score, name
FROM
	second_table
WHERE
      score >= 10
ORDER BY score DESC;
