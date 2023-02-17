-- Displays the avg temperature(Fahrenheit) by city
-- Ordered by temp descendin
SELECT city, AVG(value) AS avg_temp
  FROM temperatures
 GROUP BY city
 ORDER BY AVG(value) DESC;
