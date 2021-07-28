#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 0012 20:45
# @Author  : mazhiqiang
# @Site    : 
# @File    : day3_end.py
# @Software: PyCharm
# 1.使用列表推导式生成能被5整除的数（100以内）
list1 = [i for i in range(101) if i % 5 == 0]
print(list1)
# 2.有两个列表，一个是学生姓名，一个是学生的年龄，生成一个字典，key为姓名，value为年龄
names = ['小明', '小红', '小蓝']
ages = [12, 18, 20]
dic1 = {names[i]: ages[i] for i in range(len(names))}
print(dic1)


# 3.开发一个注册系统，
# 页面：
# [{name:xxx,age:xxx},xxx]
# ----------------
# *   1-新增用户
# *   2-查询用户
# *   3-删除用户
# ----------------
# 功能1：新增学生信息（姓名和年龄）通过键盘，如果学生已经存在提示用户已存在
# 功能2：查询学生信息
# 功能3：删除学生信息

def add_user():
    '''
    添加学生信息
    :param name:
    :param age:
    :return:
    '''
    name = input('请输入要添加的学生姓名')
    age = input('请输入要添加的学生年龄')
    for i in users:
        if name == i["name"]:
            print('用户已存在')

    dic2['name'] = name
    dic2['age'] = age
    users.append(dic2)
    print('新增成功')


def users1():
    '''
    查询学生信息
    :param name:
    :return:
    '''
    name = input('请输入要查询的学生姓名')
    for i in users:
        if name == i["name"]:
            print(i)
        else:
            print('信息不存在')
    if users == []:
        print('信息表已空')


def del_user():
    '''
    删除学生信息
    :param name:
    :return:
    '''
    name = input('请输入要删除的学生姓名')
    for i in users:
        if name == i["name"]:
            users.remove(i)
            print('信息已删除')
        else:
            print('信息不存在')
    if users == []:
        print('信息表已空')


def shouye():
    print('-' * 20)
    print('1-新增用户')
    print('2-查询用户')
    print('3-删除用户')
    print('-' * 20)


users = []
dic2 = {}
num = 0
while num >= 0:
    shouye()
    num = int(input('请输入您需要的功能的序号：'))
    if num == 1:
        add_user()
    elif num == 2:
        users1()
    elif num == 3:
        del_user()
    else:
        print('输入错误，系统退出')
        break
