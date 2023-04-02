import os
import re
import sys
import time
import xlwt
import xlrd
import multiprocessing
from xlutils.copy import copy

# src_dir = r'./files/'  # 源文件目录地址
src_dir = sys.argv[1]  # 需带参数指定源文件目录地址


def list_all_files(rootdir):
    _files = []

    # 列出文件夹下所有的目录与文件
    list_file = os.listdir(rootdir)
    for i in range(0, len(list_file)):
        # 构造路径
        path = os.path.join(rootdir, list_file[i])
        # 判断路径是否是一个文件目录或者文件
        # 如果是文件目录，继续递归
        if os.path.isdir(path):
            _files.extend(list_all_files(path))
        if os.path.isfile(path):
            _files.append(path)
    return _files


files = list_all_files(src_dir)


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
    os_mkdir_path = os.getcwd() + '/数据/'
    # 判断这个路径是否存在，不存在就创建
    if not os.path.exists(os_mkdir_path):
        os.mkdir(os_mkdir_path)
    # 判断excel表格是否存在           工作簿文件名称
    os_excel_path = os_mkdir_path + '1.xlsx'
    if not os.path.exists(os_excel_path):
        # 不存在，创建工作簿(也就是创建excel表格)
        workbook = xlwt.Workbook(encoding='utf-8')
        """工作簿中创建新的sheet表"""  # 设置表名
        worksheet1 = workbook.add_sheet("sheet1", cell_overwrite_ok=True)
        """设置sheet表的表头"""
        sheet1_headers = (
            '序号', '主机名', 'IP地址', '当前系统补丁', '强制最低系统补丁', '', '推荐补丁版本', 'HBA卡补丁版本', '推荐升级HBA卡版本', '网卡补丁版本', '推荐网卡补丁版本',
            '其他需要升级补丁', '目前版本', '推荐升级版本')
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


def clock(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("...The End...")
        print("共耗时：%s秒" % round(end_time - start_time, 2))
        return result

    return wrapper


def run(func):
    def wrapper(*args, **kwargs):
        running_process = multiprocessing.Process(target=running)
        running_process.daemon = True  # 方法一：开始前设置守护主进程
        running_process.start()
        result = func(*args, **kwargs)
        # running_process.terminate()  # 方法二：结束时手动结束子进程
        return result

    return wrapper


def running():
    while True:
        print('...running...')
        time.sleep(0.1)


# @clock
# @run
class XunJianInfo(object):
    @clock
    @run
    def CDB_XunJianInfo(self):
        Num = 0
        for fi in files:
            with open(fi) as f:
                r = f.read()
                Num += 1

                p_hostname = 'Nodename:.*?(\w.*?)\n'
                hostname = re.findall(p_hostname, r, re.S)

                p_uptime = 'up\s(.*?)load average:'
                uptime = re.findall(p_uptime, r, re.S)

                p_use = '(\d\d{0,1}%\s/.*?)\n'
                use = re.findall(p_use, r, re.S)

                p_ip = 'IP address:.*?(1.*?)\n'
                ip = re.search(p_ip, r, re.S)

                p_FEATURE11i = '(FEATURE11i.*?B\..*?)\s'
                FEATURE11i = re.search(p_FEATURE11i, r, re.S)

                p_FibrChanl_01 = '(FibrChanl-01.*?B\..*?)\s'
                FibrChanl_01 = re.search(p_FibrChanl_01, r, re.S)

                p_FibrChanl_02 = '(FibrChanl-02.*?B\..*?)\s'
                FibrChanl_02 = re.search(p_FibrChanl_02, r, re.S)

                p_IEther_00 = '(IEther-00.*?B\..*?)\s'
                IEther_00 = re.search(p_IEther_00, r, re.S)
                p_GigEthr_02 = '(10GigEthr-02.*?B\..*?)\s'
                GigEthr_02 = re.search(p_GigEthr_02, r, re.S)
                p_GigEthr_03 = '(10GigEthr-03.*?B\..*?)\s'
                GigEthr_03 = re.search(p_GigEthr_03, r, re.S)

                p_QPKBASE = '(QPKBASE.*?B\..*?)\s'
                QPKBASE = re.search(p_QPKBASE, r, re.S)
                p_HWEnable11i = '(HWEnable11i.*?B\..*?)\s'
                HWEnable11i = re.search(p_HWEnable11i, r, re.S)

                li = []
                for j in use:
                    if (int(j.split('%')[0]) >= 80):
                        li.append(j)

                A = Num
                B = hostname[0]
                C = ip.group().split(':')[1].strip()
                D = uptime[0].split(',')[0]
                E = '_'.join(FEATURE11i.group().split())
                F = ''
                G = 'FEATURE11i_B.11.31.1905.441'
                H = '_'.join(FibrChanl_01.group().split()) + '\n' + '_'.join(FibrChanl_02.group().split())
                I = 'FibrChanl-01_B.11.31.1905' + '\n' + 'FibrChanl-02_B.11.31.1805'
                J = '_'.join(IEther_00.group().split()) + '\n' + '_'.join(GigEthr_02.group().split()) + '\n' + '_'.join(
                    GigEthr_03.group().split())
                K = 'IEther-00_B.11.31.1806' + '\n' + '10GigEthr-02_B.11.31.1905' + '\n' + '10GigEthr-03_B.11.31.2010'
                L = 'QPK1131'
                M = '_'.join(QPKBASE.group().split()).replace("BASE", "1131") + '\n' + '_'.join(
                    HWEnable11i.group().split())
                N = 'QPK1131_B.11.31.2009.447c' + '\n' + 'HWEnable11i_B.11.31.1703.423'

                data = {
                    'sheet1': [A, B, C, D, E, F, G, H, I, J, K, L, M, N, li]
                }
                SaveExcel(data)


###########################################
if __name__ == '__main__':
    filename = os.getcwd() + '\\数据\\' + '1.xlsx'
    os.remove(filename)
    X = XunJianInfo()
    X.CDB_XunJianInfo()
    print('\n' + '生成文件保存路径为：' + filename + '\n')
