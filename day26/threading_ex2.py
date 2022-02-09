import threading
import datetime

# 5초후에 타이머 종료
def call():
    print("타이머 종료")
    print(datetime.datetime.today())

# call()
print(datetime.datetime.today())
timer = threading.Timer(5,call)
timer.start()