# return이 있는 함수의 정의와 호출

def one_up(x):
    return x + 1

#두 수의 차를 구하는 함수
def sub(x , y):
    return x - y

# 절대값을 구하는 함수
def my_abs(a):
    if a < 0 :
        return -a
    else:
        return a

num1 = one_up(1)   #호출후에 반환값이 저장
print(num1)  #호출

num2 = sub(5,6)
print(num2)

num3 = my_abs(-10)
num4 = my_abs(10)
print(num3)
print(num4)

# 내장 함수 abs()
print(abs(10))
