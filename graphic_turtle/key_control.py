# 키보드로 거북이 조종하기

import turtle as t

def turn_right():
    t.setheading(0)
    t.forward(10)

def turn_up():
    t.setheading(90)
    t.forward(10)

def turn_left():
    t.setheading(180)
    t.forward(10)

def turn_down():
    t.setheading(270)
    t.forward(10)

def clear():
    t.clear()


t.shape("turtle")
t.onkeypress(turn_right,"Right")
t.onkeypress(turn_left,"Left") # 첫글자 대문자로 약속
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(clear, "Escape")  # 지우기
t.listen() # 실행대기

t.mainloop()