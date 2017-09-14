# -*- coding:utf-8 -*-

'封装MySQL操作'

__author__ = '建磊'

from pymysql import *

class MySQL(object):
    def __init__(self,host,user,passwd,db,port=3306,charset='utf8'):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.port = port
        self.charset = charset

    def open(self):
        self.conn = connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,db=self.db,charset=self.charset)
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def in_de_up(self,sql,param=[]):
        self.open()

        self.cur.execute(sql,param)
        self.conn.commit()

        self.close()
        print('done')

    def fetch_one(self,sql,param=[]):
        self.open()
        self.cur.execute(sql,param)
        result = self.cur.fetchone()
        self.close()
        print('done')
        return result

    def fetch_all(self,sql,param=[]):
        self.open()
        self.cur.execute(sql,param)
        result = self.cur.fetchall()
        self.close()
        print('done')
        return result
