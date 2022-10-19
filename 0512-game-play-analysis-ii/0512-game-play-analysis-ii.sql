# Write your MySQL query statement below

# Solution 1 - rank()
# select
#   player_id,
#   device_id
# from
#   (
#     select
#       player_id,
#       device_id,
#       rank() over (
#         partition by player_id
#         order by
#           event_date
#       ) as rnk
#     from
#       activity
#   ) x
# where
#   rnk = 1



# Solution 2 - first_value()
# select distinct player_id, first_value(device_id)  over(partition by player_id order by event_date) as 'device_id'  from Activity;


# Solution 3 - min()
select player_id, device_id  from activity where (player_id, event_date) in (select player_id, min(event_date) as 'event_date' from activity group by player_id);
