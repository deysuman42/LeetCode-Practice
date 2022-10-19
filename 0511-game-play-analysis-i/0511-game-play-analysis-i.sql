# Write your MySQL query statement below

# Solution 1 - rank()
# select
#   player_id,
#   first_login
# from
#   (
#     select
#       player_id,
#       event_date as first_login,
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
# select  distinct player_id, first_value(event_date) over(partition by player_id order by event_date) first_login from Activity;

# Solution 3 - min()
select player_id, min(event_date) as first_login from activity group by player_id;