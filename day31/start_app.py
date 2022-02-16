# 웹 서버 만들기
# 127.0.0.1 주소를 사용하기
from flask import Flask
# 웹 서버 객체 생성
app = Flask(__name__)
# url 결로 설정 -> 제어 함수 정의
@app.route('/') #루트 경로 - 127.0.0.1:5000
def index():
    return "<h1>Hello~ Flask</h1>"

@app.route('/login/')  # 127.0.0.1:5000/login/
def login():
    return "<h1>로그인 페이지 입니다.</h1>"

@app.route('/register/')  # 127.0.0.1:5000/register/
def register():
    return "<h1>회원가입 페이지입니다.</h1>"
@app.route('/register/info/')  # 127.0.0.1:5000/register/
def info():
    return "<h1>회원가입</h1>"

app.run()
