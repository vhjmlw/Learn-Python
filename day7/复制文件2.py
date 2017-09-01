# -*- coding:utf-8 -*-

old_file_name = input('请输入要复制的文件名')

old_file = open(old_file_name,'r')

#获取 . 的索引位置，根据旧的文件名生成一个新的文件名
#注意在查找索引的时候要使用rfind()才合理，切片使用的很巧妙
point_index = old_file_name.rfind('.')
new_file_name = old_file_name[:point_index] + '[复本]' + old_file_name[point_index:]

new_file = open(new_file_name,'w')

#考虑到复制的文件可能很大，所以使用read()一次性读取所有的内容不太合理
#应该使用循环每次读取指定长度的内容read(1024*100)每次读取100KB
#如果检测到读取的内容长度为0，则说明文件的内容读取结束，应该结束循环
while True:
    content = old_file.read(1024*100)
    if len(content) == 0:
        break
    new_file.write(content)

#最后记得关闭文件
old_file.close()
new_file.close()

