import requests
from bs4 import BeautifulSoup

url = 'https://www.umeitu.com/bizhitupian/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36'
}

# resp = requests.get(url).content.decode()
resp = requests.get(url, headers=headers)
resp.encoding = 'utf-8'

# page = BeautifulSoup(resp.text, "html.parser")
page = BeautifulSoup(resp.text, features="lxml")

ul = page.find_all("ul", class_="pic-list after")
for i in ul:
    li = i.find_all("a")
    for j in li:
        # print(j)
        name = j.text.strip(' ')
        data_src = j.find("img").get("data-src").replace('small', '')
        print(name, data_src)
