# Write your MySQL query statement below

with t1 as (select s.user_id, s.product_id, sum((s.quantity * p.price)) as spent
from sales s left join product p on s.product_id = p.product_id group by s.user_id, s.product_id)


select user_id, product_id from (
select user_id, product_id, rank() over (partition by user_id order by spent desc) as rnk
from t1) x where rnk = 1


