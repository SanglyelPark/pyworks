#구구단 전체 출력
# for i in range(2,10):
#     for j in range(1,10):
#         print("{} * {} = {}".format(i,j,i*j))
#     print()

#구구단 가로 출력
for i in range(1,10):
    for j in range(2,10):
        # print("{} * {} = {}".format(j,i,i*j), end=' ')
        print("%d * %d = %3d"%(j,i,j*i), end=" | ")
    print()