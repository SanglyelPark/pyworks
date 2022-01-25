#키 반복 동작

while True:
    key = input("반복을 계속 할까요?(y/n)")

    if key == 'y':
        print("반복을 계속합니다.")
    elif key == 'n':
        print("반복을 중단합니다.")
        break
    else:
        print("키를 잘못 눌렸습니다.")
        
