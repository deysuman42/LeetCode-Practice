# Write your MySQL query statement below

WITH T1 AS
  (SELECT company,
          salary,
          id,
          row_number() over(PARTITION BY company
                            ORDER BY salary) AS s
   FROM employee),
     T2 AS
  (SELECT company,
          count(salary) AS c
   FROM employee
   GROUP BY company),
     T3 AS
  (SELECT company,
          c,
          (CASE
               WHEN c % 2 = 0 THEN floor(c / 2)
               ELSE ceil(c/2)
           END) AS m
   FROM T2
   UNION SELECT company,
                c,
                (CASE
                     WHEN c % 2 = 0 THEN floor(c / 2) + 1
                     ELSE ceil(c/2)
                 END) AS m
   FROM T2),
     T4 AS
  (SELECT t1.company,
          t1.salary,
          t3.m
   FROM t1
   INNER JOIN t3 ON t1.company = t3.company
   AND t1.s = t3.m)
SELECT t1.id,
       t4.company,
       t4.salary
FROM t4
INNER JOIN t1 ON t4.company = t1.company
AND t4.m = t1.s;
