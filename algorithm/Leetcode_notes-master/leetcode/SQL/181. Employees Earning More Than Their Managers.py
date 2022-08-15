# Write your MySQL query statement below
'''
select emp.Name as Employee
From Employee emp inner join Employee Manager ON emp.ManagerId = Manager.Id
where emp.Salary > Manager.Salary
'''
