#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

name = input('请输入姓名\n')
print('hello',name)

number = 100
if number > 100:
	print(number,'大于一百')
else:
	print(number,'小于等于一百')

print('\\')
print('\\\t\\')	
print('\\\n\\')
print(r'\\\t\\')
print('hello\nworld')
print('''hello
world
cao
nima''')

age = 18
if age > 20:
	print('age>20')
elif age > 18:
	print('18<age<=20')
elif age > 10:
	print('10<age<=18')
else:
	print('age<=10')

age = input('请输入年龄：')
age = int(age)
if age < 2000:
	print('00前')
else:
	print('00后')

# 练习：小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖
height = 1.75
weight = 80.5
BMI = weight/(height*height)
if BMI > 32:
	print('严重肥胖')
elif BMI > 28:
	print('肥胖')
elif BMI > 25:
	print('过重')
elif BMI > 18.5:
	print('正常')
else:
	print('过轻')

name = [1,2,3,4]
sum = 0
for item in name:
	sum = sum + item
print(sum)

sum = 0
for item in range(101):
	sum = sum + item
print(sum)

sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print(sum)