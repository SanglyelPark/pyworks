# 거듭제곱 함수 만들기

def myabs(x):
    if x < 0:
        return  -x
    else:
        return x

def mypow(x,y):
    num = 1
    for i in range(0,y):
        num *= x
    return num
        # print(" i = ",i,"num = ", num)

if __name__=="__main__":
    print(myabs(-10))

    #절대값 호툴
    print(myabs(-10))

    print(mypow(2,4))
    print(mypow(5,3))
