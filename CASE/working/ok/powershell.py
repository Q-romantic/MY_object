# -*- coding: utf-8 -*-
"""
@Time    : 2023/1/10  010 下午 22:55
@Author  : Jan
@File    : powershell.py
"""

import os
import re
import subprocess
from glob import glob
import subprocess as sp

""" {python 调用 powershell} """
""" {批量查询 windows 已连接过的 wifi 账号 & 密码} """

""" # 用到的 powershell 命令
alias | out-string -stream | sls object     # | 使用参考，没太理解到
netsh wlan show profiles | sls "所有用户配置文件"
netsh wlan show profile name="ChinaNet-eP3b" key="clear" | sls "关键内容"
"""


def checkLocalWifiPassword():
    powershell = '''netsh wlan show profiles'''.split()
    #  主要代码，注意：修改 window 默认编码为 utf-8 后不能指定 decode 为 GBK
    # result = subprocess.Popen(powershell, stdout=subprocess.PIPE).stdout.read().decode('GBK')
    result = subprocess.Popen(powershell, stdout=subprocess.PIPE).stdout.read().decode()
    # li = re.findall("所有用户配置文件 \s+: (.*?)\r\n", result, re.S)
    # li = re.findall("All User Profile \s+: (.*?)\r\n|Profiles on (.*?) WLAN:\r\n", result, re.S)  # 此方法有缺陷，采用 “零宽断言” 方式升级如下
    li = re.findall("(?<=All User Profile\s{5}: ).*?(?=\r\n)|(?<=所有用户配置文件\s{5}: ).*?(?=\r\n)", result, re.S)
    for i in li:
        try:
            powershell = f'''netsh wlan show profile name="{i}" key="clear"'''.split()
            result = subprocess.Popen(powershell, stdout=subprocess.PIPE).stdout.read().decode()
            # li = re.findall("名称.*?: (.*?)\r\n.*?关键内容.*?: (.*?)\r\n", result, re.S)[0]
            li = re.findall('(?<=SSID name\s{14}: ").*?(?="\r\n)|(?<=Key Content\s{12}: ).*?(?=\r\n)', result, re.S)
            # print(li)
            print("账号：" + li[0])
            print("密码：" + li[1])
            print('---' * 4)
        except:
            # print(f'''netsh wlan show profile name="{i}" key="clear"''')
            pass


def other():
    """ 补充 python 调用 cmd 3种方法 """
    cmd = "date /t & time /t"  # 连续执行多条命令有： &  &&  ||
    # cmd = "powershell.exe date"  # 有缺点，不支持管道之后命令操作
    powershell_cmd = r'netsh wlan show profiles | sls "All User Profile"'
    # 执行 powershell 优化
    ps = PowerShell('UTF-8')
    outs, errs = ps.run(powershell_cmd)
    print(outs)

    # 1、OS 模块
    os.system(cmd)  # 输出中文有乱码，改 windows 区域设置，勾选 Beta 版使用 Utf-8 全局编码后解决
    # 2、OS 模块 popen 方法

    outs = os.popen(cmd).read()
    print(outs)  # 有返回值

    # 3、subprocess 模块
    sub = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    sub.wait()
    outs = sub.stdout.read().decode()
    print(outs)


class PowerShell:
    # from scapy
    def __init__(self, coding='GBK', ):
        cmd = [self._where('PowerShell.exe'),
               "-NoLogo", "-NonInteractive",  # Do not print headers
               "-Command", "-"]  # Listen commands from stdin
        startupinfo = sp.STARTUPINFO()
        startupinfo.dwFlags |= sp.STARTF_USESHOWWINDOW
        self.popen = sp.Popen(cmd, stdout=sp.PIPE, stdin=sp.PIPE, stderr=sp.STDOUT, startupinfo=startupinfo)
        self.coding = coding

    def __enter__(self):
        return self

    def __exit__(self, a, b, c):
        self.popen.kill()

    def run(self, cmd, timeout=15):
        b_cmd = cmd.encode(encoding=self.coding)
        try:
            b_outs, errs = self.popen.communicate(b_cmd, timeout=timeout)
        except sp.TimeoutExpired:
            self.popen.kill()
            b_outs, errs = self.popen.communicate()
        outs = b_outs.decode(encoding=self.coding)
        return outs, errs

    @staticmethod
    def _where(filename, dirs=None, env="PATH"):
        """Find file in current dir, in deep_lookup cache or in system path"""
        if dirs is None:
            dirs = []
        if not isinstance(dirs, list):
            dirs = [dirs]
        if glob(filename):
            return filename
        paths = [os.curdir] + os.environ[env].split(os.path.pathsep) + dirs
        try:
            return next(os.path.normpath(match)
                        for path in paths
                        for match in glob(os.path.join(path, filename))
                        if match)
        except (StopIteration, RuntimeError):
            raise IOError("File not found: %s" % filename)


if __name__ == '__main__':
    pass
    # # Example:
    # ps = PowerShell('UTF-8')
    # outs, errs = ps.run(r'Get-ChildItem G:\test1 -recurse|?{$_.Name -like "test*"}|select Name')
    # print(outs)

    # ps = PowerShell('UTF-8')
    # outs, errs = ps.run(r'netsh wlan show profiles | sls "All User Profile"')
    # print(outs)

    # 查看本地电脑已连接过的 WiFi 账号/密码
    checkLocalWifiPassword()

    # 补充 python 调用 cmd 3种方法
    # 拼多多()
