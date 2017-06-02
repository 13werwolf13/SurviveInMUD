#import sqlalchemy
import sqlite3

def printcharacterinfo():
    conn = sqlite3.connect('gamedb.db')

    curs = conn.cursor()
    curs.execute('SELECT * FROM character')
    conn.commit()

    print(curs.fetchall())
