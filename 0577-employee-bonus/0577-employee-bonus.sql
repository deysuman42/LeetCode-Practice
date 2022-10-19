# Write your MySQL query statement below


# solution 1 - COALESCE
# select e.name, b.bonus from 
# employee e left join bonus b
# on e.empid = b.empid
# where COALESCE(b.bonus,0) < 1000;

# Solution 2 - IS NULL condition
# select e.name, b.bonus from 
# employee e left join bonus b
# on e.empid = b.empid
# where b.bonus < 1000 OR b.bonus is NULL;


# Solution 3 - IFNULL
select e.name, b.bonus from 
employee e left join bonus b
on e.empid = b.empid
where IFNULL(b.bonus,0) < 1000;




