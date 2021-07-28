# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2021/7/11 0011 16:56
# # @Author  : mazhiqiang
# # @Site    :
# # @File    : test_digui.py
# # @Software: PyCharm
# # def sum1(n):
# #     '''
# #     计算累加和
# #     :param n:
# #     :return:
# #     '''
# #     print(n)
# #     if n ==1:
# #         return 1
# #     return n+sum1(n-1)
# # print(sum1(3))
#
def sum2(m):
    '''
    计算累加和
    :param n:
    :return:
    '''
    if m == 10:
        return 10
    return m+sum2(m+1)
print(sum2(5))
# # print('1+(2+(3+4)))')
# # import os
# # os.listdir('E:\\tools-xuexi\\test_ck')
# # list1=[]
# # def dir():
# #     if 'file' in os.getcwd():
# #         return 'day3'
# #     return list1.append(dir())
# # 列表每个数据都进行一种计算
# list1 = [1, 2, 3, 4, 5]
#
#
# def func1(a):
#     return a ** 2
#
#
# result = map(func1, list1)
# print(result)
# print(list(result))
# # 列表累计计算
# import functools
#
# list2 = [1, 2, 3, 4, 5]
#
#
# def func2(a, b):
#     return a + b
#
#
# result2 = functools.reduce(func2, list2)
# print(result2)
# # 过滤
# list3 = [1, 2, 3, 4, 5]
#
#
# def func3(a):
#     return a % 2 == 0
#
#
# result3 = filter(func3, list3)
# print(list(result3))
