import sqlite3

conn=sqlite3.connect('Main.db')

c=conn.cursor()

c.execute('''INSERT INTO youtuber VALUES(8, "Coldplay", 13238300, 14000000, 12345)''')
c.execute('''INSERT INTO youtuber VALUES(9, "pewdiepie", 70000000, 15000000, 12345)''')
c.execute('''INSERT INTO youtuber VALUES(7, "T-series", 71000000, 12345, 50000)''')
conn.commit()

conn.close()
