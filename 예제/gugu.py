def gugu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n*i)
        i += 1
    return result

print(gugu(6))

result = 0
for n in range(1,1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n

print(result)

