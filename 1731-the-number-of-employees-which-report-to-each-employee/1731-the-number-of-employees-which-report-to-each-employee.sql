# Write your MySQL query statement below


# with t1 as (select reports_to, count(*) as cnt from employees where reports_to is not null group by reports_to ),

# t2 as (select reports_to, cnt as reports_count from t1 where cnt >= 1),

# t3 as (select reports_to as employee_id, ceil(avg(age)) as average_age from employees where reports_to in (select reports_to from t2))

# select b.employee_id, e.name, a.reports_count, b.average_age
# from employees e join t3 b join t2 a on e.employee_id = b.employee_id
# and b.employee_id = a.reports_to


select m.employee_id, m.name, count(e.employee_id) as reports_count, round(avg(e.age)) as average_age
from employees e join employees m
on m.employee_id = e.reports_to
where e.reports_to is not null
group by m.employee_id order by m.employee_id;



