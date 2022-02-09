# Airplane 을 상속받을 SuperSonicAirPlane
from day26.classlib.airplane import AirPlane


class SuperSonicAirPlane(AirPlane):
    NORMAL = 1   #클래스 변수
    SUPERSONIC = 2

    def __init__(self):
        self.fly_mode = SuperSonicAirPlane.NORMAL

    def fly(self):  # 메서드 재정의(오바라이딩 - overriding)
        if self.fly_mode == SuperSonicAirPlane.SUPERSONIC:
            print("초음속 비행합니다.")
        else:
            # print("비행기가 비행합니다.")
            super().fly() #부모 메서드 상속받음