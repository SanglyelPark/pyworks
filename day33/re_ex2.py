import re

# findall() - 리스트로 반환
str1 = "Two is too"
m1 = re.findall("T[wo]o", str1)
print(m1)

m2 = re.findall("T[wo]o", str1, re.IGNORECASE) #ignorecase - 대소문자 허용
print(m2)