import sqlite3
import pandas as pd
import pathlib

# Define the database file in the current root project directory
db_file = pathlib.Path("project.sqlite3")

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def create_tables():
    """Function to read and execute SQL statements to create tables"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql", "creating_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)

def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        teams_data_path = pathlib.Path("data", "nhl_teams.csv")
        players_data_path = pathlib.Path("data", "nhl_players.csv")
        teams_df = pd.read_csv(teams_data_path)
        players_df = pd.read_csv(players_data_path)
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            teams_df.to_sql("teams", conn, if_exists="replace", index=False)
            players_df.to_sql("players", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)

def main():
    create_database()
    create_tables()
    insert_data_from_csv()

if __name__ == "__main__":
    main()
