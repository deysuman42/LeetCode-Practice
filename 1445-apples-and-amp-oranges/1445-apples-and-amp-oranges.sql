# Write your MySQL query statement below


select sale_date, sum(if(fruit = 'apples', sold_num, 0)) - sum(if(fruit = 'oranges', sold_num, 0)) as diff
from sales group by sale_date