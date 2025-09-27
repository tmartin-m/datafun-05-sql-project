-- Example of an Inner join between nhl_teams and nhl_players
SELECT nhl_teams.TEAM, nhl_teams.WINS, nhl_players.PLAYER, nhl_players.GAMES_PLAYED
FROM nhl_teams
INNER JOIN nhl_players ON nhl_teams.TEAM_ID = nhl_players.TEAM_ID;