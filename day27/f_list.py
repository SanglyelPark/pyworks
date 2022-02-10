#  파일에 리스트 쓰기 읽기

season = ['봄','여름','가을','겨울']
f = open("c:/pyfile/season.txt",'w')

for i in season:
    f.write(i + '\n')

# n = len(season)
# for i in range(0,n):
#     f.write(season[i] + '\n')

f.close()
# 파일 읽기
try:
    f = open("c:/pyfile/season.txt",'r')
    season = f.read()
    print(season)
    # print(season[0])
    # print(season[2:3])
    f.close()
except:
    print("파일을 열 수 없습니다.")