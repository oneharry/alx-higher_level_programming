-- Displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT t.city, AVG(t.value) AS avg_temp
  FROM temperatures AS t
 WHERE month BETWEEN 7 AND 8
 GROUP BY t.city
 ORDER BY AVG(t.value) DESC
 LIMIT 3;
