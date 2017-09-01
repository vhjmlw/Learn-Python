# -*- coding:utf-8 -*-

class SweetProtato(object):

    def __init__(self):
        self.string = '生的'
        self.level = 0
        self.condiment = []

    def cook(self,add_level):
        self.level += add_level
        if self.level > 0 and self.level <= 3:
            self.string = '生的'
        elif self.level > 3 and self.level <=5 :
            self.string = '半生不熟'
        elif self.level > 5 and self.level <= 8 :
            self.string = '熟了'
        elif self.level > 8:
            self.string = '烤糊了'

    def __str__(self):
        return '烤的level：%d，烤的程度：%s，加的佐料：%s'%(self.level,self.string,str(self.condiment))

    def add_condiment(self,condiment):
        self.condiment.append(condiment)

a = SweetProtato()
a.cook(1)
print(a)
a.cook(2)
print(a)
a.cook(1)
print(a)
a.add_condiment('生蚝')
a.cook(3)
a.add_condiment('鲍鱼')
print(a)
a.cook(5)
a.add_condiment('鱼翅')
print(a)
