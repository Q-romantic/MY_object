import socket  # 导入 socket 模块

s = socket.socket()  # 创建 socket 对象

# host = socket.gethostname()  # 获取本地主机名
# port = 12345  # 设置端口号

hostname = 'DESKTOP-14ALFQN'
port = 22345

sysinfo = socket.gethostbyname_ex(hostname)
print(sysinfo)

s.connect((hostname, port))
print(s.recv(1024).decode(encoding='utf-8'))
s.close()