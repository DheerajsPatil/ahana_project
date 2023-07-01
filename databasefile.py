import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ahana.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS clients(cid INT, name TEXT, contact INT, email TEXT, address TEXT, insta TEXT, facebook TEXT)")
    con.commit()


create_db()