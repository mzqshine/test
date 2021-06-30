#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/6/28 20:26
# @Author : 马志强
# @Site : 
# @File : day1——end.py
# @Software: PyCharm

# 石头剪刀布
import random

n = 1
while n == 1:
    me = random.randint(0, 2)
    you = int(input('请输入你的选择0拳头1剪刀2布：'))
    if you == 0:
        if me == 0:
            print(f'我是{me}')
            print('打平')
        if me == 1:
            print(f'我是{me}')
            print('你赢啦')
            break  # 或者n=2
        if me == 2:
            print(f'我是{me}')
            print('你输了')
    if you == 1:
        if me == 0:
            print(f'我是{me}')
            print('你输了')
        if me == 1:
            print(f'我是{me}')
            print('打平')
        if me == 2:
            print(f'我是{me}')
            print('你赢啦')
            break  # 或者n=2
    if you == 2:
        if me == 0:
            print(f'我是{me}')
            print('你赢啦')
            break  # 或者n=2
        if me == 1:
            print(f'我是{me}')
            print('你输了')
        if me == 2:
            print(f'我是{me}')
            print('打平')

# 三角形
for i in range(5):
    for j in range(0, i):
        print("*", end=" ")
    print("")

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j}={i * j}', end=' ')
    print('')

# 三角形的不同样子
print("----------右对齐正三角-------")
for i in range(5):
    for j in range(0, 4 - i):
        print(" ", end=" ")
    for j in range(0, i):
        print("*", end=" ")
    print("")

print("----------右对齐倒三角----------")
for i in range(5):
    for j in range(0, i):
        print(" ", end=" ")
    for j in range(0, 4 - i):
        print("*", end=" ")
    print(" ")

print("---------正三角-------------")
for i in range(5):
    for j in range(0, 5 - i):
        print(end=" ")
    for k in range(5 - i, 5):
        print("*", end=" ")
    print("")
