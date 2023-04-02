import os
import msvcrt
import requests
from lxml import etree
import win32com
from win32com.client import Dispatch

# pyinstaller -F -i 1.ico 有道_v2.py      # 打包.exe文件

def get_ts_date():
    url = 'https://slh.h3c.com/ProjectTaskManager/MyProjectSubTask'
    headers = {
        'Cookie': 'SLH_CookiesID_UserIdentify={}'.format(input('请输入您的16位ID\nSLH_CookiesID_UserIdentify: ')),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53',
        'X-Requested-With': 'XMLHttpRequest'
    }
    data = {
        'SubTask_State': 'IssuedPending',
        'SubTask_State': 'ApprovalPending',
        'SubTask_State': 'Deliverying',
        # 'SubTask_State': 'DeliveryFinish',
        # 'SubTask_State': 'Closed',
        'rows': 300,
        'X-Requested-With': 'XMLHttpRequest',
    }
    response = requests.post(url, headers=headers, params=data)
    # print(response.text)
    if response.status_code == 200:
        print('Waitting...')
        try:
            xml = etree.HTML(response.text)
            l11 = xml.xpath('//*/td/div[1]/div[2]/a/@href')  # 子任务详情链接
            l12 = xml.xpath('//*/tbody/tr/td[3]/a/text()')  # BOM
            l13 = xml.xpath('//*/td/div[6]/div[2]/text()')  # 合同号
            Num = 0
            for x, y, z in zip(l11, l12, l13):
                Num += 1
                sub_link = 'https://slh.h3c.com/' + x
                sub_task_link = 'https://slh.h3c.com/ProjectTaskManager/_WorkHourList?lookWorkHour_SubTaskIdStr=' + x[-16:]
                sub_bom = y
                sub_hetong = z.strip().replace(' ', '').split('\n')[-1].replace('合同号：', '')
                try:
                    response = requests.get(sub_task_link, headers=headers)
                    if response.status_code == 200:
                        xml = etree.HTML(response.text)
                        work_time = xml.xpath('//*[@id="datatable"]/tbody/tr/td[3]/text()')
                        start_work_time = work_time[-1:]
                        end_work_time = work_time[:0]
                except:
                    start_work_time = end_work_time = ''
                    print(5)
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
                                      l8]
                    # print(info_list_data)
                    os_mkdir_path = os.getcwd() + '\\数据\\'
                    if not os.path.exists(os_mkdir_path):
                        os.mkdir(os_mkdir_path)
                    source = os.getcwd() + '\\TS_Tmp.xlsx'
                    target = os_mkdir_path + l0 + '_2.xlsx'

                    sheet_name = source
                    sub_sheet = '签字页'

                    app = win32com.client.Dispatch('Excel.Application')

                    # 后台运行，不显示，不警告
                    app.Visible = 0
                    app.DisplayAlerts = 0

                    # 打开已存在表格，注意这里要用绝对路径
                    WorkBook = app.Workbooks.Open(sheet_name)
                    sheet = WorkBook.Worksheets(sub_sheet)

                    sheet.Cells(7, 4).Value = l8
                    sheet.Cells(11, 4).Value = l5
                    sheet.Cells(11, 9).Value = l6
                    sheet.Cells(14, 4).Value = l1
                    sheet.Cells(15, 4).Value = sub_hetong
                    sheet.Cells(16, 4).Value = start_work_time
                    sheet.Cells(16, 9).Value = end_work_time
                    sheet.Cells(21, 2).Value = sub_bom
                    sheet.Cells(21, 3).Value = l2.replace('\r\n', '')
                    sheet.Cells(21, 8).Value = l3
                    sheet.Cells(21, 9).Value = l0

                    # WorkBook.Save()     # 保存表格

                    WorkBook.SaveAs(target)  # 另存为实现拷贝

                    WorkBook.Close()  # 关闭表格
                    app.Quit()

                    # print(info_list_data)
                    print(target)
                # break
        except:
            print('请重试，可能需要您的网页保持登录状态！输入ID例如：A942DA1294D6015D')
            print('注意：需要将TS_Tmp.xlsx同本程序放同一个目录，模板中非标黄区域可自定义。')
        else:
            pass
        print('Done')


if __name__ == '__main__':
    while True:
        print()
        get_ts_date()
        print()
        print()
        print('请按任意键继续. . .')
        print("Press 'ESC' or 'Ctrl+C' to exit...")
        if ord(msvcrt.getch()) in [3, 27]:
            break
        print()
        print()
        print()