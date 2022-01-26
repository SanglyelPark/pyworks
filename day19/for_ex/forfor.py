#이중 for문
for i in range(0,5):
    for j in range(0,5):
        print('$', end='')
    print()

#직각 삼각형 모양
for i in range(0,5):
    for j in range(0, i+1):
        print('$', end='')
    print()


#역직각 삼각형 모양
for i in range(0,5):
    for j in range(0, 5-i):
        print('$', end='')
    print()
