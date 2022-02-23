from bs4 import BeautifulSoup

# find() 함수 사용

html_str = """
<html>
<body>
    <ul class='item'>
        <li>인공지능</li>
        <li>Big Data</li>
        <li>로봇</li>
    </ul>
    <ul class='lang'>
        <li>파이션</li>
        <li>자바</li>
        <li>자바스크립트</li>
    </ul>
</body>
</html>
"""
soup = BeautifulSoup(html_str, "html.parser")
# print(soup)
# 선택자로 찾기 - 딕셔너리 형태
ul = soup.find('ul', attrs={'class':'item'})   #처음 나오는 ul 태그 및 하위태그 검색
print(ul)
