# 파일쓰기
# 파일 열기 - open(경로, 모드)
f = open("c:/pyfile/test.txt",'w')
# 파일 쓰기
f.write("안녕하세요 \n")
f.write("Have a nice day \n")
# 파일 닫기 / 종료
f.close()