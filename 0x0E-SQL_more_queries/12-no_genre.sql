-- Lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT tv_shows.title AS 'title', tv_show_genres.genre_id AS 'genre_id'
  FROM tv_shows, tv_show_genres
 WHERE tv_shows.id != tv_show_genres.show_id
 ORDER BY (tv_shows.title, tv_show_genres.genre_id);
