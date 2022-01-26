#구구단 출력

dan = int(input("단을 입력하세요 : "))
for i in range(1,10):
    # print(dan, "x", i, "=" ,(dan*i))
    print("{} * {} = {}".format(dan, i, dan*i))