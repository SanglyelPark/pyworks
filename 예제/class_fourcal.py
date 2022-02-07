class FourCal:
    def __init__(self,first,second):   # 메서드 선언
        self.first = first
        self.second = second
    # def setdata(self,first,second):
    #     self.first = first
    #     self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


a = MoreFourCal(4,2)
print(a.pow())
a = MoreFourCal(4,0)
print(a.div())


# a = FourCal()
# b = FourCal()
# a.setdata(4,2)   메서드를 선언하면 setdata로 데이터를 지정 할 필요가 없다.
# b.setdata(3,8)
# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.div())
# print(b.add())
# print(b.mul())
# print(b.sub())
# print(b.div())

# a = FourCal(4,2)
# print(a.first)
# print(a.second)
# print(a.add())
# print(a.div())
#
# b =FourCal(8,2)
# print(b.first)
# print(b.second)
# print(b.add())
# print(b.div())