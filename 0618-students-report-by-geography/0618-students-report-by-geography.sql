# Write your MySQL query statement below


with T1 as (Select name as 'America', row_number() over(partition by continent order by name) as r1 from student where continent = 'America'),

T2 as (Select name as 'Asia', row_number() over(partition by continent order by name) as r2 from student where continent = 'Asia'),

T3 as (Select name as 'Europe', row_number() over(partition by continent order by name) as r3 from student where continent = 'Europe')


Select america, asia, europe from T1
left join t2 on t1.r1 = t2.r2
left join t3 on t1.r1 = t3.r3;