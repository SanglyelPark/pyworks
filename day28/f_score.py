# 학생의 성적을 저장하는 파일 만들기
# 이름 국어 수학 - 추신수 90 80
with open("./output/score.txt", 'a') as f:
    name = input("이름 입력 : ")
    kor = input("국어 점수 : ")
    math = input("수학 점수 : ")

    f.write(name + ' ')
    f.write(kor + ' ')
    f.write(math + '\n')

