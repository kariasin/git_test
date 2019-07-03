#class 기본 
class Quadrangle:
    width = 0
    height = 0
    color = "black"

    def get_area(self):
        return self.width * self.height
    def set_area(self,width,height,color):
        self.width = width
        self.height = height
        self.color = color
square = Quadrangle()

print(square.width)
print(square.get_area())


# * 위에서 작성한 Quadrangle 클래스를 기반으로 직사각형 1개 객체와 정사각형 1개 객체를 만들고, 각 사각형 너비 출력하기
# - 직사각형2개 속성: width=10, height=5, color='red'
# - 정사각형2개 속성: width=7, height=7, color='blue'

t1 = Quadrangle()
t2 = Quadrangle()

t1.set_area(10,5,'red')
t2.set_area(7,7,'blue')

print(t1.get_area(),t1.color)
print(t2.get_area(),t2.color)


class Quadrangle:
    #생성자 __init__(self)
    def __init__(self,width,height,color):
        self.width = width
        self.height = height
        self.color = color
    def __del__(self):
        print("Quadrangle object is deleted")
square = Quadrangle(5,5,"red")

print(square.width,square.height,square.color)

del square



# 한발짝 더 나가보기!(심화 문제)
# * 정삼각형 클래스를 만들고, 너비 출력하기
# - attribute: 정삼각형 한 변의 길이, 삼각형 이름
# - method: 정삼각형 너비 리턴
# - 힌트: 정삼각형 한 변의 길이를 self.length 라고 할 때, 다음 식은 (math.sqrt(3) / 2) * self.length**2 와 같이 작성 가능 (import math 선언 후)
# 3–√2∗정삼각형한변의길이2
import math


class Figure:
    def __init__(self,length,name):
        self.length = length
        self.name = name
    def get_area(self):
        return (math.sqrt(3) / 2 ) * self.length ** 2 #(math.sqrt(3) / 2) * math.pow(self.length,2)   
    def get_name(self):
        return self.name
    def __del__(self):
        print("object is deleted")

square = Figure(10,'dave')
print(square.get_area(), square.get_name())
del square





