-- Table definitions for the tournament project.
-- Last edited: oct 22, 2017

-- check if database 'tournament' already exists; if so, delete and create an (empty) database
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

-- psql code to connect to the database
\c tournament

-- create a table to keep track of player identification information
CREATE TABLE players
(
    player_id serial primary key
  , name varchar(100) -- assumes names are <100 characters long...
  -- prepare columns to store standings information
  -- set defaults to 0 so that newly registered players start off correctly
  , wins integer DEFAULT 0 -- +1 for each win
  , matches integer DEFAULT 0 -- +1 for each match they compete in
)
;

-- create a table to track match outcomes
-- note: a match must be between two different players
-- note: we assume there are no draws in a match
CREATE TABLE matches
(
    match_id serial primary key
  , winner integer
  , loser integer
  -- add constraint to make sure matches have legal pairings
  , CONSTRAINT valid_pairing CHECK (winner <> loser)
)
;

-- create a view of just player_ids and names, ranked by wins
-- and with a match_pair column that assigns adjacent players together
-- in descending order of wins.
-- this table will help make the match pairing query easier
CREATE VIEW rankedPlayers AS
    SELECT
        player_id
      , name
      , NULL as match_pair
    FROM players
    ORDER BY wins
;
-- use cross join to create the match_pair sequence
-- TO FIX: need to figure out how to append a column to existing VIEW
, (SELECT i.n
  FROM generate_series(1, (SELECT count(player_id)/2 FROM players)) as i(n),
    generate_series(1, 2))
  as match_pair
