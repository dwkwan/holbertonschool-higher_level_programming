-- the max temperature of each state (ordered by State name)
-- displays the the max temperature of each state (ordered by State name)
SELECT state, MAX(value) as avg_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
