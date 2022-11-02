# Write your MySQL query statement below


with t1 as (select exam_id, max(score) as highest, min(score) as lowest from exam group by exam_id),

t2 as (select a.student_id, b.highest from exam a left join t1 b
on a.exam_id = b.exam_id and a.score in (b.highest, b.lowest)),

t3 as (Select distinct student_id from t2 where highest is null and student_id not in (select student_id from t2 where highest is not null))

Select student_id, student_name from student where student_id in (select student_id from t3)