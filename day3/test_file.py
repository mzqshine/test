#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/11 0011 15:42
# @Author  : mazhiqiang
# @Site    : 
# @File    : test_file.py
# @Software: PyCharm
# f = open('text.txt', 'w')
# f.write('hello')
# f.close()
# f = open('text.txt', 'a+')
# f.write('nihao')
# # f.close()
# f = open('text.txt', 'r+', encoding='utf-8')
# # print(f.read(10))
# # print(f.readlines(2))
# print(f.readlines())
# f.seek(5, 0)
# # tell是获取光标位置
# print(f.tell())
# print(f.read(10))
# f.seek(0, 1)
# print(f.tell())
# f.seek(0, 2)
# print(f.tell())
#
# f.close()
# f = open('text.txt', 'r+', encoding='utf-8')
# print(f.read())
# f.close()
import os
# os.rename('test_new.txt','test_new.txt')
# os.remove('test_new.txt')
#os.mkdir('test')
#os.rmdir('test')
os.getcwd()
print(os.getcwd())
#os.chdir('E:\\tools-xuexi\\test_ck')

# os.listdir
print(os.listdir('E:\\tools-xuexi\\test_ck\day3'))