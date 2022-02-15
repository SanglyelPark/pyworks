# willdb.db에 접속
import sqlite3

sqlite3.connect("c:/mydb/willdb.db")

def getconn():
    conn = sqlite3.connect("c:/mydb/willdb.db")
    return conn

def create_table():
    # member table 생성
    conn = getconn()
    cur = conn.cursor()
    sql = """
        CREATE TABLE member (
    	memberId 	char(5) PRIMARY KEY,
	    passwd 		char(10) NOT NULL,
 	    name		TEXT NOT NULL,
 	    gender		char(4),
 	    age			INTEGER )
 	    """
    cur.execute(sql)
    conn.commit()
    conn.close()


def select_member():
    conn = getconn()
    cur = conn.cursor()   #db 작업 객체
    # print("연결", conn)
    cur = conn.cursor()
    sql = "SELECT * FROM member"
    cur.execute(sql)
    rs = cur.fetchall() #리스트로 반환(값은 튜플구조)
    print(rs)
    conn.close()

def select1_member():
    conn = getconn()
    cur = conn.cursor()  # db 작업 객체
    sql = "SELECT * FROM member WHERE memberId = ?"
    # sql = "SELECT memberId, passwd FROM member WHERE memberId = ?"
    cur.execute(sql, ('10003',)) # 자료가 1개인 경우 콤마(,)를 붙임 - 튜플 자료구죠
    rs = cur.fetchone()
    print(rs)
    conn.close()


def insert_member():
    conn = getconn()
    cur = conn.cursor()
    # 정적 바인딩 형식
    # sql = "INSERT INTO member(memberId, passwd, name, gender, age) VALUES ('10002', 'M123456780', '민정', '여자',24)"
    # 동적 바인딩
    sql = "INSERT INTO member(memberId, passwd, name, gender, age) VALUES (?, ?, ?, ?, ?)"
    cur.execute(sql, ('10003', 'M123456782', '희민', '여자', 29))  # 실행
    cur.execute(sql, ('10004', 'M123456781', '성민', '남자', 35))  # 실행
    conn.commit()
    conn.close()


# 메인 영역
# create_table()
# insert_member()
select1_member()


