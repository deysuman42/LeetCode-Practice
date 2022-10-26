# Write your MySQL query statement below

with T1 as (select p.id, c.name from 
person p join country c on substring(p.phone_number, 1,3) = c.country_code)

select t1.name as country from calls 
join t1 on t1.id in (calls.caller_id, calls.callee_id)
group by t1.name
having avg(duration) > (select avg(duration) from calls)



# SELECT
#  co.name AS country
# FROM
#  person p
#  JOIN
#      country co
#      ON SUBSTRING(phone_number,1,3) = country_code
     
     
     
#  JOIN
#      calls c
#      ON p.id IN (c.caller_id, c.callee_id)
# GROUP BY
#  co.name
# HAVING
#  AVG(duration) > (SELECT AVG(duration) FROM calls)