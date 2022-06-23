import sqlite3
con= sqlite3.connect('Movies.db')
print(con) 

con.cursor()


con.execute("INSERT INTO Movies VALUES('One Day','Jim Sturgess','Anne Hathaway','Lone Scherfig','2011-12-23')")
con.execute("INSERT INTO Movies VALUES('La La Land','Ryan Gosling','Emma Stone','Damien Chazelle','2016-09-12')")
con.execute("INSERT INTO Movies VALUES('You've Got Mail','Tom Hanks','Meg Ryan','Nora Ephron','1998-12-18')")
con.execute("INSERT INTO Movies VALUES('Oceans Eleven','George Clooney','Julia Roberts','Gary Ross','2001-05-21')")


con.commit()
con.close()