import re
#sub() 사용하기
p = re.compile('blue|red') # |는 또는
str01 = p.sub('color',"blue socks and red socks")
print(str01)

# sub() 사용 - 출력시엔 객체로 출력(group() 사용한함
pat2 = re.compile("(?P<name>\w+)\s+(?P<phone>\d{3}[-]\d{4}[-]\d{4})")
# m = pat2.sub("\g<name>","park 010-3333-5555")
m = pat2.sub("\g<1>","park 010-3333-5555")
print(m)