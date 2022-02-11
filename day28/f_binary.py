# 바이너리 파일을 쓰고 읽기

with open('./output/data.bin', 'wb') as f:
    text = "비가 내린다."
    f.write(text.encode())  # 코드화 - 0과 1로 기계어로 변환

with open('./output/data.bin', 'rb') as f:
    data = f.read()
    print(data)
    print(data.decode()) # 복호 - 다시 문자로 변환

