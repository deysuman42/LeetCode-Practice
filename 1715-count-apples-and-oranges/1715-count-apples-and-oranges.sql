# Write your MySQL query statement below

select (sum(apple_count) + sum(chest_apple_count)) as 'apple_count', 
(sum(orange_count) + sum(chest_orange_count)) as 'orange_count' from (
select b.box_id, b.apple_count, b.orange_count, coalesce(c.apple_count,0) as chest_apple_count, 
coalesce(c.orange_count,0) as chest_orange_count from boxes b left join chests c on 
b.chest_id = c.chest_id)x

