def is_odd(number):
    if number % 2 ==0:
        return True
    else:
        return False
prn = is_odd(4)
print(prn)

is_odd = lambda x: True if x % 2 == 0 else False   #람다와 조건부 표현식
prn2 = is_odd(5)
print(prn2)

def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

prn3 = avg_numbers(1,2,3,4,5)
print(prn3)

f1 = open("test.txt","w")
f1.write("Life is too short!")
f1.close()

f2 = open("test.txt","r")
print(f2.read())
f2.close()

with open("test.txt","w") as f1:
    f1.write("텍스트에 문자열 넣기")
with open("test.txt","r") as f2:
    print(f2.read())

user_input = input("저장할 내용을 입력하세요:")
f = open("test.txt", "a")
f.write(user_input)
f.write("\n")
f.close()

f = open('test.txt','r')
body = f.read()
f.close()

body = body.replace('java','python')

f = open('test.txt','w')
f.write(body)
f.close()




