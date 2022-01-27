#딕셔너리 생성과 사용
d = {'진' : 30, '슈가' : 28}
print(d)

# 요소 추가
d['지민'] = 27

#요소 삭제 - pop()
d.pop('슈가')

#전체 요소
for key in d:
    print(key, ':', d[key])


# 모든 키 가져오기 - d.keys()
print(d.keys())
print(list(d.keys()))

# 모든 키 가져오기 - 
print(d.values())
print(list(d.values()))

#모든 키와 값 가져오기
for key, val in d.items():
    print(key,val)