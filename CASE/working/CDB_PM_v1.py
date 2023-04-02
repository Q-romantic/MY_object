import os
import re
import sys
import time
import multiprocessing
from datetime import datetime

starttime = datetime.now()

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


@clock
@run
def XunJianInfo():
    print(
        '序号' + '\t' + '主机名' + '\t' + 'IP地址' + '\t' + '当前系统补丁' + '\t' + '强制最低系统补丁' + '\t\t' + '推荐补丁版本' + '\t' + 'HBA卡补丁版本' + '\t' + '推荐升级HBA卡版本' + '\t' + '网卡补丁版本' + '\t' + '推荐网卡补丁版本' + '\t' + '其他需要升级补丁' + '\t' + '目前版本' + '\t' + '推荐升级版本')

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

            # with open('./tmp.txt', 'a') as g:
            #     g.write(hostname[0] + '\t' + uptime[0] + '\t' + ip.group().split(':')[1].strip() + '\n')
            print(str(Num) + '\t' + hostname[0] + '\t' + ip.group().split(':')[1].strip() + '\t' + uptime[0].split(',')[
                0],
                  end="\t")

            p_FEATURE11i = '(FEATURE11i.*?B\..*?)\s'
            FEATURE11i = re.search(p_FEATURE11i, r, re.S)
            print('_'.join(FEATURE11i.group().split()), end="\t\t")

            ###################### 推荐补丁版本
            print('FEATURE11i_B.11.31.1905.441', end="\t")
            ######################

            p_FibrChanl_01 = '(FibrChanl-01.*?B\..*?)\s'
            FibrChanl_01 = re.search(p_FibrChanl_01, r, re.S)
            print('"' + '_'.join(FibrChanl_01.group().split()))
            p_FibrChanl_02 = '(FibrChanl-02.*?B\..*?)\s'
            FibrChanl_02 = re.search(p_FibrChanl_02, r, re.S)
            print('_'.join(FibrChanl_02.group().split()) + '"', end="\t")

            ###################### 推荐升级HBA卡版本
            print('"' + 'FibrChanl-01_B.11.31.1905')
            print('FibrChanl-02_B.11.31.1805' + '"', end="\t")
            ######################

            p_IEther_00 = '(IEther-00.*?B\..*?)\s'
            IEther_00 = re.search(p_IEther_00, r, re.S)
            print('"' + '_'.join(IEther_00.group().split()))
            p_GigEthr_02 = '(10GigEthr-02.*?B\..*?)\s'
            GigEthr_02 = re.search(p_GigEthr_02, r, re.S)
            print('_'.join(GigEthr_02.group().split()))
            p_GigEthr_03 = '(10GigEthr-03.*?B\..*?)\s'
            GigEthr_03 = re.search(p_GigEthr_03, r, re.S)
            print('_'.join(GigEthr_03.group().split()) + '"', end="\t")

            ###################### 推荐网卡补丁版本
            print('"' + 'IEther-00_B.11.31.1806')
            print('10GigEthr-02_B.11.31.1905')
            print('10GigEthr-03_B.11.31.2010' + '"', end="\t")
            ######################

            ###################### 其它需要升级补丁
            print('QPK1131', end="\t")
            ######################

            p_QPKBASE = '(QPKBASE.*?B\..*?)\s'
            QPKBASE = re.search(p_QPKBASE, r, re.S)
            print('"' + '_'.join(QPKBASE.group().split()).replace("BASE", "1131"))
            p_HWEnable11i = '(HWEnable11i.*?B\..*?)\s'
            HWEnable11i = re.search(p_HWEnable11i, r, re.S)
            print('_'.join(HWEnable11i.group().split()) + '"', end="\t")

            ###################### 推荐升级版本
            print('"' + 'QPK1131_B.11.31.2009.447c')
            print('HWEnable11i_B.11.31.1703.423' + '"', end="\t")
            ######################

            # print('----'*20)
            print('"', end="")
            for j in use:
                if (int(j.split('%')[0]) >= 90):
                    print(j)
            print('"')


###########################################
if __name__ == '__main__':
    XunJianInfo()
