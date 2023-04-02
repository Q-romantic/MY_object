# -*- coding: utf-8 -*-
"""
@Time    : 2023/2/14  014 下午 19:47
@Author  : Jan
@File    : url_to_doc.py
"""

""" { url 转 doc} """

import requests
import pypandoc

"""
　　pypandoc.convert_file(source_file, to, format=None, extra_args=(), encoding='utf-8',
                 outputfile=None, filters=None, verify_format=True)
    参数说明：
    source_file:源文件路径
    to：输入应转换为的格式；可以是'pypandoc.get_pandoc_formats（）[1]`之一
    format：输入的格式；将从具有已知文件扩展名的源_文件推断；可以是“pypandoc.get_pandoc_formats（）[1]”之一（默认值= None)
    extra_args：要传递给pandoc的额外参数（字符串列表）(Default value = ())
    encoding：文件或输入字节的编码 (Default value = 'utf-8')
    outputfile：转换后的内容输出路径+文件名，文件名的后缀要和to的一致，如果没有，则返回转换后的内容（默认值= None)
    filters – pandoc过滤器，例如过滤器=['pandoc-citeproc']
    verify_format：是否对给定的格式参数进行验证，（pypandoc根据文件名截取后缀格式，与用户输入的format进行比对）

    pypandoc.convert_text(source, to, format, extra_args=(), encoding='utf-8',
                     outputfile=None, filters=None, verify_format=True):
    参数说明：
    source：字符串       
    其余和canvert_file()相同      

"""

url = 'https://mp.weixin.qq.com/s?__biz=MzAwMjExNDU1Mw==&mid=2650602348&idx=1&sn=ae6aa0af240dd63e86a03d425c11e163&chksm=82c70dfab5b084ec8fbdfc913a72abbe2ad836b28ee5b44e68cf853887d989980ec51555bbc3&scene=21'
response = requests.get(url)
data = response.text

# 将当前目录下html目录中的1.html网页文件直接转换成.docx文件，文件名为file1.docx，并保存在当前目录下的doc文件夹中
# pypandoc.convert_file('login.html', 'docx', outputfile="file1.docx")

# 将当前目录下html目录中的1.html网页文件 读取出来，然后转换成.docx文件，文件名为file2.docx，并保存在当前目录下的doc文件夹中
# with open('login.html', encoding='utf-8') as f:
#     data = f.read()
pypandoc.convert_text(data, to='docx', format='html', encoding='utf-8', outputfile="file2.docx")
