import  turtle as t
import time

# 1초 간격으로 사각형 그리기
t.shape("turtle")
t.up()
t.goto(0,0)
t.down()
time.sleep(1)
t.goto(0,100)
time.sleep(1)
t.goto(100,100)
time.sleep(1)
t.goto(100,0)
time.sleep(1)
t.goto(0,0)
t.mainloop()