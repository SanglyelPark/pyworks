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


def start():
    global playing
    if playing == False:
        playing = True  # 게임 시작
        t.clear()   # 화면지우기
        play()   # play 함수 호출

def message(m1,m2):
    t.clear()
    t.goto(0,100)
    t.write(m1,False,"center",("",20))   # 메세지 출력 중앙에 20크기
    t.goto(0, -100)
    t.write(m2, False, "center", ("", 16))
    t.home()

def play():
    global playing
    global score
    if playing:
        t.ontimer(play,100)

    t.forward(10)
    if random.randint(1,5) == 2:  # 1~5 중에서 뽑은 수가 2일 확률(20%)
        angle = te.towards(t.pos())     # 내 거북이의 각도를 적색 거북이에게 전달
        te.setheading(angle)
    speed = score + 5
    te.forward(speed)  #적 거북이 속도

    # 먹이에 닿으면
    if t.distance(tf) < 12:
        score += 1
        t.write(score)
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        tf.goto(x,y)

    #적 거북이에 닿으면
    if t.distance(te) < 12:
        text = "Score : " + str(score)
        message("Game over",text)
        playing = False
        score = 0

# 점수수와 게 스위치
playing = False
score = 0

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
t.onkeypress(start, "space")

t.listen()
message("Turtle Run","[Space]")

t.mainloop()