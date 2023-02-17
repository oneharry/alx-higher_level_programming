-- Dump from hbtn_0d_tvshows
-- Lists all genres not linked to the show
SELECT name 
  FROM tv_genres
  WHERE name NOT IN (
       SELECT name
         FROM tv_genres
        INNER JOIN tv_show_genres
	   ON tv_genres.id = tv_show_genres.genre_id
        INNER JOIN tv_shows
	   ON tv_show_genres.show_id = tv_shows.id
	WHERE title = 'Dexter');

