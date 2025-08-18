# Write your MySQL query statement below
select project.project_id,round( avg(experience_years),2) as average_years
from employee
join project
on employee.employee_id = project.employee_id
group by project.project_id;