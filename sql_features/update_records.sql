-- Update the position of a player
UPDATE nhl_players
SET POSITION = 'C'
WHERE TEAM_ID = 'COL';

-- Correct the goals of a player
UPDATE nhl_players
SET GOALS = 30
WHERE TEAM_ID = 'VGK';