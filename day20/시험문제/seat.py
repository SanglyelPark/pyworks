#입장객 수에 따른 줄수 계산
customer = int(input("입장객 수 : "))
col = int(input("열의 수 : "))

if customer % col == 0 :
    row = customer // col
else:
    row = int(customer / col) + 1
print("줄(행) 수 :" ,row)

#좌석 배치
for i in range(0,row):
    for j in range(1,col+1):
        num = i* col + j
        if num > customer:
            break
        print("좌석" + str(num), end=" ")
    print()
    



