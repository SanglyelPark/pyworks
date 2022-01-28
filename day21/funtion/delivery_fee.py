#주문 상품이 가격이 20,000원 미만이면 배송비(2500원) 별도 추가
# 아니면 배송비 포함

def get_price(unit_price, quantity): # 단위당 가격, 수량
    delivery_fee = 2500   #배송비
    price = unit_price * quantity  #상품 주문 가격 = 단위당 가격 * 수량

    if price < 20000:
        price = price + delivery_fee
    else:
        price
    return price

price1 = get_price(15000, 2)  # 배송비 미포함
price2 = get_price(5000, 3)   # 배송비 미포함

# print("상품1 가격 :" + str(price1) + "원")
# print("상품2 가격 :" + str(price2) + "원")
print("상품1 가격 :" , get_price(15000, 2) , "원")
print("상품2 가격 :" ,get_price(5000, 3),  "원")
