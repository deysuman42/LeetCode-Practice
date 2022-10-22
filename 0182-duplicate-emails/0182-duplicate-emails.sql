# Write your MySQL query statement below


# select email from (select email, count(*) as c from person group by email) a 
# where c > 1

Select email from person group by email
having count(id) > 1;
