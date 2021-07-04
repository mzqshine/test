#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 0004 14:05
# @Author  : mazhiqiang
# @Site    : 
# @File    : test_dict.py
# @Software: PyCharm

#空字典
dict2 ={}
dict3 = dict()
print(dict2,dict3)
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
dict1['name'] = 'xiaoming'
print(dict1)
dict1['shengao'] = '180'
print(dict1)
del dict1['shengao']
print(dict1)
dict1.clear()
print(dict1)
