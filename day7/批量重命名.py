# -*- coding:utf-8 -*-

import os

folder_name = input('请输入目录：')

os.chdir(folder_name)

for x in os.listdir():
    if os.path.isfile(x):
        os.rename(x,'批量重命名_'+x)


