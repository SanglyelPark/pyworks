import re

# match()는 첫문자부터 일치하는 검색 -> find()와 유사함
str = "before"
pattern1 = re.compile("[a-z]+")   # 정규 표현식
result = pattern1.match(str) #처음 문자부터 검색
print(result)

pattern2 = re.compile("[0-9]+\s[a-z]+")
result2 = pattern2.match("2022 python")
print(result2)