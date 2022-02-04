# 거북이 대포 게임
import turtle as t
import random as r

def turn_up():
    t.left(2)
def turn_down():
    t.right(2)

def fire():
    while t.ycor() > 0 :
        t.forward(15)
        t.right(5)


t.shape()

#땅 그리기
t.goto(-300,0)
t.goto(300,0)

#목표 지점
target = r.randint(50,150)
t.pensize(2)
t.color("green")
t.up()
t.goto(target-25,2)
t.down()
t.goto(target+25,2)

# 발사위치
t.up()
t.color("black")
t.goto(-200,15)
t.setheading(20)

#거북이 대포 동작
t.onkeypress(turn_up(),"Up")
t.onkeypress(turn_down(),"Down")
t.onkeypress(fire,"space")  #space 소문자
t.listen()

t.mainloop()