import turtle as t
import random

def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_down():
    t.setheading(270)

def turn_left():
    t.setheading(180)

def play():
    t.forward(10)  # 10 픽셀 이동
    angle = te.towards(t.pos())
    te.setheading(angle) # 주인공 거북이쪽을 바라봄
    te.forward(9)

    if t.distance(te) >= 12: # 주인공 거북이가 적 거북이와의 거리가 12이상일때
        t.ontimer(play, 100)  # 0.1 초 간격으로 play 콜백

    # 주인공 거북이가 먹이에 닿으면 새로운 위치로 이동
    if t.distance(tf) < 12:
        x = random.randint(-230, 230) #
        y = random.randint(-230, 230)
        tf.goto(x,y)

# 주인공 거북이
t.shape("turtle")
t.setup(500,500)
t.bgcolor("orange")
t.color("white")
t.speed(0)
t.up()

#적 거북이
te = t.Turtle()
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0,200)

# 먹이
tf = t.Turtle()
tf.shape("circle")
tf.color("green")
tf.speed(0)
tf.up()
tf.goto(0,-200)

#키 작동
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(turn_left, "Left")
t.listen()
play()

t.mainloop()