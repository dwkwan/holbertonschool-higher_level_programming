-- All the cities of California that can be found in the database hbtn_0d_usa
-- Lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT
       name, id
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = "California")
ORDER BY id ASC
