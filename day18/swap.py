#변수 값 교환하는 프로그램
# 파란 상자에는 1이 저장, 빨강 상자에는 2가 저장됨

blue = 1
red = 2


#출력
print("교환전")
print("blue =", blue,"red =", red)


"""
#변수값 바꾸기 - 임시 변수 temp
temp = blue
blue = red
red = temp
"""
#파이썬 교환처리
blue, red = red, blue

#출력
print("교환후")
print("blue =", blue,"red =", red)
