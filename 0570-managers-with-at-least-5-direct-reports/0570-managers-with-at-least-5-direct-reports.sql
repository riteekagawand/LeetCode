# Write your MySQL query statement below
select e1.name
from Employee e1
join Employee e2
on e1.Id = e2.managerId 
Group by e2.managerId 
Having count(e2.managerId) >= 5