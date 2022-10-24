# Write your MySQL query statement below


select p.name, coalesce(sum(i.rest),0) as 'rest', coalesce(sum(i.paid),0) as 'paid', 
coalesce(sum(i.canceled),0) as 'canceled', coalesce(sum(i.refunded),0) as 'refunded'
from product p left join invoice i on p.product_id = i.product_id
group by p.product_id order by p.name;