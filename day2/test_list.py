#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 0004 10:52
# @Author  : mazhiqiang
# @Site    : 
# @File    : test_list.py
# @Software: PyCharm
# 列表操作
# 下标
name_list = ['Tom', 'Lily', 'Rose', 'Tom']
# print(name_list[0])
# print(name_list[1])
# # 查找
# print(name_list.index('Rose', 1, 3))
# # 统计
# print(name_list.count('Tom'))
# print(name_list.count('Tom'))
# # 列表数据个数
# print(len(name_list))
# # 查找判断bool
# print('tom' in name_list)
# print('Rose' in name_list)
# # 练习
# my_list = input('请输入需要查找的字符串：')
# if my_list in name_list:
#     print('你查找的数据在这里')
#     print('你的数据：%s', my_list)
#     print('列表数据%s', name_list)
# else:
#     print('请重新输入')

# # 追加
# name_list.append('xiaom')
# print(name_list)
# # 连续追加
# name_list.extend('abc')
# print(name_list)
# name_list.extend(['abc', 'efd'])
# print(name_list)
# # 插入
# name_list.insert(2, 'wo')
# print(name_list)
# # 删除
# del name_list[1]
# print(name_list)
# # 移除
# name_list.remove('wo')
# print(name_list)
# # 删除指定（默认尾数）
# name_list.pop(2)
# print(name_list)
# name_list.pop()
# print(name_list)
# # 清空列表
# name_list.clear()
# print(name_list)
# # 删除列表
# del name_list


# 修改
# 赋值
list1 = [5, 6, 7, 8, 1, 2, 3, 5, 6, 7, 8]
list2 = [5, 6, 7, 8]

# 逆置
print(reversed(list1))
list1.reverse()
print(list1)
# 排序 默认升序
list1.sort()
print(list1)
# 倒序
list1.sort(reverse=True)
print(list1)
# 不改变原有列表
list2 = sorted(list1)
print(list1, list2)
#复制
list3 = list1.copy()
print(list3)
