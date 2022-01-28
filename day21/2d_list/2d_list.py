# 2차원 리스트
a = [
    [10,20],
    [30,40],
    [50,60]
]
print("리스트 크기(행) : ", len(a) )
print("리스트 크기(행) : ", len(a[0] ))

#특정 요소 출력
print("a[1][0] = ", a[1][0])
print("a[2][1] = ", a[2][1])

# 리스트 추가
a.append([70,80])

#전체 요소 출력
for x, y in a:
    print(x,y)
print()


#전체 요소 출력(이중for문)
for i in range(0, len(a)):
    for j in range(0,len(a[i])):
        print(a[i][j],end = " ")
    print()