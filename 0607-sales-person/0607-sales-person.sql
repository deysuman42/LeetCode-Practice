# Write your MySQL query statement below



with T1 as (select o.sales_id from orders o left join company c
           on c.com_id = o.com_id where c.name = 'RED')

select name from salesperson where sales_id not in (select sales_id from t1)