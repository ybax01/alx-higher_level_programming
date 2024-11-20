-- Script to list all records of second_table ordered by score (top first)

-- Select score and name, ordering by score in descending order
SELECT score, name 
FROM second_table 
ORDER BY score DESC;
