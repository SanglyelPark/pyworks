# 랜덤 위치로 이동
import turtle as t
import random as r


t.shape("turtle")

t.up()
x = r.randint(-500,500)
y = r.randint(-500,500)

t.goto(x,y)

t.mainloop()