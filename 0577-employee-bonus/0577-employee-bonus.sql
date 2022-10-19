# Write your MySQL query statement below


# solution 1 - COALESCE
# select e.name, b.bonus from 
# employee e left join bonus b
# on e.empid = b.empid
# where COALESCE(b.bonus,0) < 1000;


select e.name, b.bonus from 
employee e left join bonus b
on e.empid = b.empid
where b.bonus < 1000 OR b.bonus is NULL;