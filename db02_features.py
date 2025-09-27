import sqlite3

# Connect to the database
conn = sqlite3.connect("project.sqlite3")
cursor = conn.cursor()

# --- Delete players by team ---
cursor.execute("""
DELETE FROM nhl_players WHERE TEAM_ID IN ('NYR');
""")

# --- Delete players that scored less than 90 points ---
cursor.execute("""
DELETE FROM nhl_players WHERE POINTS < 90;
""")

# --- Update the position of a player ---
cursor.execute("""
UPDATE nhl_players
SET POSITION = 'C'
WHERE TEAM_ID = 'COL';
""")

# --- Correct the goals of a player ---
cursor.execute("""
UPDATE nhl_players
SET GOALS = 30
WHERE TEAM_ID = 'VGK';
""")

# --- Add a new column if it doesn't exist ---
try:
    cursor.execute("ALTER TABLE nhl_players ADD COLUMN LAST_UPDATED TEXT")
except sqlite3.OperationalError as e:
    print(f"Column may already exist: {e}")

# --- Update the new column with a timestamp ---
cursor.execute("""
UPDATE nhl_players
SET LAST_UPDATED = datetime('now');
""")

# Commit changes and close connection
conn.commit()
conn.close()

print("Database operations completed successfully.")