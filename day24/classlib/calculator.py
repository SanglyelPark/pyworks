# 계산기 클래스 정의 와 사용

class Calculator:
    def __init__(self):
        self.x = 0

    def add(self, y):
        self.x = self.x + y
        return self.x

    def sub(self,y):
        self.x -= y
        return self.x



c1 = Calculator()
c1.x = 10
print("x = ",c1.x)
print("x = " + str(c1.add(11)))
print("x = " + str(c1.sub(12)))

c2 = Calculator()
print("x = ",c2.add(10.1))
print("x = ",c2.sub(2.5))


