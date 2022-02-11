# 구구단을 파일에 쓰기
with open("./output/gugudan.txt", "w") as gugu:
    for i in range(2,10):
        for j in range(1,10):
            gugu.write("%d * %d = %d" % (i,  j, i*j ))
            gugu.write('\n')
        gugu.write('\n')

