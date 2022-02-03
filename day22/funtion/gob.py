# 1부터 n까지 곱하기(1*2*3...*n)

def get_gob(n):
    gob = 1   # 곱하기는 1부터 초기화
    for i in range(2,n+1):
        gob *= i
    return gob

#재귀 함수로 정의
def facto(n):
    if n <= 1:
        return 1
    return n * facto(n-1)

# n = 4
# 4 * facto(3)
# 4 * 3 = facto(2)
# 4*3*2 = facto(1)

print(get_gob(4))
print(facto(5))