# Write your MySQL query statement below

select distinct a.num as ConsecutiveNums
from

logs a join logs b join logs c
on b.id = a.id + 1 and c.id = b.id + 1
and b.num = a.num and c.num = b.num