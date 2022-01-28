# 전역변수(global variable)의 유효 범의(scope)

def one_up():
    global x       # global 키워드 - 전역 변수임을 표시
    x = x+1
    return x

x =1   #메인 영역에 변수를 선언하면 전역변수가 됨
print(one_up())
print(one_up())
print(one_up())
print(x)  