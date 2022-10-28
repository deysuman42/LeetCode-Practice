# Write your MySQL query statement below


select stock_name, sum(IF(operation = 'Buy', price * (-1), price)) as capital_gain_loss from stocks
group by stock_name;