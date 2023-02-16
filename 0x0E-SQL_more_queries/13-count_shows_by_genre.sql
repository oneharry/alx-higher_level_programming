-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.name AS '', COUNT(*)
  FROM tv_genres
 INNER JOIN tv_show_genres
    ON tv_genres.id = tv_show_genres.genre_id
 ORDER BY COUNT(*) DESC;