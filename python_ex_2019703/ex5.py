# class Person:
#     def __init__(self,name):
#         self.name = name
#     def work(self):
#         print(self.name + " works hard")    
# class Student(Person):
#     def study(self):
#         print(self.name + " studies hard")

#     def go_to_school(self):
#         print("Go to school")

# class Employee(Person):
#     def work(self):
#         print(self.name + " works hard")


#student1 = Student("test")
# student1.work()
# student1.go_to_school()


##############################################################
# * Car class 만들기
# - Car class
# - attribute: 생성자에서 self.name 설정
# - method: info(self) - 이름 출력

# - Eletronic Car class
# - attribute: 생성자에서 self.name 설정
# - method overide: info(self) - 이름과 사용 연료(Eletronic) 출력

# - Gasoline Car class
# - attribute: 생성자에서 self.name 설정
# - method overide: info(self) - 이름과 사용 연료(Gasoline) 출력


class Car():
    def __init__(self,name):
        self.name = name
    def info(self):
        print(self.name)
class Electronic_Car(Car):
    def info(self):
        print(self.name, "Electronic")

class Gasoline_Car(Car):
    def info(self):
        print(self.name, "Gasoline")

c1 = Car("Car")
c2 = Electronic_Car("Electronic_Car")
c3 = Gasoline_Car("Gasoline_Car")


print(c2.info(), c3.info())
