# Write your MySQL query statement below
select Email from (select Email, count(*) from Person
group by email
having count(*) > 1)ab;