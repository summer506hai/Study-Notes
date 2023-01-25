# -*- coding:utf-8 -*-
'''
检查特定字符串是否存在在原字符串中
'''
txt = ['lambda function are anonymous function.','functions are objects in python.']

#map + lambda方法
mark = map(lambda s:(True,s) if 'anonymous' in s else (False,s),txt)
print(list(mark))

#用列表解析的方式
mark = [(True,x) if 'anonymous' in x else (False,x) for x in txt]
print(mark)