-- count all rows
SELECT COUNT(*) FROM nhl_players; 

-- get average points
SELECT AVG(POINTS) FROM nhl_players;

-- combine functions
SELECT AVG(POINTS), COUNT(*) FROM nhl_players;

-- Calculate the total salary expense
SELECT SUM(GAMES_PLAYED) AS TOTAL_GAMES FROM nhl_players;

-- Average penalty minutes per position
SELECT POSITION, AVG(PENALTY_MINUTES) AS AVG_PENALTY_MINUTES
FROM nhl_players
GROUP BY POSITION;
