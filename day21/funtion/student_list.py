#딕셔너리로 성적 통계 출력

student = [
                {"name":"이대한", "kor" : 80, "eng" : 80, "math" : 75},
                {"name":"박민국", "kor" : 70, "eng" : 65, "math" : 60},
                {"name":"오상식", "kor" : 75, "eng" : 70, "math" : 53},
                {"name":"최지능", "kor" : 95, "eng" : 90, "math" : 90}
]
n = len(student)
print("개수 : ", len(student))

#개인별 총점과 평균
total = 0  # 개인별 총점

print("===== 총점 평균")
for std in student:
    total = std["kor"] + std["eng"] + std["math"]
    avg = total /3
    print("%s %d %.1f" % (std["name"], total,avg))

#과목별 총점과 평균
sum_subj = [0,0,0]
avg_subj = [0.0, 0.0, 0.0]

#과목별 총점
for std in student:
    sum_subj[0] +=  std["kor"]
    sum_subj[1] +=  std["eng"]
    sum_subj[2] +=  std["math"]

#과목별 평균
avg_subj[0] = sum_subj[0] /n
avg_subj[1] = sum_subj[1] /n
avg_subj[2] = sum_subj[2] /n

#과목별 총점 출력
print("국어 합계 : %d점" % sum_subj[0])
print("영어 합계 : %d점" % sum_subj[1])
print("수힉 합계 : %d점" % sum_subj[2])

#과목별 평균 출력
print("국어 평균 : %.1f점" % avg_subj[0])
print("영어 평균 : %.1f점" % avg_subj[1])
print("수학 평균 : %.1f점" % avg_subj[2])