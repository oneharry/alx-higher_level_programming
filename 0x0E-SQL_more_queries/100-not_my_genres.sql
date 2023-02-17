-- Dump from hbtn_0d_tvshows
-- Lists all genres not linked to the show
SELECT name 
  FROM tv_genres
 WHERE name NOT IN (
       SELECT name
         FROM tv_genres AS g
        INNER JOIN tv_show_genres AS sh
	   ON g.id = sh.genre_id
        INNER JOIN tv_shows AS s
	   ON sh.show_id = s.id
	WHERE title = 'Dexter')
 ORDER BY name;
