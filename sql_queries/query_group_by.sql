-- Get the total points and average points by position
SELECT POSITION, SUM(POINTS), AVG(POINTS) 
FROM nhl_players 
GROUP BY POSITION;