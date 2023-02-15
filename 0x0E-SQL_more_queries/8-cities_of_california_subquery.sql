-- Lists all the cities of california in the DB "hbtn_0d_usa"
SELECT id, name
  FROM cities
 WHERE cities.id = (
       SELECT id
         FROM states
	WHERE states.name = 'California')
 ORDER BY cities.id;
