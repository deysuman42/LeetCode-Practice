# Write your MySQL query statement below

# Solution 1
select class
from courses group by class
having count(student) >= 5;

