#클래스 인스턴스 출력하기 - class의 자동 string casting
class Coord(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return '({},  {})'.format(self.x, self.y)
point = Coord(10,20)
print(point)











