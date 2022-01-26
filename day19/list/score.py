#리스트의 함수 사용
score = [10, 20, 30, 40 , 50]
print("리스트의 크기 : ",len(score))

print(20 in score)   #True
print(100 in score)  #False
print(30 not in score)  #False

#요소 추가
score.append(100)  #맨 뒤에 추가
score.insert(2,70)  #2번 인덱스에 70을 추가

#요소 삭제
score.pop()   #맨 뒤 요소 삭제
score.pop(2)  #2번 인덱스 삭제


#전체 조회
for i in score:
    print(i , end= " ")
print()

#for range() 조회
for i in range(0,len(score)):
    print(score[i], end= " ")