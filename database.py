import sqlite3

con = sqlite3.connect("gamelogs.db")

cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS game_log(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    character_name TEXT,
    generation INTEGER, 
    action TEXT, 
    value INTEGER, 
    floor INTEGER
    )""")

con.commit()

def log(character_name, generation, action, value, floor):
    cur.execute("""
    INSERT INTO game_log(
        character_name,
        generation,
        action,
        value,
        floor
    )
    VALUES (?,?,?,?,?)
    """, (character_name, generation, action, value, floor))
    con.commit()
    con.close()