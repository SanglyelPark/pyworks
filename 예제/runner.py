import turtle
import random
import time

d = 10000

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.penup()
t2.penup()
t1.color('red')
t2.color('blue')
t1.shapesize(5)
t2.shapesize(5)
t1.shape('turtle')
t2.shape('turtle')

while True:
    print("보유자금:", d)
    col = (input("red or blue(종료하려면 stop)"))
    if col == 'stop':
        print('얻은 자금:', d)
        break
    m = int((input("betting your money")))

    t1.goto(random.uniform(200, -200), random.uniform(200, -200))
    t2.goto(random.uniform(200, -200), random.uniform(200, -200))
    t1.goto(-200, 100)
    t2.goto(-200, -100)

    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(0.5)

    t1.fd(random.randint(100, 400))
    t2.fd(random.randint(100, 400))
    t = t1.xcor()
    tt = t2.xcor()

    if t > tt:
        if col == 'red':
            d = d + m
            print('당신의 거북이가 이겼습니다!')
        else:
            d = d - m
            print('당신의 거북이가 졌습니다...')

    if t < tt:
        if col == 'blue':
            d = d + m
            print('당신의 거북이가 이겼습니다!')
        else:
            d = d - m
            print('당신의 거북이가 졌습니다...')

    if d <= 0:
        print('파산...')
        time.sleep(2)
        break