# Write your MySQL query statement below

# Solution 1 - rank()
select
  player_id,
  device_id
from
  (
    select
      player_id,
      device_id,
      rank() over (
        partition by player_id
        order by
          event_date
      ) as rnk
    from
      activity
  ) x
where
  rnk = 1
