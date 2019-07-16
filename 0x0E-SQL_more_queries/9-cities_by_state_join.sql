-- All the cities of California contained in the database hbtn_0d_usa
-- Lists all the cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
