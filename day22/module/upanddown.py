import random as r

# 컴퓨터가 1 -100중 난수를 저장

com = r.randint(1,100)
min_v = 1
max_v = 100

for i in range(10):
    try: #문자 입력시 오류처리(try ~ except) 사용
        guess = int(input("맞혀 보세요([%d회] %d ~ %d ) : "% (i+1,min_v,max_v))) # 숫자 입력

        #정답일때 - '정답', guess가 클때 '너무커요, 아니면 '너무작아요'
        if guess > com:
            print("너무 커요")
            max_v = guess
        elif guess < com:
            print("너무 작아요")
            min_v = guess
        else:
            print("정답")
            break
    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력해 주세요")

print("점수 : %d점"%((10-i )*10))

