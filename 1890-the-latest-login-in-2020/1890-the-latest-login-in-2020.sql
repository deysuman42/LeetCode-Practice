# Write your MySQL query statement below

# Solution 1
# select user_id, time_stamp as last_stamp from logins
# where (user_id, time_stamp) in (select user_id, max(time_stamp) from logins 
#           where EXTRACT(YEAR FROM time_stamp) = 2020   group by user_id)

# Solution 2


select user_id, time_stamp as last_stamp from (
select user_id, time_stamp, row_number() over(partition by user_id order by time_stamp desc) as rnk
from logins where EXTRACT(YEAR FROM time_stamp) = 2020) x where rnk = 1;

