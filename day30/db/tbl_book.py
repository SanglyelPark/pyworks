# 도서 db 만들기
import sqlite3 as sql

def getconn():
    # 데이터 베이스 생성 및 접속
    conn = sql.connect("./book.db")
    return conn

def create_table():
    con = getconn()
    cursor = con.cursor()
    sql = """
        CREATE TABLE book(
            book_no INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            publisher TEXT NOT NULL,
            page INTEGER )"""
    cursor.execute(sql)
    con.commit()
    con.close()

def insert_book():
    con = getconn()
    cursor = con.cursor()
    sql = "INSERT INTO book (title, publisher, page) VALUES (?,?,?)"
    # book_no는 자동이므로 입력하면 안됨
    cursor.execute(sql, ('점프 투 파이션', '박응용', 350))
    con.commit()
    con.close()

def select_book():
    con = getconn()
    cursor = con.cursor()
    sql = "SELECT * FROM book"
    cursor.execute(sql)
    rs = cursor.fetchall()
    for i in rs:
        print(i)
    con.close()

def select_book_one():
    con = getconn()
    cursor = con.cursor()
    sql = "SELECT * FROM book WHERE book_no = ?"
    cursor.execute(sql, (2,))  # 튜플 1개일때 콤머 붙임
    rs = cursor.fetchall()
    print(rs)
    con.close()

def update_book():
    con = getconn()
    cursor = con.cursor()
    sql = "UPDATE book SET page = ? WHERE book_no = ?"
    cursor.execute(sql, (400, 2))
    con.commit()
    con.close()

def delete_book():
    con = getconn()
    cursor = con.cursor()
    sql ="DELETE FROM book WHERE book_no = 1"
    cursor.execute(sql)
    con.commit()
    con.close()

if __name__ == "__main__":
    # con = getconn()
    # print(con, "연결됨")
    # create_table()
    insert_book()
    #select_book()
    #select_book_one()
    #update_book()
    #delete_book()

