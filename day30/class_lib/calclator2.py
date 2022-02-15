# MoreCalculator
from day30.class_lib.calculator import Calculator

class MoreCalculator(Calculator):
    def div(self):
        if self.y == 0:
            return 0        #종료
        else:
            return self.x / self.y

cal = MoreCalculator(10, 4)
print(cal.div())
cal2 = MoreCalculator(10,0)
print(cal2.div())
cal3 = MoreCalculator(10,3)
print(cal3.div())
cal4 = Calculator(10,11)  #calculator.py class의 함수 호출가능
print((cal4.mul()))