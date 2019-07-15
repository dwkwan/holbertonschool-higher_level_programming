-- the average temperature (Fahrenheit) by city ordered by temperature (descending)
-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month BETWEEN 7 AND 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
