# 5명의 수학, 영어 과목의 총점과 평균
# 과목별 총점과 평균

score = [
                [80,70],
                [70,70],
                [60,93],
                [50,70],
                [75,70]
            ]

n = len(score)

# 개인별 총점과 평균
total = 0
print("총점 평균")

for i in range(0,n):
    total = score[i][0] + score[i][1]
    print(total, total/2)

#과목별 총점

math_sum = 0
eng_sum = 0

for i in range(0, len(score)):
    math_sum += score[i][0]
    eng_sum += score[i][1]

math_avg = math_sum / n
eng_avg = eng_sum / n

print("수학 총점 : " +str(math_sum) + "점")
print("영어 총점 : " +str(eng_sum) + "점")
print("수학 평균 : " +str(math_avg) + "점")
print("영어 평균 : " +str(eng_avg) + "점")

