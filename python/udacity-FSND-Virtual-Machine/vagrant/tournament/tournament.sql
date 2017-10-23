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
  --, round integer
  --, player_1 integer references players(player_id)
  --, player_2 integer references players(player_id)
  , winner integer
  , loser integer
  -- add constraint to make sure matches have legal pairings
  --, CONSTRAINT valid_pairing CHECK (player_2 <> player_1)
  -- add constraint to make sure the winner is one of the two players in match
  --, CONSTRAINT valid_winner CHECK (winner = player_1 OR winner = player_2)
)
;

/*
-- create a flat table that makes it easy to return a list of players
-- and their tournament record
CREATE VIEW scoreboard AS
  SELECT
      player_id
    , name
    -- calculate number of wins per player
    , count(*) FILTER (WHERE winner = player_id) AS wins
    -- calculate number of matches played per player
    , count(player_1) FILTER (WHERE player_1 = player_id) +
      count(player_2) FILTER (WHERE player_1 = player_id)
        AS matches
  FROM players INNER JOIN matches ON matches.winner = players.player_id
  ORDER BY wins DESC
;
*/
