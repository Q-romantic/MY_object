# -*- coding: utf-8 -*-
"""
@Time    : 2022/11/7  007 下午 17:05
@Author  : Jan
@File    : 合并.py
"""

""" {} """

import pandas as pd
import os


def workbook_merge_1(pwd, name):
    new_path = f"{pwd}\\{name}.xlsx"
    if os.path.exists(new_path):
        os.remove(new_path)
    df_list = []
    for path, dirs, files in os.walk(pwd):
        for file in files:
            file_path = os.path.join(path, file)
            df = pd.read_excel(file_path)
            df_list.append(df)
    result = pd.concat(df_list)
    # print(result)
    result.to_excel(new_path, index=False)


pwd = "C:\\Y\\Case\\接任务练习\\code"
name = "tmp"
workbook_merge_1(pwd, name)
