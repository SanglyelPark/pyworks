# 입력 받아 파일에 쓰기

with open('./output/input.txt', 'a') as f:
    text = input("저장할 내용을 입력하세요 : ")
    f.write(text)
    f.write('\n')