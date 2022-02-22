import sqlite3

def getconn():
    conn = sqlite3.connect("c:/dbtest/test.db")
    return conn

def create_table():
    conn = getconn()
    cur = conn.cursor()
    sql = """
        CREATE TABLE member (
        mid     char(5) PRIMARY KEY,
        passwd  char(8) NOT NULL,
        name    TEXT NOT NULL,
        age     INTEGER)
        """
    cur.execute(sql)
    conn.commit()
    print("테이블 생성")
    conn.close()

def insert_member():
    conn = getconn()
    cur = conn.cursor()
    sql = "INSERT INTO member(mid, passwd, name, age) VALUES (?, ?, ?, ?)"
    cur.execute(sql, ('10001', 'son0123', '손흥민', 30))
    conn.commit()
    conn.close()

def select_member():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM member"
    cur.execute(sql)
    rs = cur.fetchall()
    print(rs)
    conn.close()

# create_table()
#insert_member()
select_member()
