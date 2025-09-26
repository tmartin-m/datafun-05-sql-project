-- Create the nhl_teams table 
-- Note that the nhl_teams table has no foreign keys, so it is a standalone table

CREATE TABLE nhl_teams (
    TEAM_ID TEXT PRIMARY KEY,
    TEAM TEXT,
    GAMES_PLAYED INTEGER,
    WINS INTEGER,
    LOSSES INTEGER,
    POINTS INTEGER,
    GOALS_FOR INTEGER,
    GOALS_AGAINST INTEGER
);

-- Create the nhl_players table
-- Note that the nhl_players table has a foreign key to the nhl_teams table
-- This means that the nhl_players table is dependent on the nhl_teams table
-- Be sure to create the standalone nhl_teams table BEFORE creating the nhl_players table.

CREATE TABLE nhl_players (
    PLAYER TEXT PRIMARY KEY,
    SKATER_SHOOTS TEXT,
    POSITION TEXT,
    GAMES_PLAYED INTEGER,
    GOALS INTEGER,
    ASSISTS INTEGER,
    POINTS INTERGER,
    PENALTY_MINUTES INTEGER,
    SHOTS INTEGER,
    SHOOTING_PERCENTAGE INTEGER,
    TEAM_ID TEXT,
    FOREIGN KEY (TEAM_ID) REFERENCES nhl_teams(TEAM_ID)
);
