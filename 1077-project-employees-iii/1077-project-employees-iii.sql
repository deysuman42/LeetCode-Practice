# Write your MySQL query statement below


select project_id, employee_id from (
select p.project_id, e.employee_id, e.experience_years, rank() over(partition by p.project_id order by e.experience_years desc) as rnk from project p join employee e 
on p.employee_id = e.employee_id) x where rnk = 1
