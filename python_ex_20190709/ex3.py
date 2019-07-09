import turtle as t

t.pensize(3)

class shape_triangle:
    def __init__(self):
        pass
    def view(self):
        print("삼각형")
    def draw(self,color,x,y):
        #print(color,x,y)
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.circle(40,steps=3)
class shape_quadrangle:
    def __init__(self):
        pass
    def view(self):
        print("사각형")
    def draw(self,color,x,y):
        #print(color,x,y)
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.circle(40,steps=4)
class shape_pentagon:
    def __init__(self):
        pass
    def view(self):
        print("오각형")
    def draw(self,color,x,y):
        #print(color,x,y)
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.circle(40,steps=5)
class shape_hexagon:
    def __init__(self):
        pass
    def view(self):
        print("육각형")
    def draw(self,color,x,y):
        #print(color,x,y)
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.circle(40,steps=6)
class shape_circle:
    def __init__(self):
        pass
    def view(self):
        print("원")
    def draw(self,color,x,y):
        print(color,x,y)
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.circle(40)

class Figure(object):
    def __init(self):
        pass
    
    def draw_shape(self,shape,color='red',x=100,y=100):
        if shape == 'triangle':
            s = shape_triangle()
        elif shape == 'quadrangle':
            print("사각형")
            s = shape_quadrangle()
        elif shape == 'pentagon':
            print("오각형")
            s = shape_pentagon()
        elif shape == 'hexagon':
            print("육각형")
            s = shape_hexagon()
        elif shape == 'circle':
            print("원")
            s = shape_circle()
        return s
    def Color(self,color):
        if color == 'red':
            print("빨강")
            s
        elif color == 'blue':
            print("파랑")
        elif color == 'black':
            print("검정")



f1 = Figure()
ff1 = f1.draw_shape('triangle')
ff1.view()
ff1.draw("red",-200,50)

ff2 = f1.draw_shape('quadrangle')
ff2.view()
ff2.draw("blue",-200,100)



ff2 = f1.draw_shape('circle')
ff2.view()
ff2.draw("blue",-200,150)







