class Figure:
    def __init__(self, width, height):
        self.width = width
        self.height = height 
class Quadrangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __add__(self, second):    
        return Quadrangle(self.width + second.width, self.height + second.height)
    
    # 연산자 곱셈    
    def __mul__(self, num):
        return Quadrangle(self.width * num, self.height * num)

    # 연산자 len() - 길이    
    def __len__(self):
        return self.width ** 2 + self.height ** 2

    # 연산자 A[index] - 리스트    
    def __getitem__(self, index):
        if index == 0:
            return self.width
        elif index == 1:
            return self.height

    # 연산자 str() - 문자열 변환           
    def __str__(self):
        return 'width : {}, height : {}'.format(self.width, self.height)

rectangle1 = Quadrangle(2, 3)
figure1 = Figure(3, 4)
rectangle2 = rectangle1 + figure1
rectangle2.width

rectangle1 = Quadrangle(2, 3)
# rectangle3 = rectangle1 + 4
# print(rectangle3.width)
# print(rectangle3.width,rectangle3.height)
# rectangle4 = rectangle1 * 3
# print(str(rectangle1))
# print(str(rectangle4))
print(rectangle2[0],rectangle2[1])
print(len(rectangle1))

# figure1 = Figure(3,4)
# rectangle2 = rectangle1 + figure1

# print(rectangle2.width)
# print(rectangle3.width)
