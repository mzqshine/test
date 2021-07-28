#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/27 0018 22:00
# @Author  : mazhiqiang
# @Site    : 
# @File    : test.py
# @Software: PyCharm
# 1.python的数据类型都有哪些(5分)
#基本数据类型 number(int,float,bool) string,list,tuple,dict,set
#     整型：int
# 浮点型：float
# 字符串：str
# 布尔型：bool
# 元组：tuple
# 集合：set
# 字典：dict
# 2.列表，元组、字典、集合如何定义，列出实例（5分）
'''
列表  [1,2,3]
元组  （1，2，3）
字典  {’name‘：’xiaom‘，’age‘：’18‘，}
集合 {1，2，3}
'''
# 有一堆字符串，“welocme to super&Test”，打印出emcolew ot  tseT&repus……全部单词原位置反转，不能使用索引倒序输出或者通过其他现有函数实现（15分）
m ='welocme to super&Test'
n = []
b = ''
for i in m:
    n.append(i)
for i in range(len(n)):
    a = n.pop()
    b = b+''.join(a)
print(b)


# 9.python可变数据类型和不可变数据类型都有哪些（5分）
# 可变  列表 字典 集合
# 不可变  数字，元组、字符串
# 10.递归实现斐波那契数列（10分）
list1 = []
def sum2(m):
    '''
    计算累加和
    :param n:
    :return:
    '''
    if m < 2:
        return 1
    else:
        return sum2(m-1)+sum2(m-2)
for i in range(10):
    list1.append(sum2(i))
print(list1)

#基本数据类型 number(int,float,bool) string,list,tuple,dict,set
#     整型：int
# 浮点型：float
# 字符串：str
# 布尔型：bool
# 元组：tuple
# 集合：set
# 字典：dict
# 2.列表，元组、字典、集合如何定义，列出实例（5分）
'''
列表  [1,2,3]
元组  （1，2，3）
字典  {’name‘：’xiaom‘，’age‘：’18‘，}
集合 {1，2，3}
'''
# 有一堆字符串，“welocme to super&Test”，打印出emcolew ot  tseT&repus……全部单词原位置反转，不能使用索引倒序输出或者通过其他现有函数实现（15分）
m ='welocme to super&Test'
n = []
b = ''
for i in m:
    n.append(i)
for i in range(len(n)):
    a = n.pop()
    b = b+''.join(a)
print(b)


# 9.python可变数据类型和不可变数据类型都有哪些（5分）
# 可变  列表 字典 集合
# 不可变  数字，元组、字符串
# 10.递归实现斐波那契数列（10分）
list1 = []
def sum2(m):
    '''
    计算累加和
    :param n:
    :return:
    '''
    if m < 2:
        return 1
    else:
        return sum2(m-1)+sum2(m-2)
for i in range(10):
    list1.append(sum2(i))
print(list1)



print(int(1.567*100)/100)
