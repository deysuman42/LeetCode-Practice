# Write your MySQL query statement below

with t1 as (select order_id, avg(quantity) as avg_q, max(quantity) as max_q
from OrdersDetails group by order_id)

select order_id from t1 where max_q > ALL (select avg_q from t1)