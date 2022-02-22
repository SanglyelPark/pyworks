import re
# 이름과 전화번호를 분리
#()는 그룹으로 분리
#group(인덱스)

str01 = "jang  010-1234-5678"
pat = re.compile("(\w+)\s{1,2}(\d{3}[-]\d{4}[-]\d{4})")
m = pat.match(str01)
print(m.group())
print(m.group(1))   #group(인덱스번호)
print(m.group(2))   #group(인덱스번호)

# group(그룹이름)
pat2 = re.compile("(?P<name>\w+)\s+(?P<phone>\d{3}[-]\d{4}[-]\d{4})")
m2 = pat2.match(str01)
print(m2.group("name"))
print(m2.group("phone"))