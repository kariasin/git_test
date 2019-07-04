from abc import *

class Character(metaclass=ABCMeta):
    def __init__(self,hp):
        self.hp = hp
    def get_hp(self):
        return self.hp    
    @abstractmethod
    def attack(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

class Elf(Character):
    def attack(self):
        print("practice the black art")

    def move(self):
        print("fly")

class Human(Character):
    def attack(self):
        print("plunge a knife")

    def move(self):
        print("run")

# elf1 = Elf()
# human1 = Human()

# elf1.attack()
# elf1.move()
# human1.attack()
# human1.move()

character1 = Elf(10)
print(character1.get_hp())


# * Car class 추상 클래스 만들기
# - attribute: 자동차 이름 - method: info(self) - 이름 출력
# - abstract method: fuel(self)

# - Eletronic Car class
# - attribute: 생성자에서 self.name 설정
# - method: info(self) - 이름 출력
# - method: fuel(self) - 사용 연료(Eletronic) 출력

from abc import *
class Car(metaclass=ABCMeta):
    def __init__(self,name):
        self.name = name
    def get_info(self):
        print(self.name)

    @abstractmethod
    def fuel(self):
        pass
class Elecronic_car(Car):
    def fuel(self):
        print("Eletronic")        
e1 = Elecronic_car("test")
e1.get_info()
e1.fuel()
