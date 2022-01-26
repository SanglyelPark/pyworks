#최고 점수와 점수의 위치
#정수리스트 생성

score = [70,80,20,90,50]

#최고 점수
max_v = scroe[0]   #0번 인덱스로 최대값으로 설정
for i in score:
    if max_v < i:
        max_v = i

print("최고 점수 : ", max_v)

#최고 점수의 위치
max_idx = 0
n = len(score)
for i in range(1,n):
    if score[max_idx] < score[i]:
        max_idx = i

print("최고 점수의 위치 : ", max_idx)