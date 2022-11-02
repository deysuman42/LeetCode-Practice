# Write your MySQL query statement below

with t1 as (
select first_player as player_id, first_score as score from matches
union all
select second_player as player_id, second_score as score from matches),

t2 as (Select p.player_id, p.group_id, t1.score from players p left join t1
on p.player_id = t1.player_id),


t3 as (select group_id, player_id, sum(score) as score from t2 
group by group_id, player_id)


select group_id, player_id from (select group_id, player_id, rank() over (partition by group_id order by score desc, player_id) as rnk 
from t3)x where rnk = 1