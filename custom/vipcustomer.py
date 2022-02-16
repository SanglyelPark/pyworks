from custom.customer import Customer

class VIPCustomer(Customer):
    # vip 고객 - 전문 상담원
    def __init__(self, cid, name, agent):
        super().__init__(cid, name)
        self.agent = agent
        self.cgrade = "VIP"  # 고객등급
        self.sale_ratio = 0.1  # 구매 할인율
        self.bonus_ratio = 0.05  # 보너스 적립율

    def calc_price(self, price): #함수 이름은 같고 내용이 다름
        # 할인된 가격 = 가격 * 구매 할인율
        price -= int(price * self.sale_ratio)
        self.bonus_point += int(price * self.bonus_ratio)
        return price

    def __str__(self):
        return  super().__str__() + " 전문상담원은 " \
                + str(self.agent) + " 입니다."


if __name__ == "__main__":
    vip = VIPCustomer(1004, "RM", 777)
    price = 10000
    cost = vip.calc_price(price)
    print(vip.getname() + "님의 구매 비용은 " + str(cost) + "원 입니다.")
    print(vip)  # vip 객체정보