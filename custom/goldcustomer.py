from custom.customer import Customer


class Goldcustomer(Customer):
    def __init__(self, cid, name):
        super().__init__(cid, name) # 고객 아이디와 이름은 상속
        self.cgrade = "GOLD"  # 고객등급
        self.sale_ratio = 0.1  #구매 할인율
        self.bonus_ratio = 0.02  # 보너스 적립율

    def calc_price(self, price):
        # 할인된 가격 = 가격 * 구매 할인율
        price -= int(price * self.sale_ratio)
        self.bonus_point += int(price * self.bonus_ratio)
        return price

if __name__ == "__main__":
    gold = Goldcustomer(1002, '지민')
    price = 10000
    cost = gold.calc_price(price)
    print(gold.getname() + "님의 구매 비용은 " + str(cost) + "원 입니다.")
    print(gold)