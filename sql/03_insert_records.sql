-- Insert teams data
INSERT INTO nhl_teams (TEAM_ID,TEAM,GAMES_PLAYED,WINS,LOSSES,POINTS,GOALS_FOR,GOALS_AGAINST)
VALUES
    ('TBL','Tampa Bay Lightning',82,47,27,102,292,216),
    ('EDM','Edmonton Oilers',82,48,29,101,259,235),
    ('BOS','Boston Bruins',82,33,39,76,222,271),
    ('TOR','Toronto Maple Leafs',82,52,26,108,267,229),
    ('WPG','Winnipeg Jets',82,56,22,116,275,190),
    ('VGK','Vegas Golden Knights',82,50,22,110,274,214),
    ('COL','Colorado Avalanche',82,49,29,102,273,231),
    ('PIT','Pittsburgh Penguins',82,34,36,80,242,287),
    ('UTA','Utah Hockey Club',82,38,31,89,240,247),
    ('NYR','New York Rangers',82,39,36,85,255,255),
    ('MTL','Montréal Canadiens',82,40,31,91,243,261);

-- Insert players data
INSERT INTO nhl_players (PLAYER,SKATER_SHOOTS,POSITION,GAMES_PLAYED,GOALS,ASSISTS,POINTS,PENALTY_MINUTES,SHOTS,SHOOTING_PERCENTAGE,TEAM_ID)
VALUES
    ('Nikita Kucherov','L','R',78,37,84,121,45,265,14,'TBL'),
    ('Nathan MacKinnon','R','C',79,32,84,116,41,320,10,'COL'),
    ('Leon Draisaitl','L','C',71,52,54,106,34,240,21.7,'EDM'),
    ('David Pastrnak','R','R',82,43,63,106,42,319,13.5,'BOS'),
    ('Mitchell Marner','R','R',81,27,75,102,14,173,15.6,'TOR'),
    ('Connor McDavid','L','C',67,26,74,100,37,196,13.3,'EDM'),
    ('Kyle Connor','L','L',82,41,56,97,25,267,15.4,'WPG'),
    ('Jack Eichel','R','C',77,28,66,94,8,233,12,'VGK'),
    ('Cale Makar','R','D',80,30,62,92,14,246,12.2,'COL'),
    ('Sidney Crosby','L','C',80,33,58,91,31,227,14.5,'PIT'),
    ('Brandon Hagel','L','L',82,35,55,90,58,228,15.4,'TBL'),
    ('Clayton Keller','L','R',81,30,60,90,28,218,13.8,'UTA'),
    ('Artemi Panarin','R','L',80,37,52,89,16,237,15.6,'NYR'),
    ('Nick Suzuki','R','C',82,30,59,89,8,172,17.4,'MTL');
