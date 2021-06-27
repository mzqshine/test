#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/6/27 15:18
# @Author : 马志强
# @Site : 
# @File : test3.py
# @Software: PyCharm
#运算符
# n = 1
# m = 2
# print(n+m)
# print(n-m)
# print(n*m)
# print(n/m)
# print(n//m)
# print(m*3%(n+4))
# print(m**m)
# print((n-m)+n)
#
# #赋值运算
# print('----赋值运算-------')
# a = 1
# print(a)
# a = b = 2
# print(a,b)
# a,b,c = 1,2,4
# print(a,b,c)
#
# #复合赋值运算
# print('复合赋值运算')
# print('---------------')
# a=1
# a += 1
# print(a)
# print('---------------')
# a -= 1
# print(a)
# print('---------------')
# a=1
# a *= 1
# print(a)
# print('---------------')
# a=1
# a /= 1
# print(a)   #除法之后就是自动转换浮点类型
# print('---------------')
# a=1
# a //= 1
# print(a)
# print('---------------')
# a=1
# a %= 1
# print(a)
# print('---------------')
# a = 2
# a **= 2
# print(a)
# #控制小数点位数
# n =1.23456
# m = round(n,2)
# print(m)
#
# c = 3
# c += 1+2 #先计算1+2
# print(c)

#比较运算符  主要为bool值
a = 8
b = 7
print( a == b)
print( a != b)
print( a >= b)
print( a <= b)
print( a > b)
print( a < b)
#逻辑运算符
print('---------------')
a = 1
b = 2
c = 3
print((a < b) and (b > c))
print((a < b) or (b > c))
n = True
print(not n)
#0默认为false

