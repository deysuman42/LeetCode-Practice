# Write your MySQL query statement below

# Solution 1 - Temporary table
# select email from (select email, count(*) as c from person group by email) a 
# where c > 1

# Solution 2 - Having
# Select email from person group by email
# having count(id) > 1;

# Solution 3 - Self join
select distinct a.email from person a join person b
on a.email = b.email and a.id <> b.id;