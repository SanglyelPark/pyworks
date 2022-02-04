#기본 매개변수
def sayhello(text, count = 1):
    for i in range(count):
        print(text)


#가변 매개변수- '*'가 붙으면 리스트로 간주
def calc_sum(*number):
    sum_v = 0
    for i in number:
        sum_v += i
    return sum_v

#키워드 매개변수 - '**'가 붙으면 딕셔너리 형태로 저장됨
def print_kw(**kwargs):
    print(kwargs)

sayhello("Hello")
sayhello("Hello", 3)

print(calc_sum(1,2))
print(calc_sum(1,2,3,4))

print_kw(name='지민')
print_kw(name='지민', age = 30)