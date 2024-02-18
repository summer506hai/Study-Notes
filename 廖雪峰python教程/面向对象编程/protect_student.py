# -*- coding: utf-8 -*-
'''
请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性
'''
class Student(object):
    def __init__(self, name,score, gender):
        self.__name = name
        self.__score = score
        self.__gender = gender

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_score(self):
        return self.__score

    def set_gender(self, gender):
        if gender in ["male","female"]:
            self.__gender = gender
        else:
            raise ValueError('bad gender')
    def get_gender(self):
        return self.__gender

# 测试:
def test():
    bart = Student('Bart',88, 'male')
    assert bart.get_gender() == 'male'
    bart.set_gender('female')
    assert bart.get_gender() == 'female'
    print('测试成功!')

if __name__ == "__main__":
    test()
