# -*- coding:utf-8 -*-

'死锁'

__author__ = '建磊'

import time
from threading import Thread
from threading import Lock

def main():

    class Task1(Thread):
        def run(self):
            while True:
                if lock1.acquire():
                    print('task1')
                    time.sleep(1)
                    lock2.release()

    class Task2(Thread):
        def run(slef):
            while True:
                if lock2.acquire():
                    print('task2')
                    time.sleep(1)
                    lock3.release()

    class Task3(Thread):
        def run(self):
            while True:
                if lock3.acquire():
                    print('task3')
                    time.sleep(1)
                    lock1.release()

    lock1 = Lock()
    lock2 = Lock()
    lock3 = Lock()
    lock2.acquire()
    lock3.acquire()

    task1 = Task1()
    task2 = Task2()
    task3 = Task3()
    task1.start()
    task2.start()
    task3.start()

if __name__ == '__main__':
    main()
