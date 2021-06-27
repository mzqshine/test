#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/6/27 18:20
# @Author : 马志强
# @Site : 
# @File : test5.py
# @Software: PyCharm
# age = input('请输入你的年龄')
# #age = int(age)
# if int(age) >= 18:
#     print('上网')
# print('回家')
# 年龄
# age = int(input('请输入你的年龄'))
# #age = int(age)
# if age >= 18:
#     if age >= 60:
#         if age >= 140:
#             print('输入错误')
#         print('退休')
#     print('搬砖')
# else:
#     print('童工')
# age = int(input('请输入你的年龄'))
# # age = int(age)
# if 0 < age < 18:
#     print('童工')
# elif 18 <= age < 60:
#     print('搬砖')
# elif 60 <= age <= 140:
#     print('退休')
# else:
#     print('输入错误')
# # 公交
# mon = int(input('余额'))
# if mon > 0:
#     print('上车')
#     seat = int(input('是否有座'))
#     if seat > 0:
#         print('坐着回家')
#     else:
#         print('站着回家')
# else:
#     print('走着回家')
#
# import random
# #猜拳  0拳头  1剪刀   2布
# you = int(input('请出拳'))
# me = random.randint(0,2)
# if


# 循环
# n= 0
# while n<5:
#     print('666')
#     n+=1
# print('够了')
# n = 0
# sum = 0
# while n <= 100:
#     # sum = sum + n
#     sum += n
#     n += 1
# print(sum)
# # 偶数累加和
# n = 0
# sum = 0
# while n <= 100:
#     # sum = sum + n
#     if n % 2 == 0:
#         sum += n
#     n += 1
# print(sum)

#breake和continue的用法
i =1
while i<5:
    if i ==3:
        print('这个有毒')
        i+=1
        continue
    print(f'吃了第{i}个')
    i+=1
i =1
while i<5:
    if i ==3:
        print('吃饱了')

        break
    print(f'吃了{i}个')
    i+=1
