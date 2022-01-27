# set() 메셔드(함수) 사용

#집합 생성
s = {1,2,3}

#요소 추가    - add()
s.add(4)

#요소 삭제      - remove()
s.remove(3)

#전체 삭제      - 빈 집합 - set()
s.clear()


print(s)

# in 집합
fruit = {"사과","바나나","포도"}
print("바나나" in fruit)
print("포도" not in fruit)

for i in fruit:
    print(i , end=" ")  # 순서가 없다. 중복 불허

print()
print(fruit)