# 클래스의 정의와 사용

class Student:
    def __init__(self):
        self.name = '콩쥐'   #멤버 변수
        self.grade = 1

    def learn(self):
        print("수업을 듣습니다.")

s = Student()  # 인스턴스 = 클래스()
print("이름 : ",s.name) #멤버 접근은 점(.) 연산자 사용용
print("학년 : ",s.grad)
s.learn()