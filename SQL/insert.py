import sqlite3

conn=sqlite3.connect('Main.db')

c=conn.cursor()

c.execute('''INSERT INTO channel1 VALUES("Coldplay", 13238300, 14000000,-1)''')
c.execute('''INSERT INTO channel1 VALUES("pewdiepie", 70000000, 15000000,-1)''')
c.execute('''INSERT INTO channel1 VALUES("T-series", 71000000, 12345, -1)''')

conn.commit()

conn.close()
