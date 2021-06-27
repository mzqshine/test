# '''
# 编写时间：2021-06-27
# 编写者：马志强
# 功能描述：第一天
# '''
# # #注释
# # #打印helloworld
# # print('helloworld')
# #
# # # 变量  --简单断点
# # his_name = '小明'
# # print(his_name)
# # print(his1name)
#
# #数据类型
# m=123
# print(type(m))
# m = 0.123
# n = 'sad'
# print(type(m))
# print(type(n))
# print(type(True))
# b = (1,2)
# v = {1,2}
# c = {'s':1,'b':2}
# print(type(b))
# print(type(v))
# print(type(c))

# 格式化输出   ctrl+alt+l 可以对代码进行格式调整
his_name = '小飞'
age = 18
weight = 50.12
num = 1
print('我的名字是：%s' % his_name)  # 字符串
print('我的年龄是：%d' % age)  # 整形
print('我的体重是：%f' % weight)  # 浮点，默认小数点后6位
print('我的学号是：%05d' % num)  # 必须0开始，5代表总长度
print('我的年龄是：%.2f' % weight)  # 。2代表小数点位数
print('我的名字是：%s,我的年龄是：%d,我的体重是：%f' % (his_name, age, weight))  # 整合
print('我的名字是：%s,我的年龄是：%d,我的明天体重是：%.3f' % (his_name, age, weight - 1))  # 打印加减函数
print(f'我的名字是：{his_name},我的年龄是：{age},我的明天体重是：{weight}')  # 3.7版本上有f参数使用
print('shjdkahdjka\nshd\tadjk\n\tsdhka')  # 转义换行符  \n换行 \t非行开头空格1个字符  \t行开头是tab 4个字符
print('结束', end='-------')  # 结束标识
