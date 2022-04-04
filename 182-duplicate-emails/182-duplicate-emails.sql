# Write your MySQL query statement below


select email from (select email, count(*) as c from person group by email) a 
where c > 1
