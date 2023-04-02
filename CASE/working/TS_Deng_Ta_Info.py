import shutil
import requests
from lxml import etree
from openpyxl import load_workbook
from openpyxl.styles import Alignment
import win32com
from win32com.client import Dispatch, constants

url = 'https://slh.h3c.com/ProjectTaskManager/MyProjectSubTask'
headers = {
    # 'Cookie': '_ga=GA1.2.973481081.1629872396; _gscu_534429827=29872396d61i8214; ut_user_id=null; ut_global_id=%22b5e648d9-14ad-459a-8555-bad8fa52c913%22; _gsuserid=17cd5427a3b5a5-0cf85044d1873-561a135a-2073600-17cd5427a3c76e; Hm_lvt_df7237ab1ce22c31bbe68ebd1817c1c4=1635665476; ELOQUA=GUID=F2D2E5499FAE437C8F36EF7EF303B8B2; _hjid=afef7b5f-b171-478a-b883-30b0a16c05fd; ASP.NET_SessionId=difemkpmevgqnwgacmp4vfsu; __RequestVerificationToken=KNGjU6UD1NRQz1Q7MXQxU53uGurHvkMqB-or3ApFLznXXJgUD78aqZZt5F2GMaqHqejdBAsacDyPRdoXQDm9aaEA6VhA2-AZw5i-3PWPDB81; SLH_CookiesID_UserIdentify=A238E2A5FCA158C4',
    'Cookie': '_ga=GA1.2.973481081.1629872396; _gscu_534429827=29872396d61i8214; ut_user_id=null; ut_global_id=%22b5e648d9-14ad-459a-8555-bad8fa52c913%22; _gsuserid=17cd5427a3b5a5-0cf85044d1873-561a135a-2073600-17cd5427a3c76e; Hm_lvt_df7237ab1ce22c31bbe68ebd1817c1c4=1635665476; ELOQUA=GUID=F2D2E5499FAE437C8F36EF7EF303B8B2; _hjid=afef7b5f-b171-478a-b883-30b0a16c05fd; SLH_CookiesID_UserIdentify=A942DA1294D6015D; ASP.NET_SessionId=jlqrjz4xpi555pxs4n0d1ozi; __RequestVerificationToken=aRIlynciJPIZ9Z9HZubT4vQUO-4LVt3PnmIxVblwL2ht0XtnuC3mDiMu5fGSq2Xs97-GvaWBm7BzqEBdlEl5exNgbZduEYGcvNzOpfSM6MQ1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53',
    'X-Requested-With': 'XMLHttpRequest'
}
data = {
    'SubTask_State': 'IssuedPending',
    'SubTask_State': 'ApprovalPending',
    'SubTask_State': 'Deliverying',
    'SubTask_State': 'DeliveryFinish',
    'SubTask_State': 'Closed',
    'rows': 300,
    'X-Requested-With': 'XMLHttpRequest',
}

