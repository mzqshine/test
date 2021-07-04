#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 0004 14:59
# @Author  : mazhiqiang
# @Site    : 
# @File    : test_set.py
# @Software: PyCharm
set1 = {}
print(type(set1))
set2 = set()
print(set2)
# 无下标，无顺序,默认去重
set3 = {10, 20, 30, 40, 50, 60, 10}
print(set3)
set3.add(100)
print(set3)
print(len(set3))
list1 = [2, 3, 2]
# 只能追加序列
set3.update(list1)
print(set3)
set3.update('list1')
print(set3)
# 删除指定数据，没有就报错
set3.remove(2)
print(set3)
# 删除指定数据，没有数据不会报错
set3.discard(2)
print(set3)
# 随机删除并返回这个数据
print(set3.pop())
print(set3)
# bool判断存在
print(10 in set3)
print(200 in set3)
print(200 not in set3)
