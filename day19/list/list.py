#리스트의 복사
a = [1,2,3,4,5]
a2 = []
a3 =[]

print("a =", a)

#복사 
for i in a:
    a2.append(i)
print("a2 =", a2)

# 홀수 저장
for i in a:
    if i % 2 ==1:
        a3.append(i)

print("a3 =", a3)
