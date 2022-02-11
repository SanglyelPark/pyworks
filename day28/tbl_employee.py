# DB  사원 관리
import sqlite3

def select_emp():
    conn = sqlite3.connect("c:/mydb/willdb.db") # 연결 객체 생성
    cur  = conn.cursor()  # 작업 객체 생성
    sql = "SELECT * FROM employee" #검색 SQL 언어
    cur.execute(sql)
    #자료 가져오기
    rs = cur.fetchall()  #rs-resulte set
    print(rs)
    for i in rs:
        print(i)
    conn.close()

def insert_emp():
    # 사원 정보 삽입
    conn = sqlite3.connect("c:/mydb/willdb.db")
    cur = conn.cursor()
    sql = "INSERT INTO employee(emp_id, name, age) VALUES ('e102','안산',21)"
    cur.execute(sql)
    # conn.commit()
    conn.close()

def updata_emp():
    #사원 정보 수정
    conn = sqlite3.connect("c:/mydb/willdb.db")
    cur = conn.cursor()
    sql = "UPDATE employee SET salary = 30000 WHERE emp_id = 'e103'"
    cur.execute(sql)
    conn.commit()
    conn.close()

def select_one():
    #특정한 사원 1명 검색
    conn = sqlite3.connect("c:/mydb/willdb.db")
    cur = conn.cursor()
    # sql = "SELECT * FROM employee WHERE emp_id = 'e101'"
    sql = "SELECT * FROM employee ORDER by salary DESC"
    cur.execute(sql)
    rs = cur.fetchone()
    print(rs)
    conn.close()

def delete_emp():
    conn = sqlite3.connect("c:/mydb/willdb.db")
    cur = conn.cursor()
    sql ="DELETE FROM employee WHERE emp_id = 'e103'"
    cur.execute(sql)
    conn.commit()
    conn.close()

# insert_emp()
delete_emp()
select_emp()

    # 사원 전체 검색

