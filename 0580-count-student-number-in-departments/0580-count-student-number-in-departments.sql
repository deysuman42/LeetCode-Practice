# Write your MySQL query statement below

select d.dept_name, coalesce(count(s.student_id), 0) AS student_number
from department d left join student s on d.dept_id = s.dept_id group by d.dept_name
order by student_number desc, d.dept_name