response = requests.post(url, headers=headers, params=data)
if response.status_code == 200:
    # print(response.text)
    xml = etree.HTML(response.text)
    l11 = xml.xpath('//*/td/div[1]/div[2]/a/@href')  # 子任务详情连接
    l12 = xml.xpath('//*/tbody/tr/td[3]/a/text()')  # BOM
    l13 = xml.xpath('//*/td/div[6]/div[2]/text()')  # 合同号
    l14 = xml.xpath('//*/td/div[7]/div[2]/text()')     # 关单日期
    Num = 0
    for x, y, z, w in zip(l11, l12, l13, l14):
        Num += 1
        sub_link = 'https://slh.h3c.com/' + x
        sub_task_link = 'https://slh.h3c.com/ProjectTaskManager/_WorkHourList?lookWorkHour_SubTaskIdStr=' + x[-16:]
        sub_bom = y
        sub_hetong = z.strip().replace(' ', '').split('\n')[-1].replace('合同号：', '')
        # close_date0 = w.strip().replace(' ', '').split('：')[0:]
        # print(close_date0)
        # print('---' * 10)
        close_date = w.strip().replace(' ', '').replace('\r\n', '').split('：')[-2].split('  ')[0]
        # print(close_date)
        try:
            response = requests.get(sub_task_link, headers=headers)
            if response.status_code == 200:
                xml = etree.HTML(response.text)
                work_time = xml.xpath('//*[@id="datatable"]/tbody/tr/td[3]/text()')
                start_work_time = work_time[-1]
                end_work_time = work_time[0]
        except:
            start_work_time = end_work_time = ''
        else:
            pass
        response = requests.get(sub_link, headers=headers, params=data)
        if response.status_code == 200:
            xml = etree.HTML(response.text)
            l0 = xml.xpath('//*[@id="SubTaskOne"]/div/div[3]/div[1]/text()')[0].strip()  # 子任务编码
            l1 = xml.xpath('//*[@id="SubTaskOne"]/div/div[1]/div/text()')[0].strip()  # 项目名称
            l2 = xml.xpath('//*[@id="SubTaskOne"]/div/div[4]/div/text()')[0].strip()  # 服务计划
            l3 = xml.xpath('//*[@id="SubTaskOne"]/div/div[5]/div[2]/text()')[0].strip() + 'H'  # 下发工时
            l4 = xml.xpath('//*[@id="SubTaskOne"]/div/div[6]/div[1]/text()')[0].strip() + 'H'  # 交付工时
            l5 = xml.xpath('//*[@id="SubTaskOne"]/div/div[11]/div[1]/text()')[0].strip()  # 客户联系人
            l6 = xml.xpath('//*[@id="SubTaskOne"]/div/div[11]/div[2]/text()')[0].strip()  # 客户联系电话
            l7 = xml.xpath('//*[@id="SubTaskOne"]/div/div[16]/div[2]/text()')[0].strip()  # 创建日期
            l8 = xml.xpath('//*[@id="SubTaskTwo"]/div/div[1]/div[1]/text()')[0].strip()  # 客户单位名称
            info_list_data = [Num, start_work_time, end_work_time, l0, sub_bom, sub_hetong, l1, l2, l3, l4, l5, l6, l7,
                              l8, close_date]
            # print(info_list_data)
            print(Num, l8, l3, start_work_time, end_work_time, close_date)
            # source = 'C:\\Y\\Case\\working\\TS_Tmp.xlsx'
            # target = 'C:\\Y\\Case\\working\\数据\\' + l0 + '_2.xlsx'
            #
            # sheet_name = source
            # sub_sheet = '签字页'
            #
            # app = win32com.client.Dispatch('Excel.Application')
            #
            # # 后台运行，不显示，不警告
            # app.Visible = 0
            # app.DisplayAlerts = 0
            #
            # # 创建新的Excel
            # # WorkBook = app.Workbooks.Add()
            # # 新建sheet
            # # sheet = WorkBook.Worksheets.Add()
            #
            # # 打开已存在表格，注意这里要用绝对路径
            # WorkBook = app.Workbooks.Open(sheet_name)
            # sheet = WorkBook.Worksheets(sub_sheet)
            #
            # # cell01_value = sheet.Cells(7, 4).Value        # 获取单元格信息 第n行n列，不用-1
            # # print("D7的内容为：", cell01_value)
            #
            # sheet.Cells(7, 4).Value = l8
            # sheet.Cells(11, 4).Value = l5
            # sheet.Cells(11, 9).Value = l6
            # sheet.Cells(14, 4).Value = l1
            # sheet.Cells(15, 4).Value = sub_hetong
            # sheet.Cells(16, 4).Value = start_work_time
            # sheet.Cells(16, 9).Value = end_work_time
            # sheet.Cells(21, 2).Value = sub_bom
            # sheet.Cells(21, 3).Value = l2.replace('\r\n', '')
            # sheet.Cells(21, 8).Value = l3
            # sheet.Cells(21, 9).Value = l0
            #
            # # WorkBook.Save()     # 保存表格
            #
            # WorkBook.SaveAs(target)  # 另存为实现拷贝
            #
            # WorkBook.Close()  # 关闭表格
            # app.Quit()
            #
            # # print(info_list_data)
            # print(target)
        # break
