import sqlite3

conn=sqlite3.connect('Main.db')

c=conn.cursor()

c.execute('''INSERT INTO youtubers VALUES(5,"test",2,26000000)''')

conn.commit()

conn.close()
