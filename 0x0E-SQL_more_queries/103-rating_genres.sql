-- Dump from hbtn_0d_tvshows
-- lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT name, SUM(rate) AS rating
  FROM tv_genres AS g
  LEFT JOIN tv_show_genres AS sg
    ON g.id = sg.genre_id
 INNER JOIN tv_shows AS s
    ON sg.show_id = s.id
 INNER JOIN tv_show_ratings AS sr
    ON s.id = sr.show_id
 GROUP BY name
 ORDER BY SUM(rate) DESC;
