-- Start by deleting any tables if the exist already
-- We want to be able to re-run this script as needed.
-- DROP tables in reverse order of creation 
-- DROP dependent tables (with foreign keys) first
-- Makes the script idempotent (rerunnable) using the most current statements each time we run

DROP TABLE IF EXISTS nhl_players;
DROP TABLE IF EXISTS nhl_teams;

-- Create the nhl_teams table 
-- Note that the nhl_teams table has no foreign keys, so it is a standalone table

CREATE TABLE nhl_teams (
    author_id TEXT PRIMARY KEY,
    first_name 
    last_name TEXT,
    year_born INTEGER
);

-- Create the books table
-- Note that the books table has a foreign key to the authors table
-- This means that the books table is dependent on the authors table
-- Be sure to create the standalone authors table BEFORE creating the books table.

CREATE TABLE books (
    book_id TEXT PRIMARY KEY,
    title TEXT,
    year_published INTEGER,
    author_id TEXT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);