import threading
# 작업관련 모듈

def repeat():
    print("3초 간격으로 반복 실행")
    timer = threading.Timer(3,repeat)  # 콜백 함수
    timer.start()

repeat()