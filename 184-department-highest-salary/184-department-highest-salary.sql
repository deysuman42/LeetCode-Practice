# Write your MySQL query statement below

Select Department, Employee, Salary
from (SELECT d.name as 'Department', e.name as 'Employee', e.Salary,
rank() over (partition by e.departmentId order by e.salary desc) as r
from employee e inner join department d on e.departmentId = d.Id) x
where r = 1;
