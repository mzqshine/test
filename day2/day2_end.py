#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 0004 12:17
# @Author  : mazhiqiang
# @Site    : 
# @File    : day2_end.py
# @Software: PyCharm
import random

# 随机分配老师
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [[], [], []]
for i in list1:
    j = random.randint(0, 2)
    list2[j].append(i)
print(list2)
