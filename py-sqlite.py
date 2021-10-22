import sqlite3

def create_table():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS store(Item TEXT,Quantity INTEGER,Price REAL)')
    conn.commit()
    conn.close()

def insert_value(item,quantity,price):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("INSERT into store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()


def view_db():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    rows = cur.execute("SELECT * FROM store")
    views = rows.fetchall()
    conn.commit()
    conn.close()
    return views

print(view_db())
