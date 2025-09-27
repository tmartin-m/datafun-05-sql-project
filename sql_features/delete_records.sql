-- Delete players by team
DELETE FROM nhl_players WHERE TEAM_ID IN ('NYR');

-- Delete players that scored less than 90 points
DELETE FROM nhl_players WHERE POINTS < 90;