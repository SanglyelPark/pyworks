import re

str1 = "Two is too"
m1 = re.findall("T[wo]o", str1)
print(m1)

m2 = re.findall("T[wo]o", str1, re.IGNORECASE)
print(m2)