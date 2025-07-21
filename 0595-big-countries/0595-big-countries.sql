# Write your MySQL query statement below
select name, population, area
from World
where area >= 3000000 
Union
select name, population, area
from World
where population  >= 25000000