#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 0004 15:50
# @Author  : mazhiqiang
# @Site    : 
# @File    : 公共操作.py
# @Software: PyCharm
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list2 + list1
# print(list3)
# print(len(list3))
# del list3[0]
# print(list3)
# print(max(list3))
# print(min(list3))
# for i in range(10):
#     print(i)
# for i in range(1,10,2):
#     print(i)
# data = range(10)
# print(list(data))

# for i in enumerate(list3):
#     print(i)
# for i,j in enumerate(list3):
#     print(i, j)
# 枚举 临时变更下标
# print(list3)
# for i, j in enumerate(list3, start=2):
#     print(i, j)
# print(list3[1])

tup = (10, 20, 30)
print(max(tup))
print(min(tup))
for i, j in enumerate(tup, start=2):
    print(i, j)

dic = {'age': [10, 20, 30]}
print(max(dic['age']))
