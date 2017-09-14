# -*- coding:utf-8 -*-

'SQL查询多行'

__author__ = '建磊'

from pymysql import *
import time

def main():
    conn = connect(host='localhost',port=3306,user='root',passwd='root',db='python',charset='utf8')
    cur = conn.cursor()
    sql = 'select * from areas limit 0,10'
    cur.execute(sql)
    result_tuple = cur.fetchall()
    print(str(result_tuple))
    for x in result_tuple:
        print(str(x))

if __name__ == '__main__':
    main()
