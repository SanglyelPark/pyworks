import turtle as t

t.setup(500,500)   #무대의 크기
t.bgcolor('red')  #배경색
t.color('yellow')   # 선색
t.pensize(3)

n = 50

t.speed(0)
for x in range(n):
    t.circle(80)
    t.left(360/n)

t.mainloop()