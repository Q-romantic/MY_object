# -*- coding: utf-8 -*-
"""
@Time    : 2022/11/5  005 上午 11:39
@Author  : Jan
@File    : 20221105_东北亚传统药物的药材和化合物数据库.py
"""
import parsel
import requests
from working.all_tools.tools import getua

""" {} """

headers = {
    "User-Agent": getua(),

}


def get_smiles(id: str):
    data = {
        "flag": "cc",
        "id": id,
    }
    url = 'https://informatics.kiom.re.kr/compound/detail.do'
    response = requests.post(url, headers=headers, data=data)
    sel = parsel.Selector(response.text)
    SMILES = sel.xpath('//*[@id="tab1"]/tbody/tr[5]/td/text()').get()
    print(id, "--->", SMILES)

def get_Compound_name(id: str):
    data = {
        "tabid": "",
        "flag": "mm",
        "id": id,
        "currentPage": "10"
    }
    url = 'https://informatics.kiom.re.kr/compound/detail.do'
    response = requests.post(url, headers=headers, data=data)
    sel = parsel.Selector(response.text)
    SMILES_ids = sel.xpath('//*[@id="tab2"]/tbody/tr/td[2]/text()').getall()
    # print(id, SMILES_ids)
    for SMILES_id in SMILES_ids:
        get_smiles(SMILES_id)
        break

def get_Latin_name():
    data = {
        "tabid": "0",
        "flag": "",
        "id": "",
        "currentPage": "1"
    }
    url = 'https://informatics.kiom.re.kr/compound/browse.do'
    response = requests.post(url, headers=headers, params=data)
    sel = parsel.Selector(response.text)
    Latin_names = sel.xpath('//*[@id="tab1"]/tbody/tr/td[2]/text()').getall()
    print(Latin_names)
    # for Latin_name in Latin_names:
    #     get_Compound_name(Latin_name)

# get_smiles("1,6-O,O-diacetylbritannilactone")
# get_Compound_name("Abri Herba")
get_Latin_name()