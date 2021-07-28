#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/11 0011 11:06
# @Author  : mazhiqiang
# @Site    : 
# @File    : day3.py
# @Software: PyCharm
# def func1():
#     sum = 1 + 2
#     print(sum)
#     return sum
#
#
# func1()
# print(func1())
# def func2(a, b):
#     sum = a + b
#     print(sum)
#     return sum
#
#
# func2(10, 20)
# print('返回值', func2(10, 20))
# def printlines():
#     """
#     打印一条横线
#     :return:
#     """
#     return ('-'*20)
#
# def num1(a):
#     """
#     控制打印多少条横线
#     :param a:需要int类型
#     :return:
#     """
#     for i in range(a):
#         print(printlines())
# num1(4)

# 返回多个参数
# def num2():
#     return 1, 2
# print(num2())
# def num3():
#     return [1, 2]
# print(num3())
# def num3():
#     return {1, 2}
# print(num3())
# def num4(a):
#     if a == True:
#         return [1, 2]
#     else:
#         return '222'
# print(num4(False))
# def user(name, age, sex, class1='三班'):
#     '''
#     位置传参，要注意顺序
#     :param name: 名字
#     :param age: 年龄
#     :param sex:性别
#     :return:
#     '''
#     print(f'你的名字是{name}，年龄是{age}，性别是{sex}，班级是{class1}')
#
#
# user('xiaoming', 20, '男')
# # 关键字传参
# user('xiaohuang', sex='女', age=18)
# # 默认传参
# user('xiaohuang', 20, '男', '一班')
# user('xiaohuang', sex='女', age=18, class1=2)

# 不定长传参
# list1 = ['xiaohuang', '女', 18]
#
# def user(*args):
#     name = args[0]
#     age = args[1]
#     sex = args[2]
#     class1 = args[3]
#     print(f'你的名字是{name}，年龄是{age}，性别是{sex}，班级是{class1}')
#     return f'你的名字是{name}，年龄是{age}，性别是{sex}，班级是{class1}'
# print(user(*list1,22))

# 不定长+关键字
# dict1 = {'name': 'xiaohuang', 'sex': '女', 'age': 18, 'class1': 6}
#
#
# def user1(**kwargs):
#     name = kwargs['name']
#     age = kwargs['sex']
#     sex = kwargs['age']
#     class1 = kwargs['class1']
#     print(f'你的名字是{name}，年龄是{age}，性别是{sex}，班级是{class1}')
#     return f'你的名字是{name}，年龄是{age}，性别是{sex}，班级是{class1}'
#
#
# print(user1(**dict1))
# print(user1(name='小红', sex='女', age=20, class1=6))
# 拆包
# def func1():
#     return 100,200
# g,h = func1()
# print(g,h)
# dict1 = {'name': 'xiaohuang', 'sex': '女'}
# a, b = dict1.keys()
# c, d = dict1.values()
# e, f = dict1.items()
# print(a, b, '\n', c, d, '\n', e, f)

def func2(a):
    print(a)
    print(id(a))
    a = a+ a
    print(a)
    print(id(a))


func2(2)
func2([1, 2, 3])
func2(1)
