-- displays the max temperature of each state
SELECT state, MAX(value) 'mac_temp'
FROM temperatures, GROUP BY state