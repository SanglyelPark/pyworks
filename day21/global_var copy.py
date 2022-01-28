# 1~100까지의 자연수 중 4의 배수와 개수를 출력하는 프로그램

from os import times

def get_times(n):
    for i in range(1, 101):
        global count
        if i % 4 == 0:
            print(i, end=" ")
            count = count + 1

count = 0

get_times(4)
print("배수의 개수 : " , count)
