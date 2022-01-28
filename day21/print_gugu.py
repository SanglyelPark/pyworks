# 구구단을 출력하는 함수

def print_gugu(dan):
    for i in range(1, 10):
        # print(dan, "x", i,"=",dan *i)
        print("%d * %d = %d"  % (dan, i,dan*i)) #변수그룹은 괄호로 묶어야 함


print_gugu(6)   #함수 호출

