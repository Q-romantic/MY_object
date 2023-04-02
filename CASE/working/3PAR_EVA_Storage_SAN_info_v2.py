# -*- encoding: utf-8 -*-
"""
亦庄邮政集团设备，个人笔记本接入管理网络：
网线位置：D3A3_1404
可用地址：172.16.136.98
可用地址：172.16.136.100
网关地址：172.16.136.1
"""

import sys
import os
import re
import xlwt
import xlrd
from xlutils.copy import copy
from collections import Counter
from lxml import etree
from datetime import datetime

# src_dir = r'C:\360安全浏览器下载\Tmp'  # 源文件目录地址
# src_dir = r'C:\Users\11390\Desktop\info\logs'  # 源文件目录地址


# src_dir = r'C:\Users\11390\Desktop\info\test'  # 源文件目录地址
# src_dir = r'C:\Users\11390\Desktop\EMS-info\logs'  # 源文件目录地址


src_dir = sys.argv[1]  # 源文件目录地址
filename = '数据'
try:
    filename = sys.argv[2].split('.')[0]  # 指定生成文件名称
except:
    pass

def list_all_files(rootdir):
    files = []

    # 列出文件夹下所有的目录与文件
    list_file = os.listdir(rootdir)
    for i in range(0, len(list_file)):
        # 构造路径
        path = os.path.join(rootdir, list_file[i])
        # 判断路径是否是一个文件目录或者文件
        # 如果是文件目录，继续递归
        if os.path.isdir(path):
            files.extend(list_all_files(path))
        if os.path.isfile(path):
            files.append(path)
    return files


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
    os_excel_path = os_mkdir_path + filename + '.xls'
    if not os.path.exists(os_excel_path):
        # 不存在，创建工作簿(也就是创建excel表格)
        workbook = xlwt.Workbook(encoding='utf-8')
        """工作簿中创建新的sheet表"""  # 设置表名
        worksheet1 = workbook.add_sheet(sheet_name, cell_overwrite_ok=True)
        """设置sheet表的表头"""
        sheet1_headers = ('序列号', '产品型号', 'IP地址', '裸容量', '剩余容量', '固件版本及补丁', 'cage数量', '硬盘数量', 'vv数量', '单盘容量及数量分布')
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
        # # 给新表设置表头
        # excel_headers_tuple = ('序列号',)
        global excel_headers_tuple
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


