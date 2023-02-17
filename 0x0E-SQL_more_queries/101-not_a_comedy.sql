-- Dump from hbtn_0d_tvshows
-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT title
  FROM tv_shows AS s
 WHERE title NOT IN (
       SELECT title
         FROM tv_shows AS s
        INNER JOIN tv_show_genres AS sg
	   ON s.id = sg.show_id
	INNER JOIN tv_genres AS g
	   ON sg.genre_id = g.id
	WHERE name = 'Comedy')
 ORDER BY title;
