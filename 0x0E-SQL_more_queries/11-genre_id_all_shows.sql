-- Lists all shows contained in the database hbtn_0d_tvshows
SELECT tv_shows.title AS 'title', IFNULL(tv_show_genres.genre_id, 'NULL') AS 'genre_id'
  FROM tv_shows, tv_show_genres
 ORDER BY (tv_shows.title, tv_show_genres.genre_id);