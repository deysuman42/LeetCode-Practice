# Write your MySQL query statement below

select distinct c.title 
from content c join tvprogram p 
on c.content_id = p.content_id 
where kids_content = 'Y' and content_type = 'Movies'
and extract(year from p.program_date) = 2020 and extract(month from p.program_date) = 6;