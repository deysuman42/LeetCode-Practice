# Write your MySQL query statement below

with t1 as (
select airport, sum(engaged) as engaged from (
select departure_airport as airport, flights_count as engaged from flights
union all
select arrival_airport as airport, flights_count as engaged from flights) x group by airport)

select airport as airport_id from (
Select airport, rank() over (order by engaged desc) as rnk from t1) x where rnk =1


