# 용어 사전 만들기

dic = {
    "이진수" : "2진법으로 나타낸 숫자로 0과 1로 구성됨",
    "버그" : "프로그램이 적절하게 동작하는데 실패하거나 또는 전혀 동작하지 않는 \n"
                "원인을 제공하는 코드 조각",
    "함수" : "특정한 기능을 수행하는 명령어 코드의 집합",
    "HTML" : "웹 페이지를 만드는 AKZMDJQ(Markup) 언어이다."
}

print(dic['이진수'])
print(dic['버그'])

print("♣ 용어 사전 ♣")
word = input("정의 되어 있는 단어 입력 : ")
try:
    definition = dic[word]
    print(definition)
except KeyError:
    print("찾는 단어가 없습니다.")
