import os, xlwt, xlrd
from xlutils.copy import copy

"""
pip install xlwt
优点：该模板是采集一次保存一次，不会受爬虫程序意外终止没有存储到数据
     在原有的工作簿上支持建新表存储数据(看data参数格式的定义)
缺点：代码较多
弊端：数据采集保存过程中，表格不能处于打开状态

数据保存的过程
    1.创建工作簿
    2.根据传递进来的data字典进行保存
    3.data字典的key值是对应保存工作表的名称
    4.插入一次数据保存一次
"""


# # 一个工作簿创建一张表模板代码
def SaveExcel(data):
    """
    使用前，请先阅读代码
    :param data: 需要保存的data字典(有格式要求)
    :return:
    格式要求:
        data = {
        '基本详情': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    }
    注意：这个模板程序会将data的key值作为excel的表名来判断，一样才会保存
    """
    # 创建保存excel表格的文件夹
    # os.getcwd() 获取当前文件路径
    os_mkdir_path = os.getcwd() + '/电商数据/'
    # 判断这个路径是否存在，不存在就创建
    if not os.path.exists(os_mkdir_path):
        os.mkdir(os_mkdir_path)
    # 判断excel表格是否存在           工作簿文件名称
    os_excel_path = os_mkdir_path + '数据.xls'
    if not os.path.exists(os_excel_path):
        # 不存在，创建工作簿(也就是创建excel表格)
        workbook = xlwt.Workbook(encoding='utf-8')
        """工作簿中创建新的sheet表"""      # 设置表名
        worksheet1 = workbook.add_sheet("电商商品数据", cell_overwrite_ok=True)
        """设置sheet表的表头"""
        sheet1_headers = ('评论内容', '评论时间', '点赞数', '用户名')
        # 将表头写入工作簿
        for header_num in range(0, len(sheet1_headers)):
            # 设置表格长度
            worksheet1.col(header_num).width = 2560 * 3
            # 写入            行, 列,           内容
            worksheet1.write(0, header_num, sheet1_headers[header_num])
        # 循环结束，代表表头写入完成，保存工作簿
        workbook.save(os_excel_path)
    # 判断工作簿是否存在
    if os.path.exists(os_excel_path):
        # 打开工作簿
        workbook = xlrd.open_workbook(os_excel_path)
        # 获取工作薄中所有表的个数
        sheets = workbook.sheet_names()
        for i in range(len(sheets)):
            for name in data.keys():
                worksheet = workbook.sheet_by_name(sheets[i])
                # 获取工作薄中所有表中的表名与数据名对比
                if worksheet.name == name:
                    # 获取表中已存在的行数
                    rows_old = worksheet.nrows
                    # 将xlrd对象拷贝转化为xlwt对象
                    new_workbook = copy(workbook)
                    # 获取转化后的工作薄中的第i张表
                    new_worksheet = new_workbook.get_sheet(i)
                    for num in range(0, len(data[name])):
                        new_worksheet.write(rows_old, num, data[name][num])
                    new_workbook.save(os_excel_path)
#
#
# if __name__ == '__main__':
#     """保存示例
#     注意字典的格式
#     """
#     data = {
#             '电商商品数据1': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#         }
#     SaveExcel(data)


# """一个工作簿创建多张表"""
def SaveExcels(data):
    """
    使用前，请先阅读代码
    :param data: 需要保存的data字典(有格式要求)
    :return:
    格式要求:
        data = {
        '基本详情': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    }
    注意：这个模板程序会将data的key值作为excel的表名来判断，一样才会保存
    """
    # 获取表的名称
    sheet_name = [i for i in data.keys()][0]
    # 创建保存excel表格的文件夹
    # os.getcwd() 获取当前文件路径
    os_mkdir_path = os.getcwd() + '/数据/'
    # 判断这个路径是否存在，不存在就创建
    if not os.path.exists(os_mkdir_path):
        os.mkdir(os_mkdir_path)
    # 判断excel表格是否存在           工作簿文件名称
    os_excel_path = os_mkdir_path + '数据.xls'
    if not os.path.exists(os_excel_path):
        # 不存在，创建工作簿(也就是创建excel表格)
        workbook = xlwt.Workbook(encoding='utf-8')
        """工作簿中创建新的sheet表"""      # 设置表名
        worksheet1 = workbook.add_sheet(sheet_name, cell_overwrite_ok=True)
        """设置sheet表的表头"""
        sheet1_headers = ('评论内容', '评论时间', '点赞数', '用户名')
        # 将表头写入工作簿
        for header_num in range(0, len(sheet1_headers)):
            # 设置表格长度
            worksheet1.col(header_num).width = 2560 * 3
            # 写入表头        行,    列,           内容
            worksheet1.write(0, header_num, sheet1_headers[header_num])
        # 循环结束，代表表头写入完成，保存工作簿
        workbook.save(os_excel_path)
    """=============================已有工作簿添加新表==============================================="""
    # 打开工作薄
    workbook = xlrd.open_workbook(os_excel_path)
    # 获取工作薄中所有表的名称
    sheets_list = workbook.sheet_names()
    # 如果表名称：字典的key值不在工作簿的表名列表中
    if sheet_name not in sheets_list:
        # 复制先有工作簿对象
        work = copy(workbook)
        # 通过复制过来的工作簿对象，创建新表  -- 保留原有表结构
        sh = work.add_sheet(sheet_name)
        # 给新表设置表头
        excel_headers_tuple = ('日期', '姓名', '年龄', '性别', '电话号码')
        for head_num in range(0, len(excel_headers_tuple)):
            sh.col(head_num).width = 2560 * 3
            #               行，列，  内容，            样式
            sh.write(0, head_num, excel_headers_tuple[head_num])
        work.save(os_excel_path)
    """========================================================================================="""
    # 判断工作簿是否存在
    if os.path.exists(os_excel_path):
        # 打开工作簿
        workbook = xlrd.open_workbook(os_excel_path)
        # 获取工作薄中所有表的个数
        sheets = workbook.sheet_names()
        for i in range(len(sheets)):
            for name in data.keys():
                worksheet = workbook.sheet_by_name(sheets[i])
                # 获取工作薄中所有表中的表名与数据名对比
                if worksheet.name == name:
                    # 获取表中已存在的行数
                    rows_old = worksheet.nrows
                    # 将xlrd对象拷贝转化为xlwt对象
                    new_workbook = copy(workbook)
                    # 获取转化后的工作薄中的第i张表
                    new_worksheet = new_workbook.get_sheet(i)
                    for num in range(0, len(data[name])):
                        new_worksheet.write(rows_old, num, data[name][num])
                    new_workbook.save(os_excel_path)


if __name__ == '__main__':
    """
    测试：
    注意观察data字典的格式
    """
    data1 = {
        '数据3': [1, 2, 3, 4, 5]
    }
    data2 = {
        '数据4': ['a', 'b', 'c', 'd', 'e']
    }
    data3 = {
        '数据5': ['1', '2', '3', 'd', 'e']
    }
    SaveExcels(data1)
    SaveExcels(data2)
    SaveExcels(data3)





import requests






