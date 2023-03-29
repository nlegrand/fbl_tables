from random import randrange
import sqlite3

def simple_table(table_name, column_name, roll, incr=0):
    roll_res = 1
    if roll == "d6":
        roll_res = roll_d6() + incr
        if roll_res > 6:
            roll_res = 6
    elif roll == "d66":
        roll_res = roll_d66() + incr
        if roll_res > 66:
            roll_res = 66
    con  = sqlite3.connect("fbl_sqlite/fbl.db")
    cur  = con.cursor()
    res  = cur.execute(f"SELECT {column_name} FROM {table_name} WHERE d6 = ?", (roll_res,))
    return res.fetchone()[0]

def roll_d6():
    return randrange(1,7)

def roll_d66():
    return randrange(1,7) * 10 + randrange(1,7)
