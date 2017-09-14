# -*- coding:utf-8 -*-

'SQL 参数化'

__author_ = '建磊'

from pymysql import *

def main():
    conn = connect(host='localhost',port=3306,user='root',passwd='root',db='python',charset='utf8')
    cur = conn.cursor()
    cur.execute('update areas set title=%s where title=%s',['大北京','北京天安门'])
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
