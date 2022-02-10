# 파일 쓰기
f = open("c:/pyfile/repeat.txt",'w')

for i in range(1,11):
    f.write("%d번째 줄입니다.\n" % i)
f.close()

# 파일 읽기
f = open("c:/pyfile/repeat.txt",'r')
data = f.read()
print(data)
f.close()
