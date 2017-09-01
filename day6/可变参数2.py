# -*- coding:utf-8 -*-

def fn(a,b,*args):
    result = a + b
    for x in args:
        result += x
    print('参数累加的结果：%s'%result)

fn(1,2,3,4,5,)
