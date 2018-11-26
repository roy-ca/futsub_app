import sqlite3

conn=sqlite3.connect('Main.db')

c=conn.cursor()


c.execute('''CREATE TABLE channel1 (channel_name text NOT NULL PRIMARY KEY, no_subs INTEGER, avg_viewers INTEGER, avg_rating INTEGER)''')

c.execute('''CREATE TABLE customers1 (cust_name text NOT NULL PRIMARY KEY)''')


c.execute('''CREATE TABLE ratings2 ( chan_id INTEGER, customer_id INTEGER, ratings INTEGER, FOREIGN KEY (chan_id) REFERENCES "channel" ([id]),FOREIGN KEY (customer_id) REFERENCES "customer"([cust_id]) )''')




# Run the file and remove the comments from it, thereadter.
conn.commit()
# updated
conn.close()
