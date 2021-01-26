# Write your MySQL query statement below
'''
select Person.FirstName, Person.LastName, Address.City, Address.State
From Person LEFT JOIN Address ON Person.PersonId = Address.PersonId;
'''
'''
用A left join B ON  可以使两个table 结合 以A 为基础
'''