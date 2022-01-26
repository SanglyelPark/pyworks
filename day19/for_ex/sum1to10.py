#1부터 10까지의 합계
sum_v =0
for i in range(1,11):
    sum_v += i
    print("i =", i,"sum_v = ",sum_v)

print("합계 : ",sum_v)

#입력받아서 1부터 n가지의 합계
n = int(input("숫자 입력 : "))
sum_v = 0
for i in range(1,n+1):
    sum_v += 1

print("합계 : ", sum_v)

#     #1부터 10까지의 곱하기
# facto = 1
# for i in range(1,11):
#     facto *=i
#     print("i =", i,"facto = ",facto)

# print("곱한 결과 :",facto)