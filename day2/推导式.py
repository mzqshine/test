#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 0004 16:32
# @Author  : mazhiqiang
# @Site    : 
# @File    : 推导式.py
# @Software: PyCharm
# list1 = []
# n = 0
# while n<=10:
#     list1.append(n)
#     n+=1
# print(list1)
# list2 = []
# for i in range(11):
#     list2.append(i)
# print(list2)
#
# list3 = [i for i in range(11)]
# # print(list3)
# list3 = [i for i in range(11) if i%2 == 0]
# print(list3)
# # 组合形式
# list1 = []
# for i in range(3):
#     for j in range(3):
#         list1.append((i, j))
# print(list1)
# # 推导式
# print([(i, j) for i in range(3) for j in range(3)])
# 创建⼀个字典：字典key是1-5数字，value是这个数字的2次⽅
dic = {i: i ** 2 for i in range(5)}
# 两个列表组成字典
print(dic)
list1 = ['name', 'age', 'gender', 'xiaoming']
list2 = ['Tom', 20, 'man', 20]
dic1 = {list1[i]: list2[i] for i in range(4)}
print(dic1)
# 取字典中值最大的
dic2 = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
dic3 = {key: value for key, value in dic2.items() if value > 200}
print(dic3)
dic3 = {key: value for key, value in dic2.items() if key == 'HP'}
print(dic3)

list4 = [1, 1, 2]
set2 = {i ** 2 for i in range(1, 3)}
print(set2)

