#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 0004 13:36
# @Author  : mazhiqiang
# @Site    : 
# @File    : test_tuple.py
# @Software: PyCharm
# tup = (1, 2, 3, 'a')
# print(tup)
# print(type(tup))
# # 注意逗号
# tup2 = (1,)
# tup3 = (1)
# print(tup2)
# print(type(tup2))
# print(tup3)
# print(type(tup3))
# # 查找
# print(tup.index(2))
# # 统计
# print(tup.count(2))
# #长度
# print(len(tup))
# #可改里面的列表数据  注意列表数据
tup = (1, 2, 3, ['bb'])
print(tup[3])
tup[3][0] = 'aa'
print(tup)
tup[3].append('trt')
print(tup)
