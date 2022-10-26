# Write your MySQL query statement below


with T1 as (select distinct customer_id from orders where product_name = 'A'),
T2 as (select distinct customer_id from orders where product_name = 'B'),
T3 as (select distinct customer_id from t1 where customer_id in (select customer_id from t2)),
T4 as (select distinct customer_id from orders where product_name = 'C'),
T5 as (select distinct customer_id from t3 where customer_id not in (select customer_id from t4))

Select customer_id, customer_name from customers where customer_id in (select customer_id from t5)
# select * from t4;
