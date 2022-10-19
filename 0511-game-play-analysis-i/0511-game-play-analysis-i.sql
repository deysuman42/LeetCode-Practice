# Write your MySQL query statement below


select player_id, first_login from (
select player_id, event_date as first_login, rank() over (partition by player_id order by event_date)as rnk from activity) x
    where rnk = 1