# -*- coding:utf-8 -*-

def fn(a,b,c=5,d=6):
    print(a,b,c,d)

fn(1,2)
fn(1,2,3)
fn(1,2,3,4)
fn(1,2,d='d')
fn(a=1,c='c',b=2,d='d')

