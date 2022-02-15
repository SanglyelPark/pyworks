# raise 구문 - 예외 미뤄두기
# 사용하는 곳에서 예외 처리 해줌

class Animal:
    def cry(self):
        # print("동물이 웁니다.")
        raise NotImplemented  # 아직 구현되지 않음
    # 기본 생성자(멤버변수가 없을때) 생략

class Dog(Animal):
    # pass
    def cry(self):
        print("왈 ~ 왈 ~")

class Cat(Animal):
    def cry(self):
        print("야 ~ 옹!")

dog = Dog()
dog.cry()

cat = Cat()
cat.cry()
