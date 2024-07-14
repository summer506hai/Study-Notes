class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

    def __str__(self):
        return 'Student object (name: %s)' % self.name

s = Student('Michael')
print(s)  #Student object (name: Michael)
s()  #My name is Michael.
