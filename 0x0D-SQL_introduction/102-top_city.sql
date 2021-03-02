-- script top 3 of cities temperatures during July and August
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month=7 OR month=8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3
