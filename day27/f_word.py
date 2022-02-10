# 단어 파일 쓰기
word = ['sky','earth','moon','flower','tree','strawberry','grape','garlic','onion']
f = open("./output/word.txt",'w')
for i in word:
    f.write(i + ' ')

f.close()