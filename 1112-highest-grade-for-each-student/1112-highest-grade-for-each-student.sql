# Write your MySQL query statement below


select student_id, course_id, grade from (
select student_id, course_id, grade, row_number() over (partition by student_id order by course_id) as rnk1 from (
select student_id, course_id, grade, rank() over (partition by student_id order by grade desc) as rnk
from enrollments) x where rnk = 1) y where rnk1 = 1;