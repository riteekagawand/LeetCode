# Write your MySQL query statement below
select email AS Email
from Person 
group by email
having COUNT(*) >1