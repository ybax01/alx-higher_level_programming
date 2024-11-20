-- 16-no_link.sql
-- Script to list records with a name value, sorted by descending score

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
