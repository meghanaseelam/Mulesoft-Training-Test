#import sqlite3 module
import sqlite3

#connect with database file
con= sqlite3.connect('Movies.db')
print(con)
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS MoviesINFO(Name VARCHAR,Actor VARCHAR,Actress VARCHAR,Director VARCHAR,YearofRelease DATE)')

con.commit()
con.close()