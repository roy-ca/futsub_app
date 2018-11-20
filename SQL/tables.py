import sqlite3

conn=sqlite3.connect('Main.db')

c=conn.cursor()




c.execute("CREATE TABLE youtuber (id INTEGER PRIMARY KEY, channel_name text NOT NULL, no_subs INTEGER, avg_viewers INTEGER, future INTEGER)")




# Run the file and remove the comments from it, thereadter.
conn.commit()
# updated
conn.close()
