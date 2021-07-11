#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 0004 12:17
# @Author  : mazhiqiang
# @Site    : 
# @File    : day2_end.py
# @Software: PyCharm
import random

# 可直接全部运行
# 1\需求：有三个办公室，8位⽼师，8位⽼师随机分配到3个办公室
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [[], [], []]
for i in list1:
    j = random.randint(0, 2)
    list2[j].append(i)
print(list2)
# 2、求100以内能被3整除的数，并将作为列表输出
list2_1 = []
for i in range(1, 101):
    if i % 3 == 0:
        list2_1.append(i)
print(list2_1)

# 3、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表  #不允许用强制类型转化
list3_1 = [1, 2, 3, 4, 3, 4, 2, 5, 5, 8, 9, 7]
for i in list3_1:
    if list3_1.count(i) > 1:  # 统计大于1的
        list3_1[list3_1.index(i)] = '-'  # 大于1的列表数据替换
for i in list3_1:
    if '-' in list3_1:
        list3_1.remove('-')
print(list3_1)
# 4、求斐波那契数列 1 1 2 3 5 8 13 ……
# 方式一
m = 1
list4_1 = []
list4_1.append(m)
list4_1.append(m)
for m in range(1, 20):
    list4_1.append(list4_1[-1] + list4_1[-2])
print(list4_1)
# 方式二
m = 1
n = 1
sum1 = 0
list4_1 = [1, 1]
for i in range(1, 20):
    sum1 = m + n
    list4_1.append(sum1)
    n = m
    m = sum1
print(list4_1)

# 5、求100以内的质数（只能被1和它本身整除）
m = []
for i in range(1, 100):
    for j in range(2, i + 1):
        if i % j == 0:
            if i == j:
                m.append(i)
            else:
                break
print(m)

# 6、有一堆字符串“aabbbcddef”打印出不重复的字符串结果：cef
list6_1 = 'aabbbcddef'
for i in range(len(list6_1)):
    if list6_1.count(list6_1[i]) == 1:
        print(list6_1[i], end='')
# 7、有一堆字符串，“welocme to super&Test”，打印出superTest，不能查字符的索引
print('\n-------')
list7_1 = 'welocme to super&Test'
list7_1 = list7_1.split(' ')
list7_1 = list7_1[2].split('&')
print(''.join(list7_1))
# 8、有一堆字符串，“welocme to super&Test”，打印出tseT&repus ot ……全部单词原位置反转  #不允许用reverse
list8_1 = 'welocme to super&Test'
list8_2 = ''
for i in range(len(list8_1)):
    list8_2 = list8_2 + ''.join(list8_1[-(i + 1)])
print(list8_2)

# 9、有一堆字符串，“abcdef”，将收尾反转，结果：fedcba，不能使用现有的函数或方法，自己写算法实现
m = 'abcdef'
n = ''
for i in range(len(m)):
    for j in range(len(m) - i):
        if j == len(m) - i - 1:
            n = n + ''.join(m[j])
print(n)

# 10、有一堆字符串，“aabbbcddef”，输出abcdef # 不允许用set
m = 'aabbbcddef'
n = ''
for i in range(len(m)):
    if m.count(m[i]) > 1:
        if m[i] not in n:
            n = n + ''.join(m[i])
    else:
        n = n + ''.join(m[i])
print(n)
