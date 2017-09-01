# -*- coding:utf-8 -*-

'生产者消费者模式'

__author__ = '建磊'

from threading import Thread
from threading import Lock
import time
from queue import Queue

que = Queue()

def main():

    class Producer(Thread):
        def run(self):
            global que
            while True:
                if que.qsize() < 1000:
                    time.sleep(1)
                    for x in range(100):
                        lock.acquire()
                        msg = '产品%s'%(que.qsize())
                        print(msg)
                        que.put(msg)
                        lock.release()

    class Consumer(Thread):
        def run(self):
            global que
            while True:
                if que.qsize() > 100:
                    time.sleep(1)
                    for x in range(3):
                        if not que.empty():
                            lock.acquire()
                            msg = que.get()
                            print('取出%s'%msg)
                            lock.release()

    for x in range(500):
        que.put('产品%s'%x)

    lock = Lock()

    for x in range(2):
        producer = Producer()
        producer.start()
    for x in range(5):
        consumer = Consumer()
        consumer.start()

if __name__ == '__main__':
    main()
