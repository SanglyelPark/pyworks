import random

print(" 가위 바위 보 게임")
you = input("당신 : ")
data = ["가위","바위","보"]
# rnd = random.randint(0,2)
# com = choice[rnd]
# print(choice[rnd])
com = random.choice(data)
print("컴퓨터 :", com)

# 게임 연산
if you not in data:   # 오류 처리
    print("잘못된 입력입니다. 다시 입력하세요")

if you == com:
    print("결과 : 무승부")
elif you == "가위" and com == "보":
    print("결과 : 승")
elif you == "바위" and com == "가위":
    print("결과 : 승")
elif you == "보" and com == "바위":
    print("결과 : 승")
elif you == "가위" and com == "바위":
    print("결과 : 패")
elif you == "바위" and com == "보":
    print("결과 : 패")
elif you == "보" and com == "가위":
    print("결과 : 패")
