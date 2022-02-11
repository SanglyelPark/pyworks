# 이미지 파일 복사하기 - 읽고 쓰기

with open('activity.jpg', 'rb') as f1:
    data = f1.read()

with open('./output/activity.jpg', 'wb') as f2:
    f2.write(data)
