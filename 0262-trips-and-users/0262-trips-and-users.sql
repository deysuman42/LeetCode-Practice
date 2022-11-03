# Write your MySQL query statement below

# SELECT Request_at as Day,
#        ROUND(COUNT(IF(Status != 'completed', TRUE, NULL)) / COUNT(*), 2) AS 'Cancellation Rate'
# FROM Trips
# WHERE (Request_at BETWEEN '2013-10-01' AND '2013-10-03')
#       AND Client_id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes')
# GROUP BY Request_at;



SELECT Request_at Day, ROUND(SUM(Status <> 'completed')/COUNT(*), 2) 'Cancellation Rate'
FROM Trips
WHERE Client_Id IN (SELECT Users_Id FROM Users WHERE Banned='No')
    AND Driver_Id IN (SELECT Users_Id FROM Users WHERE Banned='No')
    AND Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY Request_at