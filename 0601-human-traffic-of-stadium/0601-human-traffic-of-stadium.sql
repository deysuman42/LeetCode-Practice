# Write your MySQL query statement below
with t1 as (
select a.id from stadium a join
stadium b join stadium c on b.id = a.id + 1
and c.id = b.id + 1 and a.people >= 100 and b.people >= 100 
and c.people >= 100

union 

select b.id from stadium a join
stadium b join stadium c on b.id = a.id + 1
and c.id = b.id + 1 and a.people >= 100 and b.people >= 100 
and c.people >= 100

union

select c.id from stadium a join
stadium b join stadium c on b.id = a.id + 1
and c.id = b.id + 1 and a.people >= 100 and b.people >= 100 
and c.people >= 100)

select t1.id, s.visit_date, s.people from stadium s join t1 
on s.id = t1.id;