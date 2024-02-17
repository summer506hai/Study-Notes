# -*- coding: utf-8 -*-
'''
在 Python 中，装饰器是一种函数，用来修改其他函数的行为。装饰器函数接受一个函数作为输入，并返回一个新的函数。但是，在返回的新函数中，
通常会修改原始函数的行为或者增加一些额外的功能。
使用 @functools.wraps(func) 装饰器可以解决一个常见的问题：在使用装饰器装饰函数时，被装饰函数的元数据会丢失，
即原始函数的一些属性（如 __name__、__doc__ 等）会被装饰器函数的属性所取代，这可能会导致一些意外的行为，特别是在调试和文档生成等情况下。
请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
'''
import time, functools

def metric(fn):  #装饰器
    @functools.wraps(fn)
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = fn(*args,**kwargs)
        print('*args is %s, **kwargs is %s' % (args,kwargs))
        end_time = time.time()
        print('%s excute in %s ms' % (fn.__name__,end_time-start_time))
        return res
    return wrapper

@metric
def fast(x,y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x,y,z):
    time.sleep(0.1234)
    return x*y*z

def test():
    assert fast(11,22) == 33
    assert slow(11,22,33) == 7986
    print("测试通过！")

if __name__ == "__main__":
    test()
