# -*- coding:utf-8 -*-

'实现用户登录效果'

__author__ = '建磊'

from 封装 import MySQL
from hashlib import sha1

def main():
    while True:
        name = input('请输入用户名:')
        passwd = input('请输入密码:')

        sha = sha1()
        sha.update(passwd.encode('utf-8'))
        new_passwd = sha.hexdigest()

        sql = 'select passwd from users where name=%s'
        param=[name]
        mysql = MySQL(host='localhost',user='root',passwd='root',db='python')
        result = mysql.fetch_all(sql,param)

        if len(result) == 0:
            print('用户名错误')
        elif result[0][0] == new_passwd:
            print('登陆成功')
            break
        else:
            print('密码错误')


if __name__ == '__main__':
    main()
