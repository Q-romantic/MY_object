# -*- coding: utf-8 -*-
import requests
import time
import hashlib
import base64

"""  """
""" 提示： """
for i in range(1, 11):
    # url = 'https://app5.scrape.center/api/movie'  # s = f"/api/movie,{t}"
    # url = 'https://app6.scrape.center/api/movie'  # s = f"/api/movie,{t}"
    # url = 'https://app7.scrape.center/api/movie'  # s = f"/api/movie,{t}"
    url = 'https://app8.scrape.center/api/movie'    # ？？？
    # url = 'https://app9.scrape.center/api/movie'  # s = f"/api/movie,{(i - 1) * 10},{t}"
    t = int(time.time())
    s = f"/api/movie,{t}"  # app8?
    # s = f"/api/movie,{t}"  # app5、6、7
    # s = f"/api/movie,{(i - 1) * 10},{t}"  # app9
    sha1 = hashlib.sha1(s.encode('utf-8'))
    result = sha1.hexdigest()
    s = result + f",{t}"
    token = base64.b64encode(s.encode()).decode()
    params = {
        'limit': 10,
        'offset': (i - 1) * 10,
        'token': token,
    }
    resp = requests.get(url, params=params)
    print(resp.status_code, resp.url)
    print(resp.text)
    break
