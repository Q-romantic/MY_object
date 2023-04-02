# -*- coding: utf-8 -*-
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44'}
url = 'https://book.sunwing.ca/cgi-bin/resultspackage-plus.cgi'
params = {
    "page": "1",
    "section": "exact",
    "language": "en",
    "sid": "e655c3926ff070a4a15596864631f107",
    "search_id": "",
    "code_ag": "rds",
    "alias": "btd",
    "query_timestamp": "",
    "flex": "N",
    "action": "results"
}

response =requests.get(url, headers=headers, params=params)
data =response.text
print(data)
