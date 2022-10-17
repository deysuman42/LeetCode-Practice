/* Write your PL/SQL query statement below */


Select id from (
select id, Temperature, lag(Temperature) over (order by recordDate) as r,
recordDate - lag(recordDate) over (order by recordDate) as d
from Weather
    
) where Temperature > r and d = 1;