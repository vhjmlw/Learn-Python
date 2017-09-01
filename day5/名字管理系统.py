# -*- coding:utf-8 -*-


print('新增姓名输入1')
print('删除姓名输入2')
print('修改姓名输入3')
print('查询姓名输入4')
print('查询全部输入5')
print('退出系统输入6')

name_list = []

while True:
    num = int(input('请输入操作序号：'))
    if num == 1:
        new_name = input('请输入姓名。。。')
        if new_name not in name_list:
            name_list.append(new_name)
    elif num == 2:
        del_name = input('请输入要删除的姓名。。。')
        if del_name in name_list:
            name_list.remove(del_name)
        else:
            print('姓名在列表中不存在。。。')
    elif num == 3:
        modify_name = input('请输入要修改的姓名。。。')
        name = input('请输入修改后的姓名。。。')
        if modify_name in name_list:
            index =  name_list.index(modify_name)
            name_list[index] = name
        else:
            print('姓名在列表中不存在')
    elif num == 4:
        search_name = input('请输入要查询的显卡。。。')
        if search_name in name_list:
            print('查有此人')
        else:
            print('查无此人')
    elif num == 5:
        for x in name_list:
            print(x)
    elif num == 6:
        break
