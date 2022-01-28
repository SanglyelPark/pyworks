#리스트를 매개변수로 전달하여 계산하기

def get_list(a):
    a2 = []
    for i in a:
        a2.append(i * 3)
    return a2

def get_avg(a):
    sum_v = 0
    for i in a:
        sum_v += i

    avg = sum_v / len(a) 
    return avg


v = [1,2,3,4,5]

# v의 요소에 3의 배수를 저장하는 리스트
v2 = get_list(v)

#v의 요소의 평균 계산하기
average = get_avg(v)

print(v2)
print(average)