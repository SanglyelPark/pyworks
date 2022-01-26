#Q3

from dataclasses import replace
from posixpath import split


pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

print(pin[7]) 


a = "a:b:c:d"
b = a.replace(":","#")
c = a.split(":")
print(b)
print(c)

