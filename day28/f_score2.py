# 학생의 성적을 저장하는 파일 만들기
# 이름 국어 수학 - 추신수 90 80
with open("./output/scorelist.txt", 'a') as f:
    while True:
        key = input("성적을 저장할까요? (y/n) : ")
        if key =='n' or key == 'N':
            break
        elif key == 'y' or key == 'Y':
            name = input("이름 입력 : ")
            kor = input("국어 점수 : ")
            math = input("수학 점수 : ")

            f.write(name + ' ')
            f.write(kor + ' ')
            f.write(math + '\n')
        else:
            print("잘못된 입력입니다. 다시 입력하세요")

print("입력을 종료합니다.")