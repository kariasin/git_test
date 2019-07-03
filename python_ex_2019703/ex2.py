# protected
# 파이썬에서는 해당 속성의 앞에 _(single underscore) 를 붙여서 표시만 함
# 실제 제약되지는 않고 일종의 경고 표시로 사용됨

# class Quadrangle:
#     def __init__(self, width, height, color):
#         self._width = width
#         self._height = height
#         self._color = color

#     def get_area(self):
#         return self._width * self._height
    
#     def _set_area(self, width, height):
#         self._width = width 
#         self._height = height

# square = Quadrangle(5,5,'black')
# print(square.get_area())
# print(square._width)
# square._width = 10
# print(square.get_area())
# square._set_area(3,3)
# print(square.get_area())


# dir (square)


# private
# - 파이썬에서는 attribute, method 앞에 __(double underscore)를 붙이면 실제로 해당 이름으로 접근이 허용되지 않음
# - 실은 __(double underscore)를 붙이면, 해당 이름이 _classname__해당 속성 또는 메소드 이름 으로 변경되기 때문임
class Quadrangle:
    def __init__(self, width, height, color):
        self.__width = width
        self.__height = height
        self.__color = color

    def get_area(self):
        return self.__width * self.__height
    
    def __set_area(self, width, height):
        self.__width = width 
        self.__height = height

square = Quadrangle(5, 5, "black")

dir(square)


print(square.get_area())

# error
# print(square.__width)
# square.__width = 10
# square.__set_area(3,3)


class circle:
    def __init__(self,width,name):
        self.width = width
        self.name = name
    
    def get_name(self):
        return self.name

    def get_area(self):
        return self.width ** 2 * 3.14

    def get_length(self):
        return self.width * 2 * 3.14
c1 = circle(3,'test')

print(c1.get_name())
print(c1.get_length())
print(c1.get_area())










