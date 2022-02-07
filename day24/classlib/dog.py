# Dog 클래스 정의 및 사용

class Dog:
    type = "진돗개"
    def __init__(self,name):
        self.name = name #인스턴스 멤버 변수
        # self.type = type

dog1 = Dog("백구")
dog2 = Dog("검둥이")

print(dog1.name) #dog1만 유일
# print(dog1.type) # 모든 dog이 공유
print(Dog.type) #클래스 이름으로 직접 접근

print(dog2.name) #dog2만 유일
print(dog2.type)