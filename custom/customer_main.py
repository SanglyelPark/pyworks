from custom.customer import Customer
from custom.goldcustomer import Goldcustomer
from custom.vipcustomer import VIPCustomer

silver = Customer(101, "놀부")
gold = Goldcustomer(102, "흥부")
vip = VIPCustomer(103, "심청", 777)


price = 10000
cost_s = silver.calc_price(price)
cost_g= gold.calc_price(price)
cost_v = vip.calc_price(price)
print(silver.getname() + "님의 구매 비용은 " + str(cost_s) + "원입니다.")
print(gold.getname() + "님의 구매 비용은 " + str(cost_g) + "원입니다.")
print(vip.getname() + "님의 구매 비용은 " + str(cost_v) + "원입니다.")
print(silver)
print(gold)