# 커피 자동판매기 프로그램

coffee = 5

while True:
    money = int(input("돈을 넣어 주세요 : "))
    if money == 400:
        print("커피가 나옵니다.")
        coffee -= 1  # coffee = coffee -1
        #break
    elif money > 400:
        print("커피가 나오고 거스름돈 " + str(money-400) + "원을 돌려 줍니다.")
        coffee -= 1
    else:
        print("커피가 나오지 않습니다.")

    print("남은 커피의 양은 " + str(coffee) + "개 입니다.")

    # 커피가 모두 소진되면 판매 중지
    if coffee == 0:
        print("커피가 모두 소진 되었습니다. 판매를 중지합니다.")
        break