# 두수를 매개로 전달하여 서루 같은면 곱하고
# 서루 다르면 더하는 함수를 정의하고 호출
def data(x,y):
    if x == y:
        return x*y
    else:
        return x+y

n1 = data(5,5)
n2 = data(5,6)
print(n1)
print(n2)
