# Write your MySQL query statement below

select * from (
select employee_id,
(case when cnt > 1 and primary_flag = 'Y' then department_id
WHEN cnt = 1 then department_id
end) as department_id from (
select employee_id, department_id, primary_flag, count(*) over (partition by employee_id order by employee_id) as cnt from employee)x ) y where department_id is not null
