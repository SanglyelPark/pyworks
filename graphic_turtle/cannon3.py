import turtle as t
import random


def turn_up():  # 방향키 ↑를 눌렀을 때 호출되는 함수입니다.
    t.left(2)


def turn_down():  # 방향키 ↓를 눌렀을 때 호출되는 함수입니다.
    t.right(2)


def fire():  # SpaceBar를 누르면 거북이 대포를 발사합니다.
    ang = t.heading()  # 현재 거북이가 바라보는 각도를 기억합니다.
    while t.ycor() > 0:  # 거북이가 땅 위에 있는 동안 반복합니다.
        t.forward(15)
        t.right(5)

    d = t.distance(target, 0)  # 거북이와 목표 지점과의 거리를 구합니다.
    t.sety(random.randint(10, 100))  # 성공 또는 실패 지점을 지정합니다.

    if d < 25:  # 거리 차이가 25보다 작으면 명중 했다는 것입니다.
        t.color("blue")
        t.write("Good!", False, "center", ("", 15))  # 해당 줄은 아래에서 설명드리겠습니다.
        t.reset()  # 성공을 하면 화면을 지웁니다.
        game()  # 이후 다시만듭니다.
    else:
        t.color("red")
        t.write("Bad!", True, "center", ("", 15))
        t.color("black")
        t.goto(-200, 10)  # 맞추지 못해 다시 거북이 위치를 원 위치로 되돌립니다.
        t.setheading(ang)  # 각도도 처음 기억해 둔 각도로 되돌립니다.


# 땅을 그립니다.

def game():  # 리 게임을 하기 위해 해당 부분을 함수로 만들기
    t.goto(-300, 0)
    t.down()
    t.goto(300, 0)

    # 목표 타겟을 설정하고 그립니다.
    global target  # 전역변수로 선언
    target = random.randint(50, 150)  # 목표 지점을 50~150 사이에 있는 임의의 수로 지정합니다.

    t.pensize(3)
    t.color("green")
    t.up()
    t.goto(target - 25, 2)
    t.down()  # 거북이의 꼬리를 내리는 것으로 선을 그립니다.
    t.goto(target + 25, 2)  # (즉 거리 -25 ~ 25 까지 선을 그립니다.)

    t.color("black")
    t.up()  # 거북이의 꼬리를 올리는 것으로 선을 그리지 않습니다.
    t.goto(-200, 10)
    t.setheading(20)


game()  # 먼저 첫 게임을 하기 위해 그림을 그리는 함수를 사용합니다.
t.onkeypress(turn_up, "Up")  # ↑를 누르면 turn_up 함수를 실행합니다.
t.onkeypress(turn_down, "Down")  # ↓를 누르면 turn_down 함수를 실행합니다.
t.onkeypress(fire, "space")  # SpaceBar를 누르면 fire 함수를 실행합니다.
t.listen()  # 거북이 그래픽 창이 키보드 입력을 받도록 합니다.

t.mainloop()




