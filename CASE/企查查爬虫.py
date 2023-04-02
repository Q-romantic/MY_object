# Time: 2021/4/12 16:04
# Author: 阿尔法
# File: 企查查-钉钉爬虫.py
# @Software: PyCharm
from requests_html import HTMLSession
from fake_useragent import UserAgent
import os, xlwt, xlrd
from xlutils.copy import copy
ua = UserAgent()
session = HTMLSession()


class QccSpider(object):

    def __init__(self):
        self.start_url = 'https://www.qcc.com/map_searchByLocation'
        """构造请求头"""
        self.headers = {
            'content-length': '557',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': 'qcc_did=73a8e934-99cb-4a75-86ff-7a7b2047901f; UM_distinctid=17f7717b2616c-0e1c5184e6ebbd-56171d5e-1fa400-17f7717b262cf4; QCCSESSID=b450e3e4e2c87b4baef4825c4c; _uab_collina=165774146920328687320586; acw_tc=7ca3c31816577785980516016e3944de4e55fb1b368e8520a8f88d5319; CNZZDATA1254842228=101815594-1646969003-https%253A%252F%252Fcn.bing.com%252F%7C1657778723',
            'origin': 'https://www.qcc.com',
            'referer': 'https://www.qcc.com/map',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
        """构造请求体"""
        self.data = {
            'searchType': 'multiple',
            'longitude': '110.486075',
            'latitude': '29.127399',
            'searchKey': '',
            'pageSize': '10',
            'pageIndex': '{}',
            'distance': '8.123',
            'startDateBegin': '',
            'startDateEnd': '',
            'registCapiBegin': '',
            'registCapiEnd': '',
            'industryCode': '',
            'subIndustryCode': '0',
            'currencyCode': '',
            'statusCode': '',
            'isSortAsc': '',
            'sortField': '',
            'orgType': '',
            'coyType': '',
            'flagT': '',
            'flagMN': '',
            'flagE': '',
            'flagGW': '',
            'flagRECCAP': '',
            'flagISBR': '',
            'flagWEB_ISICP': '',
            'flagM': '',
            'flagP': '',
            'flagF': '',
            'flagK': '',
            'flagS': '',
            'flagC': '',
            'flagSC': '',
            'flagGX': '',
            'flagTE': '',
            'flagCI': '',
            'flagMP': '',
            'flagLQ': '',
            'flagTA': '',
            'flagGT': '',
            'flagAPP': '',
            'flagWP': '',
            'flagZhuanli': '',
            'flagBM': '',
            'flagCR': '',
            'flagZzzs': '',
            'flagTEC': '',
            'flagQauth': '',
            'flagEnp': '',
            'flagAop': '',
            'flagKey': '',
            'insuredCnt': ''
        }

    def parse_zjj_map(self):
        """
        解析张家界地区企业
        :return:
        """
        """完善请求体的拼接"""
        self.data['pageIndex'].format('1')
        """发送请求"""
        response = session.post(self.start_url, headers=self.headers, data=self.data)
        print(response.text)
        """获取企业数量"""
        listCount = response.json()['listCount']
        """回调"""
        print(listCount)
        self.parse_listCount_url_response(listCount)

    def parse_listCount_url_response(self, listCount):
        """
        根据企业数量，构造新的请求体，开始解析地区企业数据
        :param listCount: 数量
        :return:
        """
        """取整，获取翻页范围"""
        page = int(listCount) // 10
        for i in range(1, page+1):
            """进入回调机制"""
            self.parse_callback_mode(i)

    def parse_callback_mode(self, page):
        """
        请求回调机制，防止数据遗失
        :param page: 页码
        :return:
        """
        """完善请求体的拼接"""
        self.data['pageIndex'].format(page)
        """发送请求"""
        response = session.post(self.start_url, headers=self.headers, data=self.data)
        if response.status_code == 200:
            json_data = response.json()
            """取出企业数据大列表"""
            hit_list = json_data['list']
            """进入解析该列表"""
            self.parse_hit_list_func(hit_list)
        else:
            self.parse_callback_mode(page)

    def parse_hit_list_func(self, hit_list):
        """
        开始解析保存
        :param hit_list: 企业数据大列表
        :return:
        """
        for hit in hit_list:
            # print(hit)
            """数据提取"""
            # 公司key
            KeyNo = hit['KeyNo']
            # 公司名称
            Name = hit['Name']
            # 法人代表
            OperName = hit['OperName']
            # 公司状态
            Status = hit['Status']
            # 公司类型
            EconKind = hit['EconKind']
            # 注册地址
            Address = hit['Address']
            # 营业范围
            Industry = hit['Industry']['Industry']
            dict_data = {
                '基本详情': [KeyNo, Name, OperName, Status, EconKind, Address, Industry]
            }
            print(dict_data)
            # self.save_excel(dict_data)
            # print('保存完成========！！！')

    def save_excel(self, data):
        # data = {
        #     '基本详情': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        # }
        os_path_1 = os.getcwd() + '/数据/'
        if not os.path.exists(os_path_1):
            os.mkdir(os_path_1)
        # os_path = os_path_1 + self.os_path_name + '.xls'
        os_path = os_path_1 + '企查查数据.xls'
        if not os.path.exists(os_path):
            # 创建新的workbook（其实就是创建新的excel）
            workbook = xlwt.Workbook(encoding='utf-8')
            # 创建新的sheet表
            worksheet1 = workbook.add_sheet("基本详情", cell_overwrite_ok=True)
            borders = xlwt.Borders()  # Create Borders
            """定义边框实线"""
            borders.left = xlwt.Borders.THIN
            borders.right = xlwt.Borders.THIN
            borders.top = xlwt.Borders.THIN
            borders.bottom = xlwt.Borders.THIN
            borders.left_colour = 0x40
            borders.right_colour = 0x40
            borders.top_colour = 0x40
            borders.bottom_colour = 0x40
            style = xlwt.XFStyle()  # Create Style
            style.borders = borders  # Add Borders to Style
            """居中写入设置"""
            al = xlwt.Alignment()
            al.horz = 0x02  # 水平居中
            al.vert = 0x01  # 垂直居中
            style.alignment = al
            # 合并 第0行到第0列 的 第0列到第13列
            '''基本详情13'''
            # worksheet1.write_merge(0, 0, 0, 13, '基本详情', style)
            excel_data_1 = ('公司key', '公司名称', '法人代表', '公司状态', '公司类型', '注册地址', '营业范围'
                            )
            for i in range(0, len(excel_data_1)):
                worksheet1.col(i).width = 2560 * 3
                #               行，列，  内容，            样式
                worksheet1.write(0, i, excel_data_1[i], style)
            workbook.save(os_path)
        # 判断工作表是否存在
        if os.path.exists(os_path):
            # 打开工作薄
            workbook = xlrd.open_workbook(os_path)
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
                        new_workbook.save(os_path)


if __name__ == '__main__':
    q = QccSpider()
    q.parse_zjj_map()










