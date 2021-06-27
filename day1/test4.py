#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/6/27 16:18
# @Author : 马志强
# @Site : 
# @File : test4.py
# @Software: PyCharm
# a = 'hello'
# b = "world"
# print(a,b)
# str1 = "I'm tom"
# str2 = '''123
# 234'''
# str3 = 'I\'m tom'
# print(str1,str2,str3)
# #注意下标从0开始
# str1 = 'abcdef'
# print(str1)
# print(str1[0])

#切片
# name = 'abcdefg'
# #起始下标：截止下标：步长   步长为负数倒着取
# print(name[2:5:1])
# print(name[2:5])
# print(name[:5])
# print(name[1:])
# print(name[:])
# print(name[::2])
# print(name[::-1])
# print(name[-4:-1])
# print(name[6:0:-1])
# print(name[-1:-5:-1])
# print(name[-2:-5:-2])
#查找
#find 查找的字符串，下标起始，下标结束  从左侧开始
# mystr = "hello world and superctest and chaoge and Python"
# print(mystr.find('and'))
# print(mystr.find('and',15,30))
# print(mystr.find('ands',15,60))  #查不到报-1
# print('---------------')
# print(mystr.index('and'))
# print(mystr.index('and',15,30))
# #(mystr.index('ands',15,30))  #查不到报错
# #下边两个为从右往左
# print('---------------')
# print(mystr.rfind('and')) #返回的是子串开始的下标
# print(mystr.rfind('and',15,30))
# print(mystr.rfind('ands',15,30))  #查不到报-1
# print('---------------')
# print(mystr.rindex('and'))
# print(mystr.rindex('and',15,30))
# #print(mystr.rindex('ands',15,30))  #查不到报错
#
# #统计出现次数
# print('---------------')
# print(mystr.count('and'))
# print(mystr.count('and',15,30))
# print(mystr.count('ands'))
#
#replace替换
# #默认改所有
# mystr = "hello world and superctest and chaoge and Python"
# print(mystr)
# print(mystr.replace('and','he'))
# mystr_new = mystr.replace('and','he')
# print(mystr_new)
# print(mystr.replace('and','he',2))  #替换两个

# #split（）分割默认切所有
# mystr = "hello world and superctest and chaoge and Python"
# print(mystr.split(' '))
# print(mystr.split(' and'))
# print(mystr.split(' and',2))  #切割次数
#
#join组合序列
# list1 = ['a','b','c']
# list2 = ['e','f','g']
# a='111'
# print('_'.join(list1))
# print('...'.join(list1))
# print(a.join(list1))
#capitalize 把首字母改为大写
# mystr = "hello world and superctest and chaoge and Python"
# print(mystr.capitalize())
# #所有单词首字母大写
# print(mystr.title())
# #小写变大写
# print(mystr.upper())
# #大写变小写
# print(mystr.lower())
# #strip删除空格
# mystr = "        hello world and superctest and chaoge and Python      "
# print(mystr.strip())
# print(mystr.lstrip())
# print(mystr.rstrip())
#
# #填充字符
# mystr = "hello world and superctest and chaoge and Python"
# str1 = 'hello'
# print(str1.center(30,'.'))
# print(str1.ljust(30,'.'))
# print(str1.rjust(30,'.'))
#判断子串是否在里，判断真假  设置下标在指定范围查找
# mystr = "hello world and superctest and chaoge and Python"
# print(mystr.startswith('hello',3,19))
# print(mystr.endswith('n'))
# #isalpha()判断至少有一个字符且所有字符都是字母，则为turn
# mystr = "hello world and superctest and chaoge and Python"
# mystr1 = 'hello'
# mystr2 = 'hello123'
# print(mystr1.isalpha())
# print(mystr2.isalpha())
# #isdigit()：如果字符串串只包含数字则返回 True 否则返回 False。
# mystr1 = '123'
# mystr2 = 'hello123'
# print(mystr1.isdigit())
# print(mystr2.isdigit())
# #isalnum()：如果字符串串⾄至少有⼀一个字符并且所有字符都是字⺟母或数字则返 回 True,否则返回False。
# mystr1 = '123 '
# mystr2 = 'hello123'
# print(mystr1.isalnum())
# print(mystr2.isalnum())
# #isspace()：如果字符串串中只包含空⽩白，则返回 True，否则返回 False。
# mystr1 = '1 2 3 '
# mystr2 = '   '
# print(mystr1.isspace())
# print(mystr2.isspace())






