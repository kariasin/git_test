# 게임 캐릭터는 다음과 같이 3명이 존재함
# Warrior
#  - name: 원하는이름으로!  health_point = 100  striking_power = 3  defensive_power = 1
#  - attack: 상대방 객체를 입력받아서, '칼로 찌르다' 출력하고, 상대방의 receive 메서드를 호출해서, striking_power만큼 상대방의 health_point를 낮춰준다.
#  - receive: 상대방의 striking_point를 입력으로 받아서, 자신의 health_point를 그만큼 낮추기, health_point가 0 이하이면 '죽었음' 출력
# Elf
#  - name: 원하는이름으로!  health_point = 100  striking_power = 1  defensive_power = 3
#  - attack: 상대방 객체를 입력받아서, '마법을 쓰다' 출력하고, 상대방의 receive 메서드를 호출해서, striking_power만큼 상대방의 health_point를 낮춰준다.
#  - receive: 상대방의 striking_point를 입력으로 받아서, 자신의 health_point를 그만큼 낮추기, health_point가 0 이하이면 '죽었음' 출력 
#  - wear_manteau: 1번 공격을 막는다.
# Wizard
#  - name: 원하는이름으로!  health_point = 50  striking_power = 2  defensive_power = 2
#  - attack: 상대방 객체를 입력받아서, '마법을 쓰다' 출력하고, 상대방의 receive 메서드를 호출해서, striking_power만큼 상대방의 health_point를 낮춰준다.
#  - receive: 상대방의 striking_point를 입력으로 받아서, 자신의 health_point를 그만큼 낮추기, health_point가 0 이하이면 '죽었음' 출력 
#  - use_wizard: 자신의 health_point를 3씩 올려준다.


from abc import *
health_point_sample = 100
class Character(metaclass=ABCMeta):
    def __init__(self, name='yourname', health_point=100, striking_power=3, defensive_power=3):
        self.name = name
        self.health_point = health_point
        self.striking_power = striking_power
        self.defensive_power = defensive_power
    def get_info(self):
        print(self.name, self.health_point, self.striking_power, self.defensive_power)

    @abstractmethod
    def attack(self,second):
        pass

    @abstractmethod
    def receive(self,second):
        pass

    @abstractmethod
    def change_name(self,name):
        pass
    
    @abstractmethod
    def recover(self):
        pass
class Warrior(Character):
    def __init__(self, name='yourname', health_point=100, striking_power=3, defensive_power=3):
        super().__init__()
    def attack(self,second):
        print("칼로 찌르다")
        second.receive(self.striking_power)
    def receive(self,striking_power):
        self.health_point = self.health_point - striking_power
        if(self.health_point < 0):
            print('die')
    def change_name(self,name):
        self.name = name
    def recover(self):
        self.health_point = health_point_sample

class Elf(Character):
    def __init__(self, name='yourname', health_point=100, striking_power=3, defensive_power=3):
        super().__init__()
        self.manteau = 0
    def attack(self,second):
        second.receive(self.striking_power)
    def receive(self,striking_power):
        self.health_point = self.health_point - striking_power
        if(self.health_point < 0):
            print('die')
        else:
            self.manteau -= 0

    def wear_manteau(self):
        self.manteau += 1
    
    def change_name(self,name):
        self.name = name

    def recover(self):
        self.health_point = health_point_sample

class Wizard(Character):
    def __init__(self,name,health_point,striking_power,defensive_power):
        super().__init__()
    def attack(self,second):
        print("마법 공격")
        second.receive(self.striking_power)
    def receive(self,striking_point):
        if self.health_point < 0 :
            print('die')
        else:
            self.health_point = self.health_point - striking_point
    def use_wizard(self):
        self.health_point += 3
    def change_name(self,name):
        self.name = name
    def recover(self):
        self.health_point = health_point_sample

warrior1 = Warrior()
warrior2 = Warrior()
elf1 = Elf(name='elf1', health_point=100,striking_power=1,defensive_power=3)
wizard1 = Wizard(name='elf1', health_point=50,striking_power=2,defensive_power=2)

# warrior1.attack(warrior2)
# print(warrior2.health_point)
# elf1.wear_manteau()
# warrior1.attack(elf1)
# print(elf1.health_point)

warrior1.attack(wizard1)
warrior1.attack(wizard1)
warrior1.attack(wizard1)
print(wizard1.health_point)

wizard1.use_wizard()
print(wizard1.get_info())

wizard1.change_name("test")
print(wizard1.get_info())

wizard1.recover()
print(wizard1.get_info())

print(Character.__mro__)