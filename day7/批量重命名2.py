# -*- coding:utf-8 -*-

import os

folder_name = input('请输入重命名的目录：')

for x in os.listdir(folder_name):
    old_name = folder_name + '/' + x
    new_name = folder_name + '/' + '[重命名]-' + x
    print(old_name,new_name)
    os.rename(old_name, new_name)
