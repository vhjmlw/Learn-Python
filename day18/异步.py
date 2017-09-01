# -*- coding:utf-8 -*-

'异步'

__author__ = '建磊'

from multiprocessing import Pool

#为啥把下面的代码放在main()方法里面就不行？？？为啥？？
def fn1():
    print('fn1执行了')
    return 'hello world'

def fn2(tmp):
    print(tmp)

pool = Pool(3)
pool.apply_async(func=fn1,callback=fn2)
pool.close()#close方法一定要调用，否则会报错，为啥？？？
pool.join()
print('主线程执行完毕')
