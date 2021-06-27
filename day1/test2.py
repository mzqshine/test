#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/6/27 11:29
# @Author : 马志强
# @Site : 
# @File : test2.py
# @Software: PyCharm
#功能描述书：输入
from math import e
#
# passwd = input('你的密码是:\t') #输入值并赋给变量
# print(passwd)
# print(type(passwd))
# ##数据类型转化
# phone = input('你的手机号是:\n')  #输入值并赋给变量
# print(phone)
# print(type(phone))
# print(int(phone))  #转换成整形
# print(float(phone)) #转换成浮点
# print(str(phone)) #转换成浮点

#转换成列表
list1 = (1,2,3)
print(list1)
print(list(list1))
#转换成元组
list2 = [1,2,3]
print(list2)
print(tuple(list2))

#数据类型转化(智能转换)
phone = input('你的手机号是:\n')  #输入值并赋给变量
print(phone)
print(type(phone))
print(type(eval(phone)))
print(eval(phone))