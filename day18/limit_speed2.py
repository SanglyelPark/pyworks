#if ~ else문

#변수 생성 및 저장
limit_speed = 45


#if문
if limit_speed >= 50 : # 콜론은 블럭 역할
    print("안전속도 위반! 과태료 부과 대상") #4칸 스페이스(들여쓰기)
else:
    print("안전속도 준수!")

#출력
print("시속 : " + str(limit_speed) + "km입니다.")
