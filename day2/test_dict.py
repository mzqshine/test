#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 0004 14:05
# @Author  : mazhiqiang
# @Site    : 
# @File    : test_dict.py
# @Software: PyCharm

# 空字典
# dict2 ={}
# dict3 = dict()
# print(dict2,dict3)
# dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# dict1['name'] = 'xiaoming'
# print(dict1)
# dict1['shengao'] = '180'
# print(dict1)
# del dict1['shengao']
# print(dict1)
# print(type(dict1))
# dict1.clear()
# print(dict1)
dict1 = {'name': 'Tom', 'age': [20, 30], 'gender': '男'}
print(dict1['age'][1])
print(dict1.get('age'))
# 默认值
print(dict1.get('age1'))
print(dict1.get('age1', '40'))

print(dict1.keys())
print(dict1.values())
print(dict1.items())
for i in dict1.keys():
    print(i)
for i in dict1.values():
    print(i)
for i in dict1.items():
    print(i)
for i, j in dict1.items():
    print(i, j)
# 默认遍历keys
for i in dict1:
    print(i)
