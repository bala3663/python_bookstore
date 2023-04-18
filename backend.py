import sqlite3


def connect():
    conn=sqlite3.connect("shopdata1.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookstore(id INTEGER PRIMARY KEY,tittle TEXT,author Text,year INTEGER,isbn INTEGER)")
    conn.commit()
    conn.close()



def insert(tittle,author,year,isbn):
    conn=sqlite3.connect("shopdata1.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO bookstore VALUES(null,?,?,?,?)",(tittle,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("shopdata1.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM bookstore")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(tittle="",author="",year="",isbn=""):
    conn=sqlite3.connect("shopdata1.db")#database name
    cur=conn.cursor()
    cur.execute("SELECT * FROM bookstore WHERE tittle=? OR author=? OR year=? OR isbn=?",(tittle,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("shopdata1.db")#database name
    cur=conn.cursor()
    cur.execute("DELETE FROM bookstore WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,tittle,author,year,isbn):
    conn=sqlite3.connect("shopdata1.db")#database name
    cur=conn.cursor()
    cur.execute("UPDATE bookstore SET tittle=?,author=?,year=?,isbn=? where id=?",(tittle,author,year,isbn,id))
    conn.commit()
    conn.close()



