# Write your MySQL query statement below
SELECT max(SALARY) AS SecondHighestSalary FROM EMPLOYEE
where salary < (select max(salary) from employee);
