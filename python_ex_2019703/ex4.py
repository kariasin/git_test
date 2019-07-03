class Figure:
    def __init__(self,name,color):
        self.name = name
        self.color = color
class Quadrangle(Figure):
    def set_area(self,width,height):
        self.__width = width
        self.__height = height

    def get_info(self):
        print(self.name,self.color,self.__width * self.__height)

square = Quadrangle('dave','blue')
square.set_area(5,5)
square.get_info()


print(issubclass(Quadrangle,Figure))

figure1 = Figure('figure1','black')
square = Quadrangle('square','red')



print(isinstance(figure1, Figure))
print(isinstance(square, Figure))
print(isinstance(figure1, Quadrangle))
print(isinstance(square, Quadrangle))



# class Figure():
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
# class Quadrangle(Figure):
#     def set_area(self,width,height):
#         self.__width = width
#         self.__height = height

#     def get_info(self):
#         print(self.name,self.color,self.__width * self.__height)

# square = Quadrangle('square1','black')
# square.set_area(5,5)
# square.get_info()