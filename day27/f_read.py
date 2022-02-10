#파일 읽기 ,  읽기모드 'r'
try:
    f = open("c:/pyfile/test.txt",'r')
    text = f.read()
    print(text)
    f.close()

    f = open("c:/pyfile/number.txt",'r')
    data = f.read()
    print(data)
    f.close()
except FileNotFoundError:
    print("파일을 열 수 없습니다.")