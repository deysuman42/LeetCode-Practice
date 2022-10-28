# Write your MySQL query statement below

select b.name from employee a join employee b
on b.id = a.managerid
group by b.id
having count(a.id) >= 5

