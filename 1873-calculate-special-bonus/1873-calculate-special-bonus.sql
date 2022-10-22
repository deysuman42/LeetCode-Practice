# Write your MySQL query statement below


# Solution 1 - CASE
# select employee_id, 
# (case when (employee_id % 2 = 1) and substring(name, 1, 1) <> 'M' then salary
#  else 0
# end) as bonus from employees order by employee_id;


# Solution 2 - IF
select employee_id, IF(employee_id % 2 = 1 and name not like 'M%', salary, 0) as bonus
from employees order by employee_id;