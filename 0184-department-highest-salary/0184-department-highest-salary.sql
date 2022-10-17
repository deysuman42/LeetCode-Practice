# Write your MySQL query statement below

# select
#   department,
#   employee,
#   salary
# from
#   (
#     Select
#       d.name as 'department',
#       e.name as 'employee',
#       e.salary,
#       dense_rank() over(
#         partition by e.departmentId
#         order by
#           e.salary desc
#       ) as rnk
#     from
#       employee e
#       inner join department d on e.departmentid = d.id
#   ) x
# where
#   rnk = 1;

Select
      d.name as 'department',
      e.name as 'employee',
      e.salary
      
      from employee e join department d
      ON e.departmentId = d.id
      
      where (e.departmentId, e.salary) in 
      
      (select departmentId, max(salary) from employee
      group by departmentid)
