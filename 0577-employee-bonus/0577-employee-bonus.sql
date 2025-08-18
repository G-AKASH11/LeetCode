# Write your MySQL query statement below
select name,bonus from Bonus 
right join employee
on employee.empid=bonus.empid
where bonus<1000 or bonus is null;