class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getname(self):
        return self.name

    def getage(self):
        return self.age


class Employee(Person):  # Person 클래스를 상속 받음
    pass


if __name__ == "__main__":
    e1 = Employee("지민", 30)
    print("이름 :", e1.getname())
    print("나이 :", e1.getage())
# p1 = Person('뷔',28)
# print("이름 :", p1.getname())
# print("나이 : ",p1.getage)
