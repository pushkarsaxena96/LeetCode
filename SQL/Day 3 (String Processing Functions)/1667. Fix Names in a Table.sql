-- Write your MySQL query statement below
SELECT USER_ID, CONCAT(UCASE(SUBSTRING(NAME, 1, 1)), LOWER(SUBSTRING(NAME, 2))) name
FROM Users
order by user_id