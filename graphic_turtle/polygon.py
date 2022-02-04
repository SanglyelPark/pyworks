#다각형 그리기
import turtle as t


def polygon(n):
    for i in range(n):
        t.forward(100)
        t.left(360/n) # 다각형의 내각 공식

t.shape()
polygon(5)
polygon(3)
t.mainloop()