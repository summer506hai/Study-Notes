#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,height):
        self._height = height


    @property
    def resolution(self):
        return self._height * self._width

if __name__ == "__main__":
    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)
    assert s.resolution == 786432
    print('测试通过!')

