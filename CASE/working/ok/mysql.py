# -*- coding: utf-8 -*-
"""
@Time    : 2023/1/9  009 下午 15:09
@Author  : Jan
@File    : mysql.py
"""

import pymysql as mysql
import pandas as pd

""" {python操作mysql数据库} """
""" mysql 设置网页访问 网友参考 https://www.php.cn/mysql-tutorials-461081.html """

# 连接Mysql数据库
db = mysql.connect(host="localhost", port=3306, user="root", passwd="root", db="xujian", charset='utf8mb4')
# 通过cursor创建游标
cursor = db.cursor()

# 创建库 & 表 & 查表 & 删库
"""
# 创建库名（database_name）
create database database_name;
# 使用库
use database_name
# 创建表
CREATE TABLE table_name (
id bigint(18) NOT NULL AUTO_INCREMENT,
dep varchar(3) NOT NULL DEFAULT '',
arr varchar(3) NOT NULL DEFAULT '',
flightNo varchar(10) NOT NULL DEFAULT '',
flightDate date NOT NULL DEFAULT '1000-10-10',
flightTime varchar(20) NOT NULL DEFAULT '',
isCodeShare tinyint(1) NOT NULL DEFAULT '0',
tax int(11) NOT NULL DEFAULT '0',
yq int(11) NOT NULL DEFAULT '0',
cabin char(2) NOT NULL DEFAULT '',
ibe_price int(11) NOT NULL DEFAULT '0',
ctrip_price int(11) NOT NULL DEFAULT '0',
official_price int(11) NOT NULL DEFAULT '0',
uptime datetime NOT NULL DEFAULT '1000-10-10 10:10:10',
PRIMARY KEY (id),
UNIQUE KEY uid (dep,arr,flightNo,flightDate,cabin),
KEY uptime (uptime),
KEY flight (dep,arr),
KEY flightDate (flightDate)
) ENGINE=InnoDB  DEFAULT CHARSET=gbk;
# 查看表
show tables;
# 删除库
drop database database_name;
# 或者不登录 mysql 删库
mysqladmin -u root -p drop database_name
"""

# 创建sql语句，并执行
# 插入数据，方法一：（列表，列表方式）
table = 'student'
headers = ['name', 'password', 'age', 'register_date', 'phone']
data = [
    ('xujian', 'xujian', 18, '2023-01-09', '1'),
    ('xujian', 'xujian', 18, '2023-01-09', '2'),
    ('xujian', 'xujian', 18, '2023-01-09', '3'),
]
keys = ', '.join(headers)
values = ', '.join(['%s'] * len(headers))

sql = f"""insert into {table} ({keys}) values ({values});"""
# sql = """INSERT INTO {table} ({keys}) VALUES ({values});""".format(table=table, keys=keys, values=values)
cursor.executemany(sql, data)
# 插入数据，方法二：（单行）
sqls = [
    """insert into student (name,password,age,register_date,phone) values ('xujian','xujian',18,'2023-01-09','123456');""",
    # """delete from student where id>2;""",
    # """update student set age=28 where id=1;""",
    #
    # # 从 student 表删除 register_date 字段
    # # """alter table student drop register_date;""",
    # # 添加 phone 字段
    # """alter table student add phone int(11);""",

    """select * from xujian.student;""",
]
for sql in sqls:
    cursor.execute(sql)

# 提取1行数据
# result = cursor.fetchone()
# print(result)

# 提取全部数据
result2 = cursor.fetchall()
# print(result2)
result3 = pd.DataFrame(result2)
print(result3)

# close
db.commit()
cursor.close()
db.close()

from sqlalchemy import create_engine

#  数据以 dataframe 完整读取
# engine = create_engine('mysql+pymysql://用户名:密码@主机:端口/库名?charset=utf8')
engine = create_engine("""mysql+pymysql://root:root@localhost:3306/xujian?charset=utf8mb4""")
sql = f"select {keys} from xujian.student;"
df = pd.read_sql(sql, engine)
print(df)

#  数据以 dataframe 完整写入
# # df = pd.read_csv("C:\\Users\\Administrator\\Downloads\\iris.csv", index_col=0)  # 读取数据
# df = pd.read_excel(r'./111.xlsx')  # 读取数据
print(df.head(5))  # 查看前5行数据
#  表头必须和数据库表头一致
df.to_sql(table, con=engine, if_exists='append', index=False)
