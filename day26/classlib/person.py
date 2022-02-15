class Person:  #부모 클래스
    def __init__(self, name, age):  # 생성자(함수)
        self.name = name            # 멤버 변수
        self.age = age

    def getname(self):              #부모클래스의 멤버를 공유
        return self.name

    def getage(self):
        return self.age


class Employee(Person):  # Person 클래스를 상속 받음, 자식 클래스
    pass


if __name__ == "__main__":
    e1 = Employee("지민", 30)
    print("이름 :", e1.getname())
    print("나이 :", e1.getage())

    e2 = Employee("진", 28)
    print("이름 : " + e2.getname())
    print("나이 : "+ e2.getage())


# p1 = Person('뷔',28)
# print("이름 :", p1.getname())
# print("나이 : ",p1.getage)
