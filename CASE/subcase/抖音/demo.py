# -*- coding: utf-8 -*-
"""
@Time    : 2022/6/23  023 下午 12:30
@Author  : Jan
@File    : demo.py
"""
import httpx
import requests
import pprint

""" {注释请求头"accept-encoding"} """

import requests

url = 'https://www.douyin.com/user/MS4wLjABAAAAWxLpO0Q437qGFpnEKBIIaU5-xOj2yAhH3MNJi-AUY04'

headers = {
    # "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    # "accept-encoding": "gzip, deflate, br",   # 关键点
    # "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ja;q=0.5",
    # "cache-control": "no-cache",
    "cookie": "douyin.com; ttwid=1%7CbNMx_2ONyK_a-TNovp6m1bGoYn5VfIcWgrDABJg5cs8%7C1655948777%7Ccfa1af34501702e22c97a6d150e711fb84173fe22151aae49a6ae8663f6249d9; douyin.com; strategyABtestKey=1655948778.25; s_v_web_id=verify_l4qd5azg_A8Dh7Q4j_Fxli_43Rw_AbZc_i0s6y0Uf0r8V; passport_csrf_token=20e482ee5351c37bdcf06801bcce37a1; passport_csrf_token_default=20e482ee5351c37bdcf06801bcce37a1; _tea_utm_cache_2285=undefined; _tea_utm_cache_1300=undefined; AB_LOGIN_GUIDE_TIMESTAMP=%221655948778064%22; live_can_add_dy_2_desktop=%220%22; odin_tt=4a216c8261e48b9103ecc9a83bc733e0ced9593b70fea2756e3ed1b00d95c5003a39b79fff2d7884b34e5f20b326bedab09fc823d141bbb10c6bec7df8dea96c2b3c3eb7c59d4d405f341a07ff8df1ac; THEME_STAY_TIME=%22299666%22; IS_HIDE_THEME_CHANGE=%221%22; pwa_guide_count=%223%22; msToken=rqM0lRPc7elBscYJsH0LDHuIylZ-UGqFw9wZGOYOlqHUU5cbH16D3FtV9odeDwwpXsU5LPSxsA8OHk2Qp7he9etDRbo2I-Nc2AvZZI5f_oI_WUvRPvfM_sTdRX7N63Na; __ac_nonce=062b3e4640042a3c5b8bd; __ac_signature=_02B4Z6wo00f014RasvgAAIDDBFhIuOpl.3eEfrZAAIOtIe3CM1VPqQCkHgPpJKccOH8tGFEFusTlLaM690EjogKZTbab.CmN0Tq3VrFX3UKDlWvmmKJa2ZWEdcQe13fMNt8IjjS87ZWyWjQj10; tt_scid=1DdHZgSpjSE77Yh1NlS8ZJ424Eze0O8ssyzQWJwXVjo8gD9INyZ0ESLgJXwt6whu4902; home_can_add_dy_2_desktop=%221%22; msToken=XEshVhIr413w5DIYHi33PlArnL0hQWy0UFnmW94FASM0exacsqscyahY5ao8NyTlumM8jAE9wDTmkoX9htUqw0VaDidDtBQWA_RfzmipG11z4EVMS1e_EycdL478kas=",
    # "pragma": "no-cache",
    # "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Microsoft Edge\";v=\"102\"",
    # "sec-ch-ua-mobile": "?0",
    # "sec-ch-ua-platform": "\"Windows\"",
    # "sec-fetch-dest": "document",
    # "sec-fetch-mode": "navigate",
    # "sec-fetch-site": "same-origin",
    # "sec-fetch-user": "?1",
    # "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44"
}

response = requests.get(url, headers=headers).content.decode()
print(response)

# with httpx.Client(headers=headers, http2=True) as client:
#   response = client.get(url, headers=headers)
#   response.encoding = 'utf-8'
#   print(response.text)
