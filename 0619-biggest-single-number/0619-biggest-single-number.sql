# Write your MySQL query statement below

select max(num) as num from (select num, count(*) as num_count from mynumbers group by num)x where num_count = 1;
