#리스트 내포
#[표현식 for 항목 in 리스트]

a = [ 1,2,3,4,5]
a2 = []
a3 = []
a4 = []



# 3의 배수이면서 찍수인 수
for i in a:
    if i % 2 == 0:
        a2.append(i*3)

print("a2 = ", a2)

# 리스트 내포 구문 - 3의 배수
a3 = [i*3 for i in a]
print("a3 = ", a3)

# 리스트 내포 구문 - 3의 배수이면서 짝수
a4 = [i*3 for i in a if i % 2 == 0]
print("a4 = ", a4)