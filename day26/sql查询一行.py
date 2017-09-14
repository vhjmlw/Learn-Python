# -*- coding:utf-8 -*-

'SQL 查询一条数据'

__author__ = '建磊'

from pymysql import *
import time

def main():
    conn = connect(host='localhost',port=3306,user='root',passwd='root',db='python',charset='utf8')
    cur = conn.cursor()
    sql = 'select * from areas where title like "%省"'
    cur.execute(sql)
    while True:
        result = cur.fetchone()
        print(result)
        time.sleep(1)
    conn.commit()
    cur.close()
    cur.close()

if __name__ == '__main__':
    main()
