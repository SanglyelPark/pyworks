# 기본 매개변수 
# 매개변수를 초기화하여 선언하고 함수 호출시 배개 변수를 

from itertools import count


def print_string(text, count=1):
    for  i in range(count):
        print(text)


print_string("Hello")
print("="*30)
print_string("Hello", 3)