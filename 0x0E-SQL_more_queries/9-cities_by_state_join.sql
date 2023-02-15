-- Lists all cities contained in the database
SELECT cities.id AS 'id', cities.name AS 'name', states.name AS 'name'
  FROM cities, states
 ORDER BY cities.id;
