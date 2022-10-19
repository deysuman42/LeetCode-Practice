# Write your MySQL query statement below

# Solution 1 - where 
# select name, population, area 
# from world WHERE area >= 3000000 or population >= 25000000

# Solution 2 - union
select name, population, area 
from world WHERE area >= 3000000
union
select name, population, area 
from world WHERE population >= 25000000