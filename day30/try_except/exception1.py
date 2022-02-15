#예외 처리
# 다중 try ~ except 구문
try:
    data = [10, 50, 33, 74]
    x = input("정수 입력(0~3까지 입력해 주세요) : ")
    n = int(x)
    print(data[n])
except IndexError:
    print("인덱스 번호를 잘못 입력했습니다.")
except ValueError:
    print("입력값에 문제가 있습니다.")