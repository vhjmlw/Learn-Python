# -*- coding:utf-8 -*-

'使用封装的MySQL操作'

__author__ = '建磊'

from 封装 import MySQL

mysql = MySQL(host='localhost',user='root',passwd='root',db='python')
sql = 'update areas set title=%s where id=%s'
param = ['北京天安门','110000']
mysql.in_de_up(sql,param)

sql2 = 'select * from areas limit 0,5'
result = mysql.fetch_one(sql2)
print(result)

sql3 = 'select * from areas limit 0,5'
result_tuple = mysql.fetch_all(sql3)
for x in result_tuple:
    print(x)
