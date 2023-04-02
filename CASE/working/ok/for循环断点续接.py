# -*- coding: utf-8 -*-
"""
@Time    : 2023/1/4  004 下午 19:08
@Author  : Jan
@File    : for循环断点续接.py
"""
import json
import os
import time
import linecache

""" {循环列表中断后再次接着执行，当列表内容循环结束后再次运行会自动删除log记录文件} """

li = ["国内热点地区", "北京", "天津", "上海", "重庆", "安徽"]
filename = 'start_num_log.txt'
start_num = 0
if os.path.exists(filename):
    try:
        start_num = int(linecache.getline(filename, 1))  # 获取第一行内容
        content = linecache.getline(filename, 2)  # 获取第二行内容
        print("历史运行记录：", content)
    except:
        pass

if start_num != len(li):
    for i in li[start_num:]:
        pass
        time.sleep(1)
        print(i)
        pass
        start_num += 1
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(str(start_num))
            f.write('\n')
            # f.write(json.dumps(str(li[:start_num]), ensure_ascii=False))
            f.write(str(li[:start_num]))

else:
    os.remove(filename)
