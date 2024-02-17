# -*- coding: utf-8 -*-
'''
转成小写
'''
L1 = ['Hello', 'World', 18, 'Apple', None]

#使用列表生成式
L2 = [s.lower() for s in L1 if isinstance(s, str)]
assert L2 == ['hello', 'world', 'apple']
print("测试通过！")

#使用map/filter
def is_str(s):
    return isinstance(s, str)

def lower(s):
    return s.lower()

#L2 = list(map(lower,list(filter(is_str,L1))))
L2 = list(map(lambda y:y.lower(),filter(lambda x:isinstance(x, str) ,L1)))   #使用匿名函数lambda
assert L2 == ['hello', 'world', 'apple']
print("测试通过！")
