import sqlite3

conn = sqlite3.connect('check.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1,'2016-01-11 13:53:39','Python',267777)")
    conn.commit()
    c.close()
    conn.close()
    
create_table()
data_entry()
