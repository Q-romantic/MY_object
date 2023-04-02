# -*- coding: utf-8 -*-
"""
@Time    : 2022/7/20  020 下午 17:54
@Author  : Jan
@File    : AST_to_JS.py
"""
import os
import re

import execjs
import js2py

name = "9.0.7"
# name = "slide.7.8.6"
encode_file = f"C:\\Users\\11390\\Desktop\\{name}.js"
with open(encode_file, mode='r', encoding='utf-8') as f:
    jscode = f.read()
# print(jscode)
fn_1 = re.findall("return typeof (.*?)==='function'\?", jscode)[0].split('.')[1]
fn_2 = re.findall("return typeof (.*?)==='function'\?", jscode)[1].split('.')[1]
fn_3 = re.findall("\d\)\};break;\}\}\}\(\);(.*?)=function\(\)\{return", jscode)[0].split('.')[1]
fn_4 = re.findall(";\};(.*?)=function\(\)\{return", jscode)[0].split('.')[1]
fn_0 = re.findall(";function (.*?)\(\)\{\}!", jscode)[0]

with open('AST.js', mode='r', encoding='utf-8') as f:
    jscode = f.read()
jscode = jscode.replace("Bq_", fn_1).replace("CyZ", fn_2).replace("Dvn", fn_3).replace("EeS", fn_4).replace("AaWgt", fn_0).replace("slide.7.8.4", name)
# print(jscode)
with open('jscode.js', mode='w', encoding='utf-8') as f:
    f.write(jscode)
os.system('node jscode.js')
# os.remove('jscode.js')


