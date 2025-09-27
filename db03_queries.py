# -------------------------------------------------
# Imports
# -------------------------------------------------
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------
# Database Connection
# -------------------------------------------------
# Replace with your database path or connection string
conn = sqlite3.connect("project.sqlite3")  

# -------------------------------------------------
# Helper function to run queries and return DataFrame
# -------------------------------------------------
def run_query(query: str) -> pd.DataFrame:
    return pd.read_sql_query(query, conn)

# -------------------------------------------------
# Queries from your list
# -------------------------------------------------

# 1. Count all rows
df_count = run_query("SELECT COUNT(*) AS total_rows FROM nhl_players;")
print("\nTotal Rows:\n", df_count)

# 2. Average points
df_avg_points = run_query("SELECT AVG(POINTS) AS avg_points FROM nhl_players;")
print("\nAverage Points:\n", df_avg_points)

# 3. Combine functions
df_combined = run_query("SELECT AVG(POINTS) AS avg_points, COUNT(*) AS total_players FROM nhl_players;")
print("\nAverage Points & Player Count:\n", df_combined)

# 4. Total games played
df_total_games = run_query("SELECT SUM(GAMES_PLAYED) AS total_games FROM nhl_players;")
print("\nTotal Games Played:\n", df_total_games)

# 5. Average penalty minutes per position
df_penalties = run_query("""
SELECT POSITION, AVG(PENALTY_MINUTES) AS avg_penalty_minutes
FROM nhl_players
GROUP BY POSITION;
""")
print("\nAverage Penalty Minutes per Position:\n", df_penalties)

# 6. Players with > 100 points
df_high_scorers = run_query("SELECT * FROM nhl_players WHERE POINTS > 100;")
print("\nPlayers with > 100 Points:\n", df_high_scorers.head())

# 7. Total and average points by position
df_points_by_pos = run_query("""
SELECT POSITION, SUM(POINTS) AS total_points, AVG(POINTS) AS avg_points
FROM nhl_players 
GROUP BY POSITION;
""")
print("\nPoints by Position:\n", df_points_by_pos)

# 8. Inner join between nhl_teams and nhl_players
df_join = run_query("""
SELECT nhl_teams.TEAM, nhl_teams.WINS, nhl_players.PLAYER, nhl_players.GAMES_PLAYED
FROM nhl_teams
INNER JOIN nhl_players ON nhl_teams.TEAM_ID = nhl_players.TEAM_ID;
""")
print("\nJoined Teams & Players:\n", df_join.head())

# 9. Sort players by points ascending
df_sorted_players = run_query("SELECT * FROM nhl_players ORDER BY POINTS;")
print("\nPlayers Sorted by Points:\n", df_sorted_players.head())

# -------------------------------------------------
# Visualization Examples
# -------------------------------------------------

# Average penalty minutes by position
df_penalties.plot(kind="bar", x="POSITION", y="avg_penalty_minutes", legend=False)
plt.title("Average Penalty Minutes by Position")
plt.ylabel("Avg Penalty Minutes")
plt.xlabel("Position")
plt.show()

# Total vs. average points by position
df_points_by_pos.plot(kind="bar", x="POSITION")
plt.title("Total & Average Points by Position")
plt.ylabel("Points")
plt.show()

# Distribution of points across players
df_sorted_players["POINTS"].plot(kind="hist", bins=20, edgecolor="black")
plt.title("Distribution of Player Points")
plt.xlabel("Points")
plt.show()

# -------------------------------------------------
# Close connection
# -------------------------------------------------
conn.close()

