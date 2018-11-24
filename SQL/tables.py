import sqlite3

conn=sqlite3.connect('Main.db')

c=conn.cursor()




c.execute("CREATE TABLE channel (id INTEGER PRIMARY KEY AUTOINCREMENT, channel_name text NOT NULL, no_subs INTEGER, avg_viewers INTEGER, future INTEGER)")
c.execute("CREATE TABLE customer(cust_id INTEGER PRIMARY KEY AUTOINCREMENT, cust_name text)")
c.execute("CREATE TABLE rating(rat_id INTEGER PRIMARY KEY AUTOINCREMENT ,chan_id INTEGER, customer_id INTEGER, rating INTEGER, rate_date date, FOREIGN KEY (chan_id) REFERENCES "channel"([id]), FOREIGN KEY (customer_id) REFERENCES "customer"([cust_id]))")



# Run the file and remove the comments from it, thereadter.
conn.commit()
# updated
conn.close()
