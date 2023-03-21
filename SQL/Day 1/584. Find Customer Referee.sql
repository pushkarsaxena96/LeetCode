# Write your MySQL query statement below
SELECT NAME FROM Customer WHERE COALESCE(referee_id,0) <> 2;