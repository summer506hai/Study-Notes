# -*- coding: utf-8 -*-
'''
请使用迭代查找一个list中最小和最大值，并返回一个tuple
'''
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    min_value = max_value = L[0]
    for i, j in enumerate(L):
        if L[i] < min_value:
            min_value = L[i]
        if L[i] > max_value:
            max_value = L[i]
    return (min_value, max_value)

# 测试
def test():
    assert findMinAndMax([]) == (None, None)
    assert findMinAndMax([7]) == (7, 7)
    assert findMinAndMax([7,1]) == (1, 7)
    assert findMinAndMax([7, 1, 3, 9, 5]) == (1, 9)
    print("测试通过！")

if __name__ == "__main__":
    test()
