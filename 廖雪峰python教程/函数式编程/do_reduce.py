# -*- coding: utf-8 -*-
#字符串转成浮点型
from functools import reduce

CHAR_TO_FLOAT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':-1}

def char2num(s):
     return CHAR_TO_FLOAT[s]

def str2float(s):
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float,map(lambda x:CHAR_TO_FLOAT[x],s),0.0) #0.0是初始值 → str2float(".1234")
    #return reduce(to_float, map(char2num,s)) reduce(to_float, [1,2,3,-1,4])

def test():
     assert str2float("0") == 0
     assert str2float("123.456") == 123.456
     assert str2float("123.456000") == 123.456000
     assert str2float("0.1234") - 0.1234 < 0.00001
     assert str2float(".1234") - 0.1234 < 0.00001
     assert str2float("120.0034") == 120.0034

if __name__ == "__main__":
     test()
