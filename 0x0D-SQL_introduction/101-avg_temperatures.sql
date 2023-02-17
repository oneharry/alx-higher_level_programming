-- Displays the avg temperature(Fahrenheit) by city
-- Ordered by temp descendin
SELECT t1.city, AVG(t1.value) AS avg_temp
  FROM `temperatures` AS t1
 GROUP BY t1.city
 ORDER BY t1.city DESC;
