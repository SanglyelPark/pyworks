pocket = ["paper","cellphone"]
card = True
if "money" in pocket:
    print("택시를 타고 가라")
else:
    print("카드를 꺼내라")
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어가라")