# 장바구니 클래스

class Cart:
    a = []

    def __init__(self, goods):
        Cart.a.append(goods)

    def __str__(self):
        return Cart.a

cart1 = Cart("계란")
print(cart1.a)

cart2 = Cart("두부")
print(cart2.a)

cart3 = Cart("멸치")
print(cart3.a)

#전체 요소 출력
for c in Cart.a:  # 클래스 이름으로 접근
    print(c,end=" ")