class EVA_Storage_info(object):

    def SerialNumber(self, filename):
        # 获取设备序列号
        SN = filename[-14:-4]
        return SN

    def savetosheet1(self, r):
        xml = etree.HTML(r)  # 转为xml文档
        # 获取设备型号
        SystemModel = xml.xpath('//systemtype/text()')[0]
        # 获取设备IP地址
        managementhostip = xml.xpath('//managementhostip/text()')[0]
        # 获取裸容量
        totalstoragespace = xml.xpath('//totalstoragespace/text()')[0]
        if float(totalstoragespace) >= 1024:
            totalstoragespace = str(round(float(totalstoragespace) / 1024, 2)) + ' TB'
        else:
            totalstoragespace = xml.xpath('//totalstoragespace/text()')[0] + ' GB'
        # # 获取使用容量
        # usedstoragespace = xml.xpath('//usedstoragespace/text()')[0] + ' GB'
        # 获取剩余容量
        availablestoragespace = xml.xpath('//availablestoragespace/text()')[0]
        if float(availablestoragespace) >= 1024:
            availablestoragespace = str(round(float(availablestoragespace) / 1024, 2)) + ' TB'
        else:
            availablestoragespace = xml.xpath('//availablestoragespace/text()')[0] + ' GB'
        # 获取固件版本
        firmwareversion = xml.xpath('//firmwareversion/text()')[0]
        # cage数量
        EnclosureNumber = len(xml.xpath('//diskshelfname/text()'))
        # 硬盘数量
        DiskNumberlist = xml.xpath('//totaldisks/text()')
        DiskNumber = 0
        for i in DiskNumberlist:
            DiskNumber += int(i)
        # 获取VV数量
        VvNumber = len(xml.xpath('//wwlunid/text()'))
        # # 硬盘容量大小
        # DiskSize = xml.xpath('//formattedcapacity/text()')
        # print(set(DiskSize))

        data1 = {
            # ['序列号', '产品型号', 'IP地址', '裸容量', '剩余容量', '固件版本及补丁', 'cage数量', '硬盘数量', 'vv数量', '单盘容量及数量分布']
            '1、存储信息': [self.SerialNumber(fi), SystemModel, managementhostip, totalstoragespace, availablestoragespace,
                       int(firmwareversion), EnclosureNumber,
                       DiskNumber, VvNumber]
        }
        SaveExcels(data1)
        print(data1)

    def savetosheet2(self, r):
        p_hostinfo = '</objecthexuid>\n   <hostname>(.*?)</hostname>'
        hostinfo = re.findall(p_hostinfo, r, re.S)
        if hostinfo == []:
            p_hostinfo = '</timestampmodify>\n   <hostname>(.*?)</hostname>'
            hostinfo = re.findall(p_hostinfo, r, re.S)
        for hostname in hostinfo:
            # print(SerialNumber(fi), hostname)
            data2 = {
                '2、存储关联主机': [self.SerialNumber(fi), hostname]
            }
            global excel_headers_tuple
            excel_headers_tuple = ('序列号', '主机名')
            SaveExcels(data2)
            print(data2)

    def savetosheet3(self, r):
        p_hostinfo = '</objecthexuid>\n   <hostname>(.*?)</hostname>.*?<fcadapterports>(.*?)</fcadapterports>'
        hostinfo = re.findall(p_hostinfo, r, re.S)
        if hostinfo == []:
            p_hostinfo = '</timestampmodify>\n   <hostname>(.*?)</hostname>.*?<fcadapterports>(.*?)</fcadapterports>'
            hostinfo = re.findall(p_hostinfo, r, re.S)
        for hostname in hostinfo:
            p_wwn = '<portwwn>(.*?)</portwwn>'
            wwn = re.findall(p_wwn, hostname[1], re.S)
            for hostwwn in wwn:
                # print(SerialNumber(fi), hostname[0], hostwwn)
                data3 = {
                    '3、主机WWN': [self.SerialNumber(fi), hostname[0],
                                ':'.join(re.compile('.{2}').findall(hostwwn.replace('-', ''))), '存储端无法查看链路']
                }
                global excel_headers_tuple
                excel_headers_tuple = ('序列号', '主机名', '主机WWN', '主机链路')
                SaveExcels(data3)
                print(data3)

    def savetosheet4(self, r):
        xml = etree.HTML(r)  # 转为xml文档
        # 获取VV名字
        A = xml.xpath('//familyname/text()')
        B = A[:len(A) // 2]
        # 获取VV大小
        allocatedcapacity = xml.xpath('//allocatedcapacity/text()')
        # 获取VV_WWN
        wwlunid = xml.xpath('//wwlunid/text()')
        # print(B)
        for familyname, allocatedcapacity, wwlunid in zip(B, allocatedcapacity, wwlunid):
            data4 = {
                '4、存储vv信息': [self.SerialNumber(fi), familyname, allocatedcapacity + ' GB', wwlunid]
            }
            global excel_headers_tuple
            excel_headers_tuple = ('序列号', 'vvname', 'VV_Size', 'VV_WWN')
            SaveExcels(data4)
            print(data4)

    def savetosheet7(self, r):
        p_san = '<wwid>(500.*?)</wwid'
        san = re.findall(p_san, r, re.S)
        for i in san:
            data7 = {
                # ['序列号', '关联SAN的WWN']
                '7、EVA-SAN': [self.SerialNumber(fi), ':'.join(re.compile('.{2}').findall(i.replace(' ', '')))]
            }
            # print(data7)
            global excel_headers_tuple
            excel_headers_tuple = ('序列号', '存储端口WWN')
            SaveExcels(data7)
            print(data7)

    def savetosheet8(self, r):
        # 获取vlun信息
        p_vvmapinfo = '<familyname>(.*?)</familyname>.*?<wwlunid>(.*?)</wwlunid>.*?(<hostname>.*?)</hostaccess>'
        vvmapinfolist = re.findall(p_vvmapinfo, r, re.S)
        for vvmapinfo in vvmapinfolist:
            p_hostname = '<hostname>(.*?)</hostname>'
            hostnamelist = re.findall(p_hostname, vvmapinfo[-1], re.S)
            for hostname in hostnamelist:
                # print(self.SerialNumber(fi), vvmapinfo[0], vvmapinfo[1], hostname)
                data8 = {
                    '8、EVA-VLUN': [self.SerialNumber(fi), vvmapinfo[0], vvmapinfo[1], hostname.replace('\\Hosts\\', '')]
                }
                global excel_headers_tuple
                excel_headers_tuple = ('序列号', 'vvname', 'vv_wwn', 'hostname')
                SaveExcels(data8)
                print(data8)
                # print('-----已写入，此处耗时较长，等请待。。。')


class ThreePar_Storage_info(object):

    def SerialNumber(self, r):
        # 获取设备序列号
        p_SerialNumber = 'cli% shownode -i -svc\n(.*?)-1 FXN            (.*?)-63001      (.*?)   (.*?)       (.*?)           (.*?)       HP_3PAR'
        SerialNumber = re.search(p_SerialNumber, r, re.S).group(4).strip()
        return SerialNumber
        # print(SerialNumber)

    def savetosheet1(self, r):
        # 获取设备型号
        p_SystemModel = 'System Model       :(.*?)\n'
        SystemModel = '3par' + re.search(p_SystemModel, r, re.S).group(1).strip().split(' ')[1]
        # print(SystemModel)

        # 获取设备IP地址
        p_IPAddress = 'IP Address:(.*?)Netmask'
        IPAddress = re.search(p_IPAddress, r, re.S).group(1).strip()
        # print(IPAddress)

        # 获取固件版本及补丁
        p_Releaseversion = 'Release version (.*?)\n'
        Releaseversion = re.findall(p_Releaseversion, r, re.S)[2]
        # print(Releaseversion)
        p_Patches = 'Patches:  (.*?)\n'
        Patches = re.findall(p_Patches, r, re.S)[2]
        # print(Patches)
        version_patches = Releaseversion + '+' + Patches
        # print(version_patches)

        # 获取盘笼数量
        p_cage_entries = 'cage_entries: (.*?)\n'
        cage_entries = re.search(p_cage_entries, r, re.S).group(1)
        # print(cage_entries)

        # 获取物理硬盘数量
        p_pd_entries = 'pd_entries: (.*?)\n'
        pd_entries = re.search(p_pd_entries, r, re.S).group(1)
        # print(pd_entries)

        # 获取vv数量
        p_vv_entries = 'vv_entries: (.*?)\n'
        vv_entries = re.search(p_vv_entries, r, re.S).group(1)
        # print(vv_entries)

        # 获取裸容量方法1
        p_totalspace = 'cli% showpd -c\n.*?total\s.*?(\d.*?)\s.*?(\d.*?)\s.*?(\d.*?)\s.*?(\d.*?)\s.*?\n'
        totalspace = re.search(p_totalspace, r, re.S).group(1)
        if int(totalspace) >= 1024:
            totalspace = str(round(float(re.search(p_totalspace, r, re.S).group(1)) / 1024, 2)) + ' TB'
        else:
            totalspace = re.search(p_totalspace, r, re.S).group(1) + ' GB'
        # 获取已分配容量
        # usespace = re.search(p_totalspace, r, re.S).group(2) + ' GB'
        # # 获取未分配剩余容量
        freespace = re.search(p_totalspace, r, re.S).group(4)
        if int(freespace) >= 1024:
            freespace = str(round(float(re.search(p_totalspace, r, re.S).group(4)) / 1024, 2)) + ' TB'
        else:
            freespace = re.search(p_totalspace, r, re.S).group(4) + ' GB'
        # print(totalspace, usespace, freespace)

        # # 获取裸容量方法2
        # p_TotalCapacity = 'Total Capacity     :(.*?)\n'
        # TotalCapacity = int(re.search(p_TotalCapacity, r, re.S).group(1).strip())/1024
        # p_AllocatedCapacity = 'Allocated Capacity :(.*?)\n'
        # AllocatedCapacity = int(re.search(p_AllocatedCapacity, r, re.S).group(1).strip())/1024
        # p_FreeCapacity = 'Free Capacity      :(.*?)\n'
        # FreeCapacity = int(re.search(p_FreeCapacity, r, re.S).group(1).strip())/1024
        # p_FailedCapacity = 'Failed Capacity    :(.*?)\n'
        # FailedCapacity = int(re.search(p_FailedCapacity, r, re.S).group(1).strip())/1024
        # # print(TotalCapacity,AllocatedCapacity,FreeCapacity,FailedCapacity)

        # 单盘容量及数量分布
        p_disksize = 'cli% showpd\n.*?Capacity\(GB\)\n(.*?)--------'
        disksize = re.search(p_disksize, r, re.S).group(1).split('\n')
        disksize.pop(-1)
        aa = []
        for i in disksize:
            aa.append(i[-4:].strip() + 'GB')
        disksizecount = dict(Counter(aa))
        # print(str(disksizecount).replace("'", ''))
        data1 = {
            # ['序列号', '产品型号', 'IP地址', '裸容量', '剩余容量', '固件版本及补丁', 'cage数量', '硬盘数量', 'vv数量', '单盘容量及数量分布']
            '1、存储信息': [self.SerialNumber(r), SystemModel, IPAddress, totalspace, freespace, version_patches,
                       int(cage_entries),
                       int(pd_entries), int(vv_entries), str(disksizecount).replace("'", '')]
        }
        SaveExcels(data1)
        print(data1)

    def savetosheet2(self, r):
        # 获取存储连接主机名称
        p_hostname = 'Name       : (.*?)\n'
        hostnames = re.findall(p_hostname, r, re.S)
        # b = str(hostname).replace("'", '').replace(' ', '')[1:-1]
        # 一行显示所有主机名称
        # print(b)
        # hostnames = str(hostname).replace("'", '').replace(' ', '').replace(',', '\n')[1:-1]
        # 换行显示所有主机名称
        # print(hostnames)
        for i in hostnames:
            data2 = {
                '2、存储关联主机': [self.SerialNumber(r), i.replace(' ', '')]
            }
            global excel_headers_tuple
            excel_headers_tuple = ('序列号', '主机名')
            SaveExcels(data2)
            print(data2)

    def savetosheet3(self, r):
        # 获取存储连接主机链路信息
        p_hostlinks = 'cli% showhost -d\n.*?IP_addr\n(.*?) cli%'
        hostlinks = re.search(p_hostlinks, r, re.S).group(1).split('\n')
        while (':' or 'n/a') not in hostlinks[-1]:
            hostlinks.pop(-1)
        for i in hostlinks:
            # c = ' '.join(i.split())   # 将字符串多个空格替换成一个空格
            a = i.split()[1]  # 主机名
            b = ':'.join(re.compile('.{2}').findall(i.split()[3]))  # 主机WWN
            c = i.split()[4]  # 主机链路
            data3 = {
                '3、主机WWN': [self.SerialNumber(r), a, b, c]
            }
            global excel_headers_tuple
            excel_headers_tuple = ('序列号', '主机名', '主机WWN', '主机链路')
            SaveExcels(data3)
            print(data3)

    def savetosheet4(self, r):
        # 获取vv信息
        p_vvwwn = 'cli% showvv -d\n.*?Udid\n(.*?)----------'
        vvwwn = re.search(p_vvwwn, r, re.S).group(1).split('\n')
        vvwwn.pop(0)
        vvwwn.pop(0)
        vvwwn.pop(-1)
        # for i in vvwwn:
        #     # c = ' '.join(i.split())   # 将字符串多个空格替换成一个空格
        #     a = i.split()[1]    # vv名字
        #     b = i.split()[-5]   # vvWWN
        #     print(b, a)
        # 获取vvsize信息
        p_vvsize = 'cli% showvv\n.*?VSize\n(.*?)----------'
        vvsize = re.search(p_vvsize, r, re.S).group(1).split('\n')
        vvsize.pop(0)
        vvsize.pop(0)
        vvsize.pop(-1)
        for i in vvsize:
            # c = ' '.join(i.split())   # 将字符串多个空格替换成一个空格
            a = i.split()[1]
            b = int(i.split()[-1]) / 1024
            if b >= 1024:
                c = str(int(b / 1024)) + ' TB'
            else:
                c = str(int(b)) + ' GB'
            # print(c)
        for i, j in zip(vvwwn, vvsize):
            a = i.split()[1]  # vv名字
            b = i.split()[-5]  # vvWWN
            c = j.split()[1]
            d = int(j.split()[-1]) / 1024
            if d >= 1024:
                e = str(int(d / 1024)) + ' TB'
            else:
                e = str(int(d)) + ' GB'
            # print(a,e,b)
            data4 = {
                '4、存储vv信息': [self.SerialNumber(r), a, e, b]
            }
            global excel_headers_tuple
            excel_headers_tuple = ('序列号', 'vvname', 'VV_Size', 'VV_WWN')
            SaveExcels(data4)
            print(data4)

    def savetosheet5(self, r):
        # 获取vlun信息
        p_vlun = 'cli% showvlun\n.*?Status ID\n(.*?)----------'
        vlun = re.search(p_vlun, r, re.S).group(1).split('\n')
        vlun.pop(-1)
        for i in vlun:
            # c = ' '.join(i.split())   # 将字符串多个空格替换成一个空格
            a = i.split()[1]  # vvname
            b = i.split()[2]  # hostname
            c = ':'.join(re.compile('.{2}').findall(i.split()[3]))  # hostwwn
            d = i.split()[4]  # port
            e = i.split()[-2]  # 链路status
            # print(a, b, c, d, e)
            data5 = {
                '5、3par-VLUN': [self.SerialNumber(r), a, b, c, d, e]
            }
            global excel_headers_tuple
            excel_headers_tuple = ('序列号', 'vvname', 'hostname', 'hostwwn', 'port', '链路状态')
            SaveExcels(data5)
            print(f'{i.split()[0]}\t-----已写入，此处耗时较长，等请待。。。')
        print('保存完成')

    def savetosheet6(self, r):
        p_san = 'Name:           (.*?)\n'
        san = re.findall(p_san, r, re.S)
        for i in list(set(san)):
            i = ':'.join(re.compile('.{2}').findall(i))
            # print(SerialNumber(r), i)
            data6 = {
                # ['序列号', '关联SAN的WWN']
                '6、3par-SAN': [self.SerialNumber(r), i]
            }
            global excel_headers_tuple
            excel_headers_tuple = ('序列号', '光交WWN')
            SaveExcels(data6)
            print(data6)


class SAN_Switch_info(object):
    def savetosheet9(self, r):
        # 获取switchWwn
        switchWwn = re.findall('switchWwn:      (.*?)\n', r, re.S)[0]

        # 获取设备IP地址
        IP = re.findall('Ethernet IP Address: (.*?)\n', r, re.S)[0]

        # 获取固件版本
        version = re.findall('Fabric OS:  (.*?)\n', r, re.S)[0]

        global excel_headers_tuple
        excel_headers_tuple = ('序列号', 'IP地址', '固件版本')
        # 保存数据
        data1 = {
            # ['序列号', 'IP地址', '固件版本']
            '1、SAN信息': [SN, IP, version, switchWwn]
        }
        print(data1)
        SaveExcels(data1)

    def savetosheet10(self, r):
        # 获取wwn
        for line in r.readlines():
            # p_list = ['Online', '    FC  ']
            p_list = ['Online      FC  F-Port']
            xxx = ['NPIV']
            # if all(s in line for s in p_list) and (xxx not in line):
            if p_list[0] in line and xxx[0] not in line:
                a = line.split()
                if a[-8] != a[-9]:
                    list1 = [SN, a[-9] + '/' + a[-8], a[-1]]
                else:
                    list1 = [SN, int(a[-8]), a[-1]]
                # 保存数据
                global excel_headers_tuple
                excel_headers_tuple = ('序列号', '端口', 'portwwn')
                data2 = {
                    # ['序列号', '端口', 'portwwn']
                    '2、SAN-portwwn信息': list1
                }
                print(data2)
                SaveExcels(data2)


starttime = datetime.now()
if __name__ == '__main__':

    files = list_all_files(src_dir)
    for fi in files:
        if fi[-4:] == '.log':
            pass
            try:
                with open(fi, "r", encoding="utf-8") as f:
                    r = f.read()
                    T = ThreePar_Storage_info()
                    T.savetosheet1(r)
                    T.savetosheet2(r)
                    T.savetosheet3(r)
                    T.savetosheet4(r)
                    T.savetosheet5(r)
                    T.savetosheet6(r)
            except:
                print(f'{fi}---数据未获取到')
            else:
                pass
            try:
                with open(fi, 'r', encoding='utf-8') as f:
                    r = f.read()
                    S = SAN_Switch_info()
                    # 获取设备序列号Serial Num:
                    p_SN = 'Serial Num:             (.*?)\n'
                    SN = re.findall(p_SN, r, re.S)[-1]
                    S.savetosheet9(r)
                with open(fi, 'r', encoding='utf-8') as f:
                    S.savetosheet10(f)
            except:
                print('---------error')
            else:
                pass
            # break
        elif fi[-4:] == '.xml':
            try:
                with open(fi, "r", encoding="utf-8") as f:
                    r = f.read()
                    E = EVA_Storage_info()
                    E.SerialNumber(fi)
                    E.savetosheet1(r)  # ok
                    E.savetosheet2(r)  # ok
                    E.savetosheet3(r)  # ok
                    E.savetosheet4(r)  # ok
                    E.savetosheet7(r)  # ok
                    E.savetosheet8(r)  # ok

            except:
                print(f'{fi}---数据未获取到')
            else:
                pass
            # break
        else:
            pass
    print('DOWN')

###########################################
endtime = datetime.now()
usetime = endtime - starttime
print(starttime)
print(endtime)
print(usetime)
