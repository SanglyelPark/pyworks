# Counter 클래스 정의와 사용
class Counter:
    x = 0

    def __init__(self):
        self.x = 0
        Counter.x = Counter.x + 1

    def getcounter(self):
        return Counter.x


c1 = Counter()
# print(c1.x)
print(c1.getcounter())

c2 = Counter()
# print(c1.x)
print(c2.getcounter())

c3 = Counter()
print(c3.getcounter())