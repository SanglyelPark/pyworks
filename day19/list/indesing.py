#인덱싱과 슬라이싱
s = "20220126Sunny"
year = s[:4]
day = s[4:8]
weather = s[8:]

print(year)
print(day)
print(weather)

#문자열 수정하기
s2 = "Pithon"
# s2[1] = "y" - 문자열 수정 불가함

s3 = s2[1]

s2 = s2[0] + 'y' + s2[2:]
print(s2)