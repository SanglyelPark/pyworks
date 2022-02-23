import requests
# requests - python 프로그래밍 언어용 http 라이브러리
# 200 - 페이지 요청 성공
# 404 - 페이지가 없음
url = "https://www.python.org/"
response = requests.get(url)
print(response)
print(response.status_code)

html = response.text    # html 코드 저장
print(html)
