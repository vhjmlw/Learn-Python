# -*- coding:utf-8 -*-

'Python与MySQL交互'

__author__ = '建磊'

from pymysql import *

def main():
    conn = connect(host='localhost',port=3306,user='root',passwd='root',db='python',charset='utf8')
    cur = conn.cursor()
    sql = 'select * from areas limit 0,5'
    tmp = cur.execute(sql)
    print(tmp)
    sql2 = 'update areas set title="大北平" where id=110000'
    cur.execute(sql2)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
