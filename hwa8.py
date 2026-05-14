import pandas as pd
import numpy as np

import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)
print('Opened data successfully')

df = pd.read_sql("""SELECT *
                 FROM SQLite_master
                 WHERE type='table';""", conn)

print(df)

player_match = pd.read_sql("""SELECT *  
                        FROM Player_Match;""", conn)

print(player_match.head())

null_player_match = pd.read_sql("""SELECT *
                        FROM Player_Match
                        WHERE TEAM_id IS NULL;""", conn)

print(null_player_match)

toss_dec = pd.read_sql("""SELECT *
                        FROM Match""", conn)

print(toss_dec.head())

null_match = pd.read_sql("""SELECT *
                        FROM Match
                        WHERE MATCH_WINNER IS NULL""",conn)

print(null_match)