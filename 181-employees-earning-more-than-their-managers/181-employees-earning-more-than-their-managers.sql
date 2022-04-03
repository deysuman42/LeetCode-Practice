# Write your MySQL query statement below
# with Emp as (select id as emp_id, name as emp_name, salary as emp_salary from Employee),
# Manager as (Select managerid as emp_id, name, salary from Employee)

select e.name as 'Employee' 
from Employee e
inner join employee m
on m.id = e.managerId
and e.salary > m.salary;

