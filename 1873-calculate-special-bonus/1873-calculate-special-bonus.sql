# Write your MySQL query statement below

# with T1 as (select employee_id, name, salary
#            from employees)
          
# select * from t1;
# (CASE
#         WHEN MOD(id, 2) != 0 AND counts != id THEN id + 1
#         WHEN MOD(id, 2) != 0 AND counts = id THEN id
#         ELSE id - 1
#     END) AS id,
           
# select * from t1;


select employee_id, 
(case when (employee_id % 2 = 1) and substring(name, 1, 1) <> 'M' then salary
 else 0
end) as bonus from employees order by employee_id;
