-- script that lists records with same score in second_table
SELECT score, COUNT(*) AS "number"
FROM second_table
GROUP BY score
ORDER BY score DESC
