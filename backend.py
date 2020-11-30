import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("create table if not exists library1(id INTEGER PRIMARY KEY,title text, author text, year integer, ISNB integer)")              ##if index/id taken then ad:- id integer primary key,author text, year integer, ISNB integer)") 
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("select * from library1")
    res=cur.fetchall()
    conn.close()
    return res

def insert(title,author,year,ISNB):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("insert into library1 values(NULL,?,?,?,?)",(title,author,year,ISNB))        
    conn.commit()
    conn.close()

def update(id,title,author,year,ISNB):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("update library1 set title=?,author=?,year=?,ISNB=? where id=?",(title,author,year,ISNB,id))        
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("delete from library1 where id=?" ,(id,))
    conn.commit()
    conn.close()

def search(title="",author="",year="",ISNB=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("select * from library1 where title=? OR author=? OR year=? OR ISNB=?" ,(title,author,year,ISNB))
    res=cur.fetchall()
    conn.close()
    return res

connect()
#insert('Reys on d Earth','Viju Gupta',2018,565656)
#insert('Namaskar','Jeevan',1999,897587)
#update(1,'Reeyy','Wera Sinh',1290,75567878)
#delete(2)
#print(search(author='Jeevan'))
#print(view())


