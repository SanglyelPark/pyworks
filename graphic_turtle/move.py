import turtle

turtle.shape("turtle")
turtle.color('blue')

# 이동
# turtle.forward(100)  # forward(거리)
# turtle.right(90) #right(각도)
# turtle.forward(100)  # forward(거리)
# turtle.right(90)
# turtle.forward(100)  # forward(거리)
# turtle.right(90) #right(각도)
# turtle.forward(100)  # forward(거리)
# turtle.right(90) #right(각도)

# for문을 이용함
# 사각형
for i in range(0,4):
    turtle.forward(100)  # forward(거리)
    turtle.right(90)  # right(각도)

turtle.color('red')
for i in range(0,3):
    turtle.forward(100)  # forward(거리)
    turtle.left(120)  # left(각도)

turtle.color("green")
turtle.circle(50)

turtle.mainloop()