-- Script to list all records with a score >= 10 ordered by score (top first)

-- Select score and name where score is greater than or equal to 10
SELECT score, name 
FROM second_table 
WHERE score >= 10 
ORDER BY score DESC;
