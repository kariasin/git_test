# from abc import *

# class Calc:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#         self.calc2 = Calc2(x,y)
#     def add(self):
#         return self.x + self.y
#     def subtract(self):
#         return self.x - self.y
#     def multiply(self):
#         return self.calc2.multiply()    
# class Calc2:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def add(self):
#         return self.x + self.y

#     def multiply(self):
#         return self.x * self.y

# ca = Calc(1,2)
# print(ca.multiply())
# calc2 = Calc(x=2,y=3)

# print(calc2.multiply())



# 클래스 설계해보기 1. 게임 캐릭터 클래스 만들기
# - attribute: name, health_point, striking_power, defensive_power
# - attribute 명시적 입력이 없으면, name='yourname', health_point=100, striking_power=3, defensive_power=3이 디폴트로 입력되도록 함
# - method: info() - 게임 캐릭터 name, health_point, striking_power, defensive_power 출력
# - 다음 시나리오가 동작할 수 있도록 작성

class Warrior:
    def __init__(self,name, health_point, striking_power, defensive_power):
        self.g = Game(name, health_point,striking_power,defensive_power)
    def info(self):
        self.g.info()
    def attack(self,elf1):
        self.g.attack(elf1)
class Elf:
    def __init__(self,name, health_point, striking_power, defensive_power):
        self.g = Game(name, health_point,striking_power,defensive_power)
    def info(self):
        self.g.info()
class Wizard:
    def __init__(self,name, health_point, striking_power, defensive_power):
        self.g = Game(name, health_point,striking_power,defensive_power)
    def info(self):
        self.g.info()        
class Game():
    def __init__(self,name, health_point=100, striking_power=3, defensive_power=3):
        self.name = name
        self.health_point = health_point
        self.striking_power = striking_power
        self.defensive_power = defensive_power
    def info(self):
        print(self.name, self.health_point,self.striking_power,self.defensive_power)
    def attack(self,obj):
        #print(obj['name'] + " 칼로 찌르다")
        obj['health_point'] -= self.striking_power
        return obj
war = Warrior("Warrior",100,3,3)

elf2 = {"name":"Elf", "health_point":100, "striking_power":1, "defensive_power":3}
#war.attack(elf2)
for i in range(0,34):
    war.attack(elf2)
if elf2['health_point'] < 0:
    print('die')
#print(war.info())
print(elf2)





