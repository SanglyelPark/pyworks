#다각형 그리기
import turtle as t


def polygon(n):
    for i in range(n):
        t.forward(50)
        t.left(360/n) # 다각형의 내각 공식

def polygon2(n, d):
    for i in range(n):
        t.forward(d)
        t.left(360/n) # 다각형의 내각 공식

t.shape() #기본으로 생략 가능 화살표
polygon(5)
polygon(3)
t.up()   # 펜 올리기
t.forward(100)
t.color('blue')
t.down()  # 펜 내리기

polygon2(3,100)
polygon2(5,100)

t.mainloop()