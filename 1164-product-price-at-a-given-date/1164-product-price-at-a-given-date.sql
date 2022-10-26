# Write your MySQL query statement below


with t1 as (
select product_id, max(change_date) as dt
from products where change_date <= '2019-08-16'
group by product_id)

select p.product_id, p.new_price as price from products p 
join t1 b on p.product_id = b.product_id and b.dt = p.change_date 

union 

select product_id, 10 as price from products where product_id not in (select product_id from t1)