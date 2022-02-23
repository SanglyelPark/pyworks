import requests

urls = ["https://www.naver.com/", "https://www.python.org/"]
filename = "robots.txt"

# print(urls[0] + filename)

for url in urls:
    url_path = url + filename
    print(url_path)
    resp = requests.get(url_path)
    print(resp)