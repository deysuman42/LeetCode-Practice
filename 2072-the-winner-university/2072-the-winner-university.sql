# Write your MySQL query statement below

# select (case when select sum(if(a.score > 90,1,0)) > sum(if(b.score > 90,1,0)) then 'New York University'

     
     
SELECT (CASE 
            WHEN (SELECT COUNT(score) FROM NewYork WHERE score >= 90) > (SELECT COUNT(score) FROM California WHERE score >= 90) THEN 'New York University'
            WHEN (SELECT COUNT(score) FROM NewYork WHERE score >= 90) < (SELECT COUNT(score) FROM California WHERE score >= 90) THEN 'California University'
            ELSE 'No Winner' END) AS WINNER
;