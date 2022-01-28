# 지역변수(local variable)의 유효 범의(scope)

def one_up():
    x = 1
    x = x+1
    return x

print(one_up())
print(one_up())
#print(x)  not defined x error