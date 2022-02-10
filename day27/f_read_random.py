import random
# slplit() - 문자열 다루는 함수 - 구분기호로 분리해서 리스트로 반환
f = open("c:/pyfile/season.txt",'r')
season = f.read().split()  # 데이터를 공백문자 구분해서 리스트로 반환
print(season)
print(season[1])
word = random.choice(season)
print(word)
f.close()