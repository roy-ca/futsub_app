import sqlite3

conn=sqlite3.connect('Main.db')

c=conn.cursor()

c.execute('''INSERT INTO channel VALUES(1, "Coldplay", 13238300, 14000000,-1)''')
c.execute('''INSERT INTO channel VALUES(2, "pewdiepie", 70000000, 15000000,-1)''')
c.execute('''INSERT INTO channel VALUES(3, "T-series", 71000000, 12345, -1)''')

conn.commit()

conn.close()
