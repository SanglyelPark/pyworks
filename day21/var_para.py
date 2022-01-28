# 가변 매개변수 
# 매개변수를 입력값이 정해지지 않고 변경해야 할때 사용하는 변수
# 변수이름 앞에 '*'를 붙임


from audioop import avg


def cale_avg(*number):
    sum_v = 0 
    for i in number:
        sum_v += 1

    avg = sum_v / len(number)
    return avg
    
avg1 = cale_avg(1,2)
avg2 = cale_avg(1,2,3)


print(avg1)
print(avg2)
