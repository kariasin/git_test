class Figure:
    count = 0 # 클래스 변수

    #생성자
    def __init__(self,width,height):
        #self.* : 인스턴스변수
        self.width = width
        self.height = height
        #클래스 변수 접근 예
        Figure.count += 1
    def __del__(self):
        Figure.count -= 1    

    # 메서드
    def calc_area(self):
        return self.width * self.height
print(Figure.count)
figure1 = Figure(2, 3)
print(Figure.count)
figure2 = Figure(4, 5)
print(Figure.count)
print(figure1.width)
print(figure2.width)
del figure1
print(Figure.count)
del figure2
print(Figure.count)
