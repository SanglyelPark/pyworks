def add(a, b):
    return a+b

print(3,4)
a = add(3,4)
print(a)

def say():
    return "HI"
print(say())


def add(a, b):
    print("%d , %d의 합은 %d입니다." % (a,b,a+b))

add(5,6)


def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result
result = add_many(1,2,3)
print(result)
result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul("add", 1,2,3,4,5)
print(result)

result = add_mul("mul", 1,2,3,4,5)
print(result)

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name="foo",age=3)

def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s입니다." % nick)

say_nick("야호")
say_nick("바보")

