#문자열 출력함수 -format()
from sys import set_coroutine_origin_tracking_depth


print("I eat {} apples".format(3))

n = 5
print("I eat {} apples".format(n))

day = 2
print("I eat {} apples, I was sick for {} days".format(n,day))

# '+' 연산자로 출력
sentence = "I eat " +str(n) + "apples, I was sick for" + str(day)+" days"
print(sentence)

#회원 정보 출력하기
name = input("이름 : " )
user_id = input("아이디 : ")
user_pw = input("비밀번호 :")
user_pw = '*' * len(user_pw)


print("이름 : {}".format(name))
print("아이디 : {}".format(user_id))
print("비밀번호  : {}".format(user_pw))
