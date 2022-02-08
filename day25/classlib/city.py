# city 클래스 생성

class City:
    a = ["Seoul","Incheon","Daejeon","Jeju","dokdo"]

str1 = " "
for c in City.a:
    str1 += c[0]   #str1 = str1 + c[0]

print(str1)