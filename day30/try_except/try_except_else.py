# try ~ except ~ else
# 에러가 없으면 try ~  else 실행
# 에러가 있으면 try ~ except 실행

try:
    print("1번")
    with open("c:/pyfile/season.txt", 'r') as f:
        season = f.readlines()
        # print(season)

except FileNotFoundError:
    print("2번")
else:
    print("3번")
    for s in season:
        print(s, end='')


