# Write your MySQL query statement below

select ad_id, 
(case when COUNT(IF(action = 'Clicked',user_id,NULL)) + COUNT(IF(action = 'Viewed',user_id,NULL)) = 0 then 0.00
 else round(COUNT(IF(action = 'Clicked',user_id,NULL)) / (COUNT(IF(action = 'Clicked',user_id,NULL)) + COUNT(IF(action = 'Viewed',user_id,NULL))) * 100 ,2) 
 end) as ctr

from ads
group by ad_id
order by ctr desc, ad_id asc