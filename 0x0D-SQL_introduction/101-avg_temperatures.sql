-- Calculate the average temperature (Fahrenheit) by city and order by descending average temperature

SELECT 
    city, 
    ROUND(AVG(temperature), 4) AS avg_temp
FROM 
    temperatures
GROUP BY 
    city
ORDER BY 
    avg_temp DESC;
