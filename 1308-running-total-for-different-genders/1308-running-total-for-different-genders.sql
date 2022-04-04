# Write your MySQL query statement below

SELECT gender, day, 
SUM(score_points) OVER (partition by gender ORDER BY day) AS total
FROM scores;