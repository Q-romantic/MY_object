# -*- coding: utf-8 -*-
import requests

""" 对接 JWT 模拟登录方式，适合用作 JWT 模拟登录练习。 """
""" 提示： """

url = 'https://login3.scrape.center/api/login'

session = requests.session()
data = {
    'username': 'admin',
    'password': 'admin',
}
resp = session.post(url, data=data)
token = resp.json()['token']
# print(token)


for page in range(1, 11):
    url = 'https://login3.scrape.center/api/book'
    # headers = {'Authorization': 'jwt 加密token'}
    headers = {'Authorization': f'jwt {token}'}
    params = {'limit': 18, 'offset': (page - 1) * 18}
    resp = requests.get(url, headers=headers, params=params)
    # print(resp.status_code, url)
    # print(resp.text)
    data = resp.json()['results']
    for i in data:
        name = i['name']
        sub_url = 'https://spa5.scrape.center/detail/' + str(i['id'])
        authors = str(i['authors']).replace('\\n', '').replace(' ', '')
        img_url = i['cover']
        score = i['score']
        print(name, sub_url, authors, img_url, score)
    break
