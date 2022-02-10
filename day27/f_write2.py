# 파일에 숫자 데이터 쓰기
# 숫자는 문자로 형변환 해야함
f = open("c:/pyfile/number.txt",'w')
# f.write(10)
f.write(str(10) + '\n')
f.write(str(3.14) + '\n')

num = 10 * 3.14 # 산술 연산
num2 = 10 > 11  # bool 연산
f.write(str(num) + '\n')
f.write("%.2f" % num + '\n')
f.write(str(num2) + '\n')

f.close()