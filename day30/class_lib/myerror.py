# 사용자 예외 클래스 만들기
# 원기은 Exception 클래스를 상속 받아야함
class Myerror(Exception):
    #pass
    def __str__(self):
        return "허용되지 않는 별명입니다."
def say_nick(nick):
    if nick == '바보' or nick == '나쁜놈':
        raise Myerror()

    print(nick)

try:
    say_nick('하늘')
    say_nick('바보')
    say_nick('나쁜놈')
except Myerror as e:
    print(e)