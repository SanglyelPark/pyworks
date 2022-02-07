# Student 클래스 정의와 사용

class Student:
    def __init__(self,name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return "이름 : {}, 학년 : {}".format(self.name,self.grade)

    def learn(self):
        return "수업을 듣습니다."

if __name__ == "__main__":
    s1 = Student('콩쥐',1)
    # print("이름 : ", s1.name)
    # print("학년 : ", s1.grade)
    print(s1)

    s2 = Student('팥쥐',2)
    # print("이름 : ", s2.name)
    # print("학년 : ", s2.grade)
    print(s2)

