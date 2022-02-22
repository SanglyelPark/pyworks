import re

#주민번호 뒷 7자리 '*'로 마스킹

data = """
    kim 951212-1234567
    lee 800101-2345678
    han 770505-3456789
"""

pat = re.compile("(\d{6}[-])\d{7}")
data2 = pat.sub("\g<1>-*******",data)
print(data2)
