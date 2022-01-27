#secore 리스트 생성과 저장
score = [70,80,20,90,100,50]

#합계

sum_v = 0

# for i in score:
#     sum_v  += i

#for in range()
for i in range(0,len(score)):
    sum_v += score[i]

# 평균 계산
avg = sum_v / len(score)

print("평균 : ", avg)
print("합계 : ",sum_v)
print("평균 : %.2f"% avg)  # %d- 정수 대응, %f-실수 대응문자

#내장함수 - sum()
print("합계 : ",sum([70,80,20,90,100,50]))
print("합계 : ",sum(score))

# 내장 함수 - max()
print("최고 점수 : ",max(score))
print("최고 점수 : ",min(score))
