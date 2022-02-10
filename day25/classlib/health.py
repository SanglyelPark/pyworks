# health 클래스

class Health:
    def __init__(self,name):
        self.__name = name
        self.__hp = 0

    def sethp(self,hp):
        if hp < 0:
            hp = 0
        if hp > 100:
            hp = 100

        self.__hp = hp

    def gethp(self):
        return self.__hp

    def getname(self):
        return self.__name

    def exercise(self,hours):  # 1시간 입력 hp = 1
        self.sethp(self.__hp + hours)
        print("{}시간 운동하다.".format(hours))

    def drink(self,alcohol):   # 술 1병에 hp = 1
        self.sethp(self.__hp - alcohol)
        print("술을 {}잔 마시다.".format(alcohol))

p1 = Health("이몽룡")
p1.sethp(70)
p1.exercise(3)
p1.drink(4)
print(p1.getname(), p1.gethp())
print('*'*20)
p2 = Health("성춘향")
p2.sethp(100)
p2.exercise(2)
p2.drink(1)
print(p2.getname(), p2.gethp())