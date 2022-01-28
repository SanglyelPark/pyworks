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
sum_subject = [0, 0]
avg_subject = [0, 0, 0, 0]

for i in range(0, len(score)):
    sum_subject[0] += score[i][0]
    sum_subject[1] += score[i][1]

avg_subject[0] = sum_subject[0] /n
avg_subject[1] = sum_subject[1] /n

print("수학 총점 : %d 점" % sum_subject[0])
print("영어 총점 : %d 점" % sum_subject[0])
print("수학 평균 : %d 점" % avg_subject[1])
print("영어 평균 : %d 점" % avg_subject[1])

