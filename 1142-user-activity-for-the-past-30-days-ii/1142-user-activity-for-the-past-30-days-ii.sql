# Write your MySQL query statement below


select round(Coalesce(avg(cnt),0.00000),2)  as average_sessions_per_user from (
select user_id, count(distinct session_id) as cnt from activity
where activity_date > DATE_SUB('2019-07-27', interval 30 day) and activity_date <= '2019-07-27'
group by user_id) x