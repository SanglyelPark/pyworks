#Customer 클래스 생성
class Customer:
    def __init__(self, cid, name):
        self.cid = cid          #고객 아이디
        self.name = name        #고객 이름
        self.cgrade = "SILVER"  #고객 등급
        self.bonus_point = 0    #보너스 포인트
        self.bonus_ratio = 0.01 #보너스 적립율 - 1%
    def calc_price(self, price):        # 가격 및 보너스 포인트 계산
        #보너스 포인트 = 보너스 포인트 + (가격 * 보너스적립율)
        self.bonus_point += int(price * self.bonus_ratio)
        return price

    def getname(self):
        return self.name   #고객의 이름을 반환하는 메서드

    def __str__(self):
        return self.name + "님의 등급은 " + self.cgrade + \
            "이고, 보너스 포인트는 " + str(self.bonus_point) + "점 입니다."


if __name__ == "__main__":
    silver = Customer(1001, "정국")  # 클래스를 부르면 자동으로 __init__ __str__ 실행된다.
    price = 10000
    cost = silver.calc_price(price)
    print(silver.getname() + "님의 구매 비용은 " + str(cost) + "원 입니다.")
    print(silver)