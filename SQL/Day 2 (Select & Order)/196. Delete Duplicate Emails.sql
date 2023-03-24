-- Please write a DELETE statement and DO NOT write a SELECT statement.
-- Write your MySQL query statement below
DELETE 
from Person 
where id not in (select a.id from (select distinct email, min(id) id from Person group by email) a)