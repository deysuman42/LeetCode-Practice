# Write your MySQL query statement below


with T1 as (select s.user_id, c.action from signups s left join confirmations c
on s.user_id = c.user_id),

t2 as (select user_id, action, (case when action is null or action = 'timeout' then 0
                         else 1
                        end) as action_number
from t1)


Select user_id, round(sum(action_number) / count(action_number ),2) as confirmation_rate
from t2 group by user_id